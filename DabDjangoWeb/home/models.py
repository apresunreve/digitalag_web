from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    third_party_name = models.CharField(max_length=255)
