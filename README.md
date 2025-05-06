Installation Steps
1. Clone the Repository
Start by cloning the project to your local machine:
git clone https://github.com/marufmonower/countries-project.git
cd country-project
2. Create a Virtual Environment
It is recommended to use a virtual environment to manage your dependencies:
# For Linux/MacOS
python3 -m venv venv

# For Windows
python -m venv venv
3. Activate the Virtual Environment
For Linux/MacOS:

source venv/bin/activate
For Windows:

venv\Scripts\activate
4. Install Required Dependencies
Install the project dependencies using pip:

pip install -r requirements.txt
________________________________________
Required Dependencies and Versions:

The following are the main dependencies used in this project:

a).	Django: 3.x or later
b).  djangorestframework: 3.x or later
c).	requests: 2.x or later
d).	psycopg2 (if using PostgreSQL database)
e).	gunicorn (for deployment)


Make sure your environment has these versions or install them from requirements.txt.
You can see all required dependencies listed in requirements.txt file.


________________________________________
Database Setup and Configuration
This project uses the SQLite database by default. If you want to use a different database (e.g., PostgreSQL), follow these steps:
1. Configure Database Settings
In settings.py, under DATABASES, update the database configuration:
For PostgreSQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'country_db',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
For SQLite (default):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

2. Apply Database Migrations
Once the database is set up, apply migrations to create the necessary tables:

python manage.py migrate
3. Create a Superuser
If you want to access the Django Admin, create a superuser:

python manage.py createsuperuser
Follow the prompts to set a username, email, and password.
________________________________________
Running the Application
1. Start the Development Server
To run the application locally, start the Django development server:

python manage.py runserver

This will start the server at http://127.0.0.1:8000/.

2. Access the Application
•	The country list page is accessible at http://127.0.0.1:8000/countries/.
•	The country details page is accessible at http://127.0.0.1:8000/countries/<country_id>/details/.
•	The login page is accessible at http://127.0.0.1:8000/accounts/login/.
•	The admin page is accessible at http://127.0.0.1:8000/admin/.

