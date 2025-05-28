 dotenv -f .env.prod run -- python manage.py migrate
 
 dotenv -f .env.prod run -- python manage.py loaddata questions/fixtures/algebra_questions.json