apt-get install python-pygraphviz
pip install django-extensions
# add 'django_extensions' to INSTALLED_APPS in settings.py
python manage.py graph_models trees -o test.png