from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

class person(models.Model):
    User = settings.AUTH_USER_MODEL
    added_by = models.ForeignKey(User,
        null=True, blank=True, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20, null=True)
    lastname=models.CharField(max_length=20, null=True)
    profession=models.CharField(max_length=20, null=True)
    title=models.CharField(max_length=20, null=True)
    city=models.CharField(max_length=30, null=True)
    state=models.CharField(max_length=30, null=True)
    pincode=models.IntegerField( null=True)
    phoneno=models.IntegerField( null=True)
    emailid=models.EmailField( null=True)
    profile = models.TextField(max_length=100, null=True)
    
    def __str__(self):
        return self.firstname

class education(models.Model):
    added_by = models.ForeignKey(person,
        null=True, blank=True, on_delete=models.CASCADE)
    institute=models.CharField(max_length=40)
    startingyear=models.IntegerField()
    endingyear=models.IntegerField()
    grade=models.CharField(max_length=4)
    course=models.CharField(max_length=20)

    def __str__(self):
        return self.institute

class experience(models.Model):
    added_by = models.ForeignKey(person,
        null=True, blank=True, on_delete=models.CASCADE)
    company=models.CharField(max_length=40)
    startingyear=models.IntegerField()
    endingyear=models.IntegerField()
    post=models.CharField(max_length=20)
    details=models.TextField(max_length=200)

    def __str__(self):
        return self.company

class projects(models.Model):
    added_by = models.ForeignKey(person,
        null=True, blank=True, on_delete=models.CASCADE)
    topic=models.CharField(max_length=40)
    startingyear=models.IntegerField()
    endingyear=models.IntegerField()
    details=models.TextField(max_length=200)

    def __str__(self):
        return self.topic

class skill(models.Model):
    added_by = models.ForeignKey(person,
        null=True, blank=True, on_delete=models.CASCADE)
    skill1=models.CharField(max_length=40,blank=True)
    skill2 = models.CharField(max_length=40, blank=True)
    skill3=models.CharField(max_length=40,blank=True)

    def __str__(self):
        return self.skill1
class temp(models.Model):
    added_by = models.ForeignKey(person,
        null=True, blank=True, on_delete=models.CASCADE)
    temp_id = models.IntegerField(blank=True, null=True)
    

# class resume(models.Model):
#     resumename=models.CharField(max_length=40)
#     person=models.ForeignKey(person, on_delete=models.CASCADE)
#     education=models.ManyToManyField(education)
#     experience=models.ManyToManyField(experience)
#     project=models.ManyToManyField(projects)

#     def __str__(self):
#         return self.resumename




# Create your models here.
