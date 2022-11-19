sleep 10

echo '>>> Do migrations'
python app/manage.py makemigrations
python app/manage.py migrate

echo '>>> Starting server'

python app/manage.py runserver 0.0.0.0:8000

echo '>>> Server started'

