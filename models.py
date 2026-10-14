from django.db import models

# Create your models here.

class Breed(models.Model):
    SIZE_BREED = {
	"T": "TINY",
	"S": "SMALL",
	"M": "MEDIUM",
	"L": "LARGE",
    }
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100, choices=SIZE_BREED)
    friendliness = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
    	return self.name 

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