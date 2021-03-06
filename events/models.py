from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model

User = get_user_model()

# ‘event_name’, ’data’ ,’time’, ‘location’ ,’image’, ‘is_liked’

class EventModel(models.Model):
    event_name = models.CharField("Event Name", max_length=100)
    data = models.TextField("About")
    time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150)
    image = models.FileField(upload_to='event/%Y/', validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Image."),
            ],)
        
    def __str__(self):
        return self.event_name


class UserLikeEvent(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'event',)
    
    def __str__(self):
        return f"{self.user} <3 {self.event}"