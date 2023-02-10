
from django.db import models
from django.contrib.auth.models import User

# from django.contrib.staticfiles import static

# Create your models here.

class UserProfile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, ("Pria")),
        (GENDER_FEMALE, ("Wanita")),
    ]
    user     = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar   = models.ImageField(upload_to="users/profiles/avatars/", null=True, blank=True)
    gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone    = models.CharField(max_length=32, null=True, blank=True)
    nik      = models.CharField(max_length=32, null=True, blank=True)
    # address  = models.CharField(max_length=255, null=True, blank=True)
    # city     = models.CharField(max_length=50, null=True, blank=True)
    # zip      = models.CharField(max_length=30, null=True, blank=True)

    @property
    def get_avatar(self):
        return self.avatar.url
        #  if self.avatar else static('images/team/default-profile-picture.png')
