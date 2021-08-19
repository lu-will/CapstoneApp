from django.db import models
from django.contrib.auth.models import User


# Model for day prompts
class day(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name="dayjournal", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    prompt_1 = models.TextField(max_length=200)
    prompt_2 = models.TextField(max_length=200)
    prompt_3 = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.date}'

# Model for evening prompts


class evening(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='nightjournal', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    prompt_1 = models.TextField(max_length=200)
    prompt_2 = models.TextField(max_length=200)
    prompt_3 = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.date}'


# Model for users
class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
