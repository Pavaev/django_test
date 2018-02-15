from django.db import models
from django.utils.encoding import smart_text


# Create your models here.

class Header(models.Model):
    class Meta():
        db_table = "header"

    title = models.CharField(max_length=100)

    def __str__(self):
        return smart_text(self.title)
