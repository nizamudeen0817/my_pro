from django.db import models

# Create your models here.
class Ekartcard(models.Model):
    img=models.ImageField(upload_to='pic')
    title=models.CharField(max_length=100)
    dis=models.CharField(max_length=100)
    
    
class Productcard(models.Model):
    img=models.ImageField(upload_to='pic')
    title=models.CharField(max_length=100)
    dis=models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    name=models.CharField(max_length=100)
    phn=models.CharField(max_length=100)
    title=models.ForeignKey(Productcard, on_delete=models.CASCADE)
    bookingdate=models.DateField()

    def __str__(self):
        return self.name   
    