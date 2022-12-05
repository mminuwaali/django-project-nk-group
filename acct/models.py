from django.db import models
from main.models import Icon
from django.contrib.auth.models import User

def user_profile_upload(self, image) -> str:
    return f'profiles/{self.user.username}/{image}'

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile = models.FileField(upload_to=user_profile_upload)
    team_member = models.BooleanField(default=False)
    proffession = models.CharField(max_length=50)
    info = models.TextField(default='')
    
class SocialMedia(models.Model):
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media')
    
    class Meta:
        verbose_name_plural = 'social media'
    
