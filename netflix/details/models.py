from django.db import models

# Create your models here.
# class User(models.Model):
#     user_id=models.EmailField(unique=True)
#     password=models.CharField(max_length=128)

# ------------------------------------------------------------------------------------------------------------------

class User(models.Model):
    user_id = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user_id


class Profile(models.Model):
    # us_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    video=models.ManyToManyField('Video')
    image=models.ImageField(upload_to='cover')

    def __str__(self):
        return self.name
    
class Video(models.Model):
    Title =models.CharField(max_length=100)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.Title