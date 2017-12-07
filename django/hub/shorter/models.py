from django.db import models



class ShortUrl(models.Model):
    name = models.CharField(max_length=50)
    long = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' (' + self.long + ')'