from django.db import models

# Create your models here.
class Category(models.Model):
    topics = models.CharField(max_length=100)

    def __str__(self):
        return self.topics


class Post(models.Model):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')
    caption = models.TextField(default='')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title