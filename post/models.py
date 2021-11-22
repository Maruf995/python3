from django.db import models


class BlogPost(models.Model):
    image = models.FileField(upload_to="post_images/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)

    def get_absolute_url(self):
        return f"/blog/{self.pk}"
