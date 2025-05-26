 dotenv -f .env.prod run -- python manage.py migrate
 dotenv -f .env.prod -- python manage.py loaddata questions/fixtures/sample_questions.json