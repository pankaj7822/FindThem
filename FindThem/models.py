from django.db import models, migrations


class Disaster(models.Model):
    DISASTERS = (
        ('drought', 'Drought'),
        ('avalanche', 'Avalanche'),
        ('wildfire', 'Wildfire'),
        ('flood', 'Flood'),
        ('earthquake', 'Earthquake'),
        ('tsunami', 'Tsunami'),
        ('storm', 'Storm'),
    )
    name = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to='static/images/disasters',
                             default='static/dish/images/disaster.jpg',
                             max_length = 500,
                             blank=True)
    state = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=30, choices=DISASTERS)
    date_started = models.DateField()
    #input_formats=["%B %Y"], 

    def __str__(self):
        return self.name

class Person(models.Model):
    BLOOD_GROUPS = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('X', 'Unknown')
    )
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    STATUS = (
        ('found', 'Found'),
        ('missing', 'Missing'),
        ('identified', 'Identified')
    )
    name = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='static/images/persons',
                             default='static/dish/images/person.jpg',
                             max_length = 500,
                             blank=True)
    specific_characteristics = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    clothing = models.CharField(max_length=300)
    age_estimate = models.IntegerField()
    height = models.FloatField()
    alive = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS)
    blood_group = models.CharField(max_length=2, choices=BLOOD_GROUPS)
    gender = models.CharField(max_length=11, choices=GENDERS)
    disaster = models.ForeignKey(Disaster, on_delete = models.CASCADE, default=False)
