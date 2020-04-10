echo "The running of app"
sleep 3
python manage.py migrate
python manage.py test
python manage.py loaddata api/fixtures/initial_data.xml
gunicorn point.wsgi:application --bind 0.0.0.0:8000