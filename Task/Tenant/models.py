from django.db import models
from django.db.models.fields import PositiveIntegerField

# Create your models here.

# Tenant App => Create Monthly Expenditure | Fetch the data form db | Update the data for correction | Delete Date if wrong.

class Tenant(models.Model):
    MONTH_CHOICES = (
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December'),
    )
    name = models.CharField(max_length=100,blank=True, null=True,verbose_name="Person Name")
    occupant = models.PositiveIntegerField(blank=True, null=True,verbose_name="Occupant")
    month = models.CharField(max_length=9,choices=MONTH_CHOICES,blank=True, null=True,verbose_name="Month")
    rent = models.PositiveIntegerField(blank=True, null=True,verbose_name="Rent")
    electricity = models.PositiveIntegerField(blank=True, null=True,verbose_name="Electricity Bill")
    water = models.PositiveIntegerField(blank=True, null=True,verbose_name="Water Bill")
    food = models.PositiveIntegerField(blank=True, null=True,verbose_name="Food Bill")
    other_bills = PositiveIntegerField(blank=True, null=True,verbose_name="Other Expenses")
    total = models.PositiveIntegerField(blank=True, null=True,verbose_name="Total Bill")

    
    def save(self,*args,**kwargs):
        self.rent = self.rent
        self.electricity= self.electricity
        self.water = self.water
        self.food = self.food
        self.other_bills = self.other_bills
        if self.rent or self.electricity or self.water or self.food or self.other_bills:
            self.total = self.rent+self.electricity+self.water+self.food+self.other_bills
        super(Tenant,self).save(*args,**kwargs)

    def __str__(self):
        return f'No. of Occupant: {self.occupant}'
    

