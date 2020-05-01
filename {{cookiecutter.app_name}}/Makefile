dockerCommand=docker-compose -f docker-compose.yml

.PHONY: build up down bash

# Container utility
build:
	$(dockerCommand) build

up:
	$(dockerCommand) up

down:
	$(dockerCommand) down

bash:
	$(dockerCommand) exec web bash
