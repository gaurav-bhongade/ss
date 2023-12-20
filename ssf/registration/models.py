from django.db import models

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)

    class Meta:
        db_table = "site_details"

    def __str__(self):
        return f'''{self.__dict__}'''
    
    def __repr__(self):
        return str(self)

class Pipe_Laying(models.Model):
    label = models.CharField(max_length = 20)
    start_node = models.CharField(max_length = 20)
    stop_node = models.CharField(max_length = 20)
    length = models.IntegerField()
    diameter_id = models.IntegerField()
    diameter_od = models.IntegerField()
    material = models.CharField(max_length = 20)
    laying_length = models.CharField(max_length = 20, null=True, blank = True)
    balance_laying = models.IntegerField()

    class Meta:
        db_table = "pipe_layings"

    def __str__(self):
        return f'''{self.__dict__}'''
    
    def __repr__(self):
        return str(self)
    
