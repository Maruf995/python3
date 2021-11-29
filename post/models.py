from django.db import models

class BlogPost(models.Model):
    image = models.FileField(upload_to="post_images/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=150)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    # def __str__(self):

