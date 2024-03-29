from django.conf import settings
from django.db import models
from django.utils import timezone

#class - makes it an Object
#Post -  name of our model/Object
#models.Model - means Post is a Django Model... so it's saved in the database
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
