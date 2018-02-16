from django.db import models
from django.utils.encoding import smart_text


# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = "article"

    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return smart_text(self.title)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    text = models.TextField(verbose_name="Комментарий:")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
