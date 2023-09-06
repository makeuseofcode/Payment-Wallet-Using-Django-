from django.db import models

class Wallet(models.Model):
    user = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    date_created  =  models.DateTimeField(auto_now_add=True)
    date_modified  =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

class  Transaction(models.Model):
	wallet  =  models.ForeignKey(Wallet, on_delete=models.CASCADE)
	amount  =  models.DecimalField(max_digits=10, decimal_places=2)
	timestamp  =  models.DateTimeField(auto_now_add=True)
    
    