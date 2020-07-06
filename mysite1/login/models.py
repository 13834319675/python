from django.db import models

# Create your models here.
class User(models.Model):

    gander={
        ("male","男"),
        ("female","nv"),
    }

    name = models.CharField(max_length=120,unique=True)
    password = models.CharField(max_length=256)
    emall = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gander,default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Mate:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"