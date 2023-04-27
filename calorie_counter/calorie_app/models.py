from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length = 200 ,null=True,blank=True)
    calorie = models.FloatField(null=True,blank=True)

class Workout(models.Model):
    workout_name = models.CharField(max_length = 200 ,null=True,blank=True)
    calorie = models.FloatField(null=True,blank=True)

class UserDetails(models.Model):
    user_email = models.CharField(max_length = 250, null = True,blank=True)
    calory_type = models.CharField(max_length = 50, null = True,blank=True)
    calorie = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True,null = True,blank = True)
    updated_at = models.DateTimeField(auto_now = True,null = True,blank = True)
