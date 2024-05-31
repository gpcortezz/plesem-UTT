from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Area

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=128, default="I love plesem system")
    avatar = models.ImageField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=User)
def auto_profile(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance, slug=instance.username)