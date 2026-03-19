from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post_slug   = models.SlugField()
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    text        = models.TextField()
    likes       = models.IntegerField(default=0)
    dislikes    = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:40]}"

class Reply(models.Model):
    comment    = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:40]}"
