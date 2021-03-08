from django.db import models
from django.core import validators, exceptions
from django.contrib.auth import get_user_model
from django.template.defaultfilters import filesizeformat

User = get_user_model()
file_size = 1024*1024*0.2
def profile_size(value):
    if value.size > file_size:
        raise exceptions.ValidationError(f"Image size is {filesizeformat(value.size)} which is not less than or equal to {filesizeformat(file_size)}")

# ‘name’, ’data’ ,’time’, ‘location’ ,’image’, ‘is_liked’

class EventModel(models.Model):
    name = models.CharField("Event Name", max_length=100)
    data = models.TextField("About")
    time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150)
    image = models.FileField(upload_to='event/%Y/',help_text=f"Select valid Image file and size is less than or equal to {filesizeformat(file_size)}.",null=True, blank=True, validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Image."),
                profile_size,
            ],)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('update_event', args=str(self.pk))


class UserLikeEvent(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'event',)
    
    def __str__(self):
        return f"{self.user} like {self.event}"