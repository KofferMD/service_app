git clone https://github.com/KofferMD/service_app.git
docker-compose build
docker-compose up
docker-compose run --rm web-app sh -c "./manage.py makemigrations"
docker-compose run --rm web-app sh -c "./manage.py migrate"
docker-compose up

api:
api/cats/ - все кошечки
api/cats/cats_booking/ - забронированные, если они есть
api/cats/cats_free/ - свободные
api/cats/{id} - посмотреть конкретного
пагинация есть, но там 10 стоит 



