from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import UserLikeEvent, EventModel
from django.urls import reverse_lazy
import json
from .models import UserLikeEvent, EventModel

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


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
        raise Http404("yes, i am liked you!")

class EventsLikeView(LoginRequiredMixin, generic.ListView):
    model = UserLikeEvent
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return self.model._default_manager.filter(user=self.request.user)

class EventCreateView(LoginRequiredMixin, generic.CreateView):
    model = EventModel
    fields = '__all__'
    success_url = reverse_lazy('list_event')

class EventsListView(generic.ListView):
    model = EventModel
    search_kwarg = 'q'
    paginate_by = 10
    
    # extra_context = {
    #     'userlike': UserLikeEvent
    # }
    

    # def get_queryset(self, *args, **kwargs):
    #     search_kwarg = self.search_kwarg
    #     name = self.request.GET.get(search_kwarg)
    #     if name:
    #         object_list = self.model._default_manager.filter(
    #             event_name__icontains=name)
    #     else:
    #         object_list = self.model._default_manager.all()
    #     return object_list
    
    # def get_context_data(self, **kwargs):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         print("*****************")
    #         kwargs['userLike'] = UserLikeEvent.objects.filter(user=user)
    #     print(kwargs)
    #     return super().get_context_data(**kwargs)
