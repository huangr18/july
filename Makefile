build:
	# sh download_models.sh
	docker-compose build
up:
	docker-compose up
	nohup docker-compose logs --no-color > logs.txt &
restart:
	make build
	make up

down:
	docker-compose down
