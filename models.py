from django.db import models

class register(models.Model):
    userid = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

    def __str__(self):
        return self.userid

class MediaItem(models.Model):
    CATEGORY_CHOICES = [
        ('song', 'Song'),
        ('album', 'Album'),
        ('artist', 'Artist'),
        ('radio', 'Radio'),
    ]

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)  # artist or description
    image = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.category})"






