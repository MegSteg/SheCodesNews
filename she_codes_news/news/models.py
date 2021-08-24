from django.contrib.auth import get_user_model
from django.db import models

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    image_url = models.URLField(max_length=400, default= "https://picsum.photos/600")
    content = models.TextField()

    class Meta:
        ordering = ['-pub_date']
