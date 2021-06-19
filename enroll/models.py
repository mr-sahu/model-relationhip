from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class One2one(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_title=models.CharField(max_length=10)
    page_cat=models.CharField(max_length=10)
    publish_date=models.DateField()


class Many2one(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song_name=models.CharField(max_length=15)
    song_duration=models.IntegerField()

class Many2Many(models.Model):
    user=models.ManyToManyField(User)
    song_name=models.CharField(max_length=15)
    song_duration=models.IntegerField()

    def written_by(self):
        return ",".join([str(f) for f in self.user.all()])