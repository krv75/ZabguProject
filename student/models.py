from django.db import models

class WatchingLectures(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=400)
    file = models.FileField(upload_to='lectures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class WatchingMethodicalmaterial(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=400)
    file = models.FileField(upload_to='methodical_material/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class LinksLibraries(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title