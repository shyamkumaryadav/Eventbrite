from django.urls import path
from .views import EventsListView, SignupView, userLike, EventsLikeView, EventCreateView

urlpatterns = [
    path('', EventsListView.as_view(), name="list_event"),
    path('add/', EventCreateView.as_view(), name="add_event"),
    path('events_like', EventsLikeView.as_view(), name="events_like"),
    path('like/', userLike, name="like_event"),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/profile/', EventsListView.as_view()),
]