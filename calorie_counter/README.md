1. Create a virtual environment
2. Activate the environment
3. After activation of environment run pip install -r requirements.txt
4. then traverse inside the folder where manage.py file is present
5. Then run python manage.py makemigrations and then python manage.py migrate
6. To load data run python manage.py shell and then run following commands in shell for loading data
   a) from calorie_app.views import \*
   b) seeding_data()

Your data will be loaded in Food and Workout Table

other way is to add data from admin panel
create a super user login from admin panel then add data in Food and Workout Table

7. now run python manage.py runserver

now you can run the website
