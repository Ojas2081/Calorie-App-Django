from django.shortcuts import render
from .models import *
from django.http import HttpResponse

    

# Create your views here.
def home(request):
    return render(request,"calorie_app/home.html")

def home_checker(request):
    if request.method == "POST":
        data_val = request.POST.get('calory')
        print(data_val)
        if data_val == 'food':
            food_list = Food.objects.all()
            context = {
                'food_list':food_list,
            }
            return render(request,"calorie_app/home_food.html",context)
        elif data_val == 'workout':
            workout_list = Workout.objects.all()
            context = {
                'workout_list':workout_list,
            }
            return render(request,"calorie_app/home_workout.html",context)

def home_food(request):
    food_list = Food.objects.all()
    context = {
        'food_list':food_list,
    }
    return render(request,"calorie_app/home_food.html",context)

def calorie_calc(request):
    if request.method == "POST":
        user_email = request.POST.get('usr_mail')
        calorie_list = request.POST.getlist('vegetables')
        type_calory = request.POST.get('type_calory')

        # print(calorie_list)
        # print(user_email)
        # print(type_calory)
        usr = UserDetails()
        usr.user_email = user_email
        usr.calory_type = type_calory
        sum_calorie = 0
        for calorie in calorie_list:
            sum_calorie += float(calorie)
        print(sum_calorie)
        usr.calorie = sum_calorie
        usr.save()
        consumed = True
        list1 = UserDetails.objects.filter(user_email = user_email)
        list2 = UserDetails.objects.filter(user_email = user_email,calory_type = type_calory)
        sum_cal = 0
        for obj in list2:
            sum_cal += obj.calorie
        context = {
            'total_calorie' : sum_cal,
            'consumed' : consumed,
            'list1' : list1,
        }
    return render(request,"calorie_app/calculate.html",context)

def calorie_calc_workout(request):
    if request.method == "POST":
        user_email = request.POST.get('usr_mail')
        calorie_list = request.POST.getlist('workout')
        type_calory = request.POST.get('type_calory')
        usr = UserDetails()
        usr.user_email = user_email
        usr.calory_type = type_calory

        # print(calorie_list)
        # print(user_email)
        # print(type_calory)
        sum_calorie = 0
        for calorie in calorie_list:
            sum_calorie += float(calorie)
        print(sum_calorie)
        usr.calorie = sum_calorie
        usr.save()
        consumed = False
        list1 = UserDetails.objects.filter(user_email = user_email)
        list2 = UserDetails.objects.filter(user_email = user_email,calory_type = type_calory)
        sum_cal = 0
        for obj in list2:
            sum_cal += obj.calorie
        
        context = {
            'total_calorie' : sum_cal,
            'consumed' : consumed,
            'list1' : list1,
        }
    return render(request,"calorie_app/calculate.html",context)

def seeding_data():
    import pandas as pd

    food_data = pd.read_csv("food_data.csv")
    workout_data = pd.read_csv("workout_data.csv")
    print("got file")
    from .models import Food, Workout


    for i in range(food_data.shape[0]):
        fd = Food()
        fd.food_name = food_data.loc[i, "food_name"]
        fd.calorie = food_data.loc[i, "calorie"]
        fd.save()


    for i in range(workout_data.shape[0]):
        wd = Workout()

        wd.workout_name = workout_data.loc[i, "workout_name"]
        wd.calorie = workout_data.loc[i, "calorie"]
        wd.save()

    