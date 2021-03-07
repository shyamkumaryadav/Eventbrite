from django.urls import path
from .views import EventsListView, SignupView, userLike, EventsLikeView, EventCreateView, EventDetailView, UserUpdateView

urlpatterns = [
    path('', EventsListView.as_view(), name="list_event"),    
    path('event/<pk>/', EventDetailView.as_view(), name="detail_event"),    
    path('add/', EventCreateView.as_view(), name="add_event"),
    path('events_like', EventsLikeView.as_view(), name="events_like"),
    path('like/', userLike, name="like_event"),
    path('accounts/<pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/profile/', EventsListView.as_view()),
]