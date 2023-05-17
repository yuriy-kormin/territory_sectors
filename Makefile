build:
	docker-compose build --parallel
up:
	docker-compose up -d
logs:
	docker-compose logs
down:
	docker-compose down --remove-orphans
clean:
	docker image prune -a

APP_DIR := app
TARGET := $(MAKECMDGOALS)

include $(APP_DIR)/Makefile

.PHONY: $(TARGET)
$(TARGET):
	cd $(APP_DIR) && $(MAKE) $(TARGET)
	@true