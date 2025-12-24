from django.db import models

class DownloadLecture(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=400)
    file = models.FileField(upload_to='lectures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class DownloadMethodicalmaterial(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=400)
    file = models.FileField(upload_to='methodical_material/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class MyDocuments(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=400)

class MyMethodicalmaterial(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=400)

