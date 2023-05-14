from django.db import models


class BotInfo(models.Model):
    text = models.CharField(max_length=255)


class Modules(models.Model):
    type = models.IntegerField(default=1, choices=(
        (1, 'listening🎧'),
        (2, 'reading📚'),
        (3, 'speaking🗣'),
        (4, 'writing✍'),
    ))


class Category(models.Model):
    typee = models.ForeignKey(Modules, on_delete=models.CASCADE)
    about = models.TextField()
    # image = models.ImageField(upload_to='media/')
    source = models.URLField()
    # materials = models.FileField()

