ENV := qa
FILE_CONFIG := ./config/${ENV}.config
CONFIG :=$(shell cat $(FILE_CONFIG))
port = $(word 2,$(CONFIG))

.PHONY: build
.PHONY: run 

build:	
	port=${port} docker-compose -f ./build/docker-compose.yml build
	
run: 
	port=${port} docker-compose -f ./build/docker-compose.yml up 
	
stop: 		
	port=${port} docker-compose -f ./build/docker-compose.yml down 

show_db:
	docker exec -it psql \
	psql -U user db -c \
	'select * from "Song" ORDER BY "ID";' \
	-c '\d'
	
	

