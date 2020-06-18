from django.db import models


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    dis = models.CharField(max_length=500)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class News_blog(models.Model):
    img2 = models.ImageField(upload_to='blog_pics')
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    post_blog_title = models.CharField(max_length=100)
    title_category = models.CharField(max_length=100)
    post_blog_summary = models.CharField(max_length=300)

    def __str__(self):
        return self.post_blog_title