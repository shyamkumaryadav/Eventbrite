from django.urls import path
from django.views.generic import TemplateView
from .views import EventsListView, SignupView, userLike, EventsLikeView, EventCreateView, EventDetailView, UserUpdateView, EventUpdateView

urlpatterns = [
    path('', EventsListView.as_view(), name="list_event"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('terms/', TemplateView.as_view(template_name="terms.html"), name="terms"),
    path('add/', EventCreateView.as_view(), name="add_event"),
    path('update/<pk>/', EventUpdateView.as_view(), name="update_event"),
    path('event/<pk>/', EventDetailView.as_view(), name="detail_event"),
    path('events_like', EventsLikeView.as_view(), name="events_like"),
    path('like/', userLike, name="like_event"),
    path('accounts/<pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/profile/', EventsListView.as_view()),
]