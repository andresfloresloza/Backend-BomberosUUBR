#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

mkdir -p /media
cp -r media/* /media/

echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='luisandresfloresloza@gmail.com').exists():
    User.objects.create_superuser('luisandresfloresloza@gmail.com', 'luisandresfloresloza@gmail.com', '76680886')
END
echo "Superuser created successfully!"