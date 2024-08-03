from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, unique=True)
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.branch} - {self.ifsc}"