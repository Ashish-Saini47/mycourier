from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField( max_length=254)
    name =models.CharField(max_length= 120)
    phone = models.IntegerField()
    query = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Courier_detail(models.Model):
    name =models.CharField(max_length=120)
    contact_no=models.IntegerField()
    p_address=models.CharField(max_length=200)
    pincode=models.IntegerField()
    p_type=models.CharField(max_length=50)
    t_weight=models.IntegerField()
    p_decs=models.TextField(max_length=200)
    p_time=models.TimeField()
    p_n_time=models.CharField(max_length=2)
    r_name=models.CharField(max_length=120)
    r_contact_no=models.IntegerField()
    d_address=models.CharField(max_length=200)
    d_pincode=models.IntegerField()
    date = models.DateField()


    def __str__(self):
        return self.name