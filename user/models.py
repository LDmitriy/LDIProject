from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d')
    user_status = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
