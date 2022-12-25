from django.db import models
from django.contrib.auth.models import User

def custom_file_name(instance, filename):
    return f'profile/{instance.user.username}-{filename}'

class Profile(models.Model):
    GENDER = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'))

    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=custom_file_name ,default = 'default-profile.png', null = True, blank = True)
    gender = models.CharField(max_length = 10, choices = GENDER, null=True)
    address = models.TextField(null = True, blank=True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return f'@{self.user.username}\'s Profile'