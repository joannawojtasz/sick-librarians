from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
TYPE = ((0, "News"), (1, "Review"))



class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    type = models.IntegerField(choices=TYPE, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    id = models.CharField(null=False, primary_key=1, max_length=70)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    parent = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
