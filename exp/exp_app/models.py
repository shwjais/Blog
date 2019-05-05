from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE )
    # author=models.CharField(max_length=40)
    title=models.CharField(max_length=40)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField()


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
