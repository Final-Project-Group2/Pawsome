from django.db import models
from django.utils.timezone import now
from backend.models import Breed, Status , Media, Description, Species, Sizes
from .more_settings import species_options, sizes_options,TWO_VALUES_OPT
# Create your models here.
from django.contrib.auth.models import AbstractUser

class Pet(models.Model):

      @property
      def dateAdded(self):
            if self.__date_added is None:
                self.__date_added=now  
            return self.__date_added

      name = models.CharField(max_length=50)
      species = models.ForeignKey(Species,null=False, on_delete=models.CASCADE,verbose_name="species",blank=False,choices=TWO_VALUES_OPT["SPECIES"],default="dog")
      size = models.ForeignKey(Sizes,null=False, on_delete=models.CASCADE,verbose_name="sizes",blank=False,choices = TWO_VALUES_OPT["SIZE"], default = "small" )
      breed = models.ForeignKey(Breed,null=True, on_delete=models.CASCADE,verbose_name="breed",choices=TWO_VALUES_OPT["BREED"])
      age = models.IntegerField(null=True)
      gender = models.CharField(max_length=50, choices=TWO_VALUES_OPT["GENDER"],default="Male")
      weight = models.IntegerField(null=True)
      description = models.ForeignKey(Description,null=True, on_delete=models.CASCADE,verbose_name="description")
      image = models.ForeignKey(Media,null=True, on_delete=models.CASCADE,verbose_name="media")
      status = models.ForeignKey(Status,null=False, on_delete=models.CASCADE,verbose_name="status",blank=False,choices=TWO_VALUES_OPT["STATUS"], default="Available")
      date_added = dateAdded #models.DateField(default=now,auto_created=True ,editable=False)
      date_uploaded = models.DateField(default=now,auto_created=True,editable=False)
      __date_added = None
      
      
      def __str__(self):
            short_details = f"{self.specie} - {self.breed} - {self.status}"
            return short_details

      
      #def __repr__(self):
      #      specific_details = f'''
      #      
      #      "Specie" :"{self.species}"
      #      "Breed" : "{self.breed}"
      #      "Name" : "{self.name}"
      #      "Size" : "{self.size}"
      #      "Age" : "{self.age}"
      #      "Gender" : "{self.gender}"
      #      "Weight" : "{self.weight}"
      #      "Description" : "{self.description}"
      #      "Image" : "{self.image}"
      #      "Status" : "{self.status}"
      #      "Date__Added" : "{self.date_added}"
      #      "Last_Update" : "{self.date_uploaded}"
      #      '''
      #      return specific_details
      

class CustomerUser(AbstractUser):

      username = models.CharField(max_length=50, unique=True,blank=False)
      email = models.EmailField(max_length=50,blank=False, unique=True)
      password = models.CharField(max_length=50)
      first_name = models.CharField(max_length=50)
      last_name =  models.CharField(max_length=50)
      address = models.CharField(max_length=100)
      phone_number = models.BigIntegerField(null=True)
      image = models.ForeignKey(Media,null=True, on_delete=models.CASCADE,verbose_name="media")
      __authtoken = ''

      def __str__(self):
            return f"{self.username} {self.first_name}"