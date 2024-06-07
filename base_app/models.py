from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Yangiliklar(models.Model):
    rasm = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.TextField()
    text = RichTextUploadingField()
    sana = models.DateTimeField()

    class Meta:
        ordering = ('-sana',)

    def __str__(self):
        return str(self.id)
