echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'p@ssw0rd')" | python manage.py shell