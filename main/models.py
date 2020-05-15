from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class m_ClassField(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.class_name)


class Cupboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user) + "'s closet"


class Dress(models.Model):
    cupboard = models.ForeignKey(Cupboard, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    prediction = models.ForeignKey(m_ClassField, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.cupboard) + str(self.prediction)
