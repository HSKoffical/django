from django.db import models
class movies_db(models.Model):
    name=models.CharField(max_length=40)
    actor=models.CharField(max_length=30)
    actress=models.CharField(max_length=30)
    year=models.IntegerField()
    rating=models.IntegerField()


