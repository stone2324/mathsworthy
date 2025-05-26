 dotenv -e .env -- python manage.py migrate
 dotenv -e .env -- python manage.py loaddata questions/fixtures/sample_questions.json