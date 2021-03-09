from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import UserLikeEvent, EventModel
from django.urls import reverse_lazy
import json
from django_filters.views import FilterView
from .models import UserLikeEvent, EventModel


User = get_user_model()

def ErrorView(request, *args, **kwargs):
    return render(request, template_name="Error.html", context=kwargs)

def View404(request, *args, **kwargs):
    kwargs.update({
        'code':404
    })
    return ErrorView(request, *args, **kwargs)

def View505(request, *args, **kwargs):
    kwargs.update({
        'code': 505
    })
    return ErrorView(request, *args, **kwargs)

def View500(request, *args, **kwargs):
    kwargs.update({
        'code': 500
    })
    return ErrorView(request, *args, **kwargs)


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserUpdateView(generic.UpdateView):
    model = User
    # form_class = UserChangeForm
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('list_event')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.pk != int(kwargs['pk']):
            raise Http404("Yes, I love You!")
        return super().dispatch(request, *args, **kwargs)

def userLike(request):
    if request.method == "POST" and request.user.is_authenticated:
        if request.is_ajax():
            event_id = json.load(request)['event_id']
            event = get_object_or_404(EventModel, pk=event_id)
            liked, is_like = UserLikeEvent.objects.get_or_create(event=event, user=request.user)
            if not is_like:
                liked.delete()
            return JsonResponse({'is_like': is_like}, safe=True)
    else:
        raise Http404("Yes, I love You!")

class EventsLikeView(LoginRequiredMixin, generic.ListView):
    model = UserLikeEvent
    paginate_by = 12

    def get_queryset(self, *args, **kwargs):
        return self.model._default_manager.filter(user=self.request.user)

class EventCreateView(LoginRequiredMixin, generic.CreateView):
    model = EventModel
    fields = '__all__'
    extra_context = {
        'form_label': 'Add Event',
    }
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise Http404("Yes, I love You!")
        return super().dispatch(request, *args, **kwargs)

class EventsListView(FilterView):
    model = EventModel
    filterset_fields = {
            'name': ['icontains'],
        }
    template_name_suffix = '_list'
    paginate_by = 12
    ordering = ['-time',]
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'event_name_filter': [i.name for i in self.model._default_manager.all()]
        })
        return context

class EventDetailView(generic.DetailView):
    model = EventModel

class EventUpdateView(generic.UpdateView):
    model = EventModel
    fields = '__all__'
    extra_context = {
        'form_label': 'Update Event',
    }
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise Http404("Yes, I love You!")
        return super().dispatch(request, *args, **kwargs)
