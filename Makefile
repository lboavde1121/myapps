NAME=myapps

run:
	docker-compose build
	docker-compose up -d

dev:
	docker-compose build
	docker-compose up


stop:
	docker stop ${NAME}_uwsgi_1 ${NAME}_nginx_1
	docker rm ${NAME}_uwsgi_1 ${NAME}_nginx_1
