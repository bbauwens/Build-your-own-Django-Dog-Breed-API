from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE,related_name='dogs')
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Breed(models.Model):
    SIZE_BREED = {
	"T": "TINY",
	"S": "SMALL",
	"M": "MEDIUM",
	"L": "LARGE",
    }
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100, choices=SIZE_BREED)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

    def_str_(self):
    	return self.name 
