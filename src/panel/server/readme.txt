made using flask MAYBE node maybe django.

todo:
    CRUD operations

	map domain to specific project <--------------------------- []

	start / stop php server <---------------------------------- []
	start / stop mysql db <------------------------------------ []

    show project list from http_server file path <------------- []
	show domain attached to the project <---------------------- []

	settings: 
		project_name <----------------------------------------- []
		php version <------------------------------------------ []
		domain mapped <---------------------------------------- []
		database used <---------------------------------------- []
		
	 
    dns server: starts automatically <------------------------- []


windows
python -m venv venv

.\venv\Scripts\activate

mac or linux
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

//#region for starting django
    django-admin startproject <project_name> .

    python manage.py startapp <name_of_app>
//#endregion


// when running project
    python manage.py runserver

// when a change to the models been made
    python manage.py makemigrations
    python manage.py migrate

<!-- to add static files atttach after urls list -->
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)