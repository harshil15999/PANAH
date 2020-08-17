from django.db import models

# Create your models here.
#i will be creating the models/schema of my table hers
#you can rfer to them at this link 
"""
1.Users
2.Volunterer profile
3.Schemes
4.Scheme Description
5.people in scheme

"""
class Users(models.Model):
    user_id=mdels.PositiveIntegerField(unique=True,primary_key=True)
    fname=models.CharField(max_length=20,db_column='firstname')
    lastname=models.CharField(max_length=20,db_column='lastname')
    age=models.PositiveIntegerField(null=False,db_column='age')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, 
            blank=True,db_column='Number')
    
    date_registered=models.DateTimeField()

    YEAR_IN_SCHOOL_CHOICES = [
        ('N','None'),
        ('FR', 'Freshman'),
        ('SOR', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='N',
    )
    GENDER_CHOICES = [
        ('M','Male')
        ('F', 'Female'),
        ('N', 'None'),
    ]
    GENDER = models.CharField(
        choices=GENDER_CHOICES,
        blank=False,
    )
    email=models.EmailField(black=True,db_column='email')
    is_valid=models.BooleanField(blank=False)
    

class Volunteer_profile(models.Model):   
    volunteer_id=models.PositiveIntegerField(unique=True,primary_key=True)
    fname=models.CharField(max_length=20,db_column='firstname')
    lastname=models.CharField(max_length=20,db_column='lastname')
    age=models.PositiveIntegerField(null=False,db_column='age')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, 
            blank=True,db_column='Number')
    
    date_registered=models.DateTimeField()

    YEAR_IN_SCHOOL_CHOICES = [
        ('N','None')
        ('FR', 'Freshman'),
        ('SOR', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='N',
    )
    GENDER_CHOICES = [
        ('M','Male')
        ('F', 'Female'),
        ('N', 'None'),
    ]
    GENDER = models.CharField(
        choices=GENDER_CHOICES,
        blank=False,
        error_messages='Gender not provided'
    )
    email=models.EmailField(blank=False,db_column='email')


class Schemes(models.Model):
    scheme=models.CharField(db_columns='Name',blank=False)
    scheme_id=models.PositiveIntegerField(db_columns='id',blank=False,unique=True
                                          primary_keys=True)
    url=models.URLField(unique=True,blank=True,db_columns='website')
    scheme_description=models.CharField(max_length=500)

class Scheme_Parameters(models.Model):
    scheme_id = models.ForeignKey(Schemes, on_delete=models.CASCADE)
    age=models.PositiveIntegerField(db_columns='age')
    city = models.CharField(max_length=50)
    GENDER_CHOICES = [
        ('M','Male')
        ('F', 'Female'),
        ('B', 'Both'),
    ]
    GENDER = models.CharField(
        choices=GENDER_CHOICES,
        blank=False,
        default='B'
    )
    no_of_parameters=models.PositiveIntegerField(db_column='Parameters',blank=False)
    
class people_in_scheme(models.Model):
    user_id=models.ForeignKey(to=user_id,on_delete=models.DO_NOTHING)
    scheme_id=models.ForeignKey(to=Schemes,on_delete=models.CASCADE)
    volunteer_id=models.ForeignKey(to=Volunteer_profile,on_delete=models.SET_NULL)
    

    
    

