from django.db import models, migrations


class Disaster(models.Model):
    DISASTERS = (
        ('drought', 'DROUGHT'),
        ('avalanche', 'AVALANCHE'),
        ('wildfire', 'WILDFIRE'),
        ('flood', 'FLOOD'),
        ('earthquake', 'EARTHQUAKE'),
        ('tsunami', 'TSUNAMI'),
        ('storm', 'STORMS'),
    )
    name = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to='static/images/disasters',
                             default='static/dish/images/disaster.jpg',
                             max_length = 500,
                             blank=True)
    state = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=2, choices=DISASTERS, null=False)
    date_started = models.DateField(null=False)
    #input_formats=["%B %Y"], 

class Person(models.Model):
    BLOOD_GROUPS = (
        ('O+', 'O-positive'),
        ('O-', 'O-negative'),
        ('A+', 'A-positive'),
        ('A-', 'A-negative'),
        ('B+', 'B-positive'),
        ('B-', 'B-negative'),
        ('AB+', 'AB-positive'),
        ('AB-', 'AB-negative'),
        ('X', 'UNKNOWN')
    )
    GENDERS = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('others', 'OTHERS')
    )
    STATUS = (
        ('found', 'FOUND'),
        ('missing', 'MISSING'),
        ('identified', 'IDENTIFIED')
    )
    name = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to='static/images/persons',
                             default='static/dish/images/person.jpg',
                             max_length = 500,
                             blank=True)
    specific_characteristics = models.CharField(max_length=300, null=False)
    location = models.CharField(max_length=300, null=True)
    clothing = models.CharField(max_length=300, null=False)
    age_estimate = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    alive = models.BooleanField(default=True, null=False)
    status = models.CharField(max_length=20, choices=STATUS, null=False)
    blood_group = models.CharField(max_length=2, choices=BLOOD_GROUPS, null=False)
    gender = models.CharField(max_length=11, choices=GENDERS, null=False)
    disaster = models.ForeignKey(Disaster, on_delete = models.CASCADE, default=False)