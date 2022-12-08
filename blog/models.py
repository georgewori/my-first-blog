from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model): #class is a special key dat defines our model(Post object)
    #models.Model means dat Post is a Django Model so Django knows it shd be saved in da DB

    # 

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        # Link to another model

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # fn/method with name publish
        # Notice all methods are indented inside class Post
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



