shema:
	python manage.py spectacular --color --file schema.yml

run:
	python manage.py runserver
	
mm:
	python manage.py makemigrations

mi:
	python manage.py migrate