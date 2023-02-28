MANAGE := poetry run python3 manage.py

start:
	${MANAGE} runserver 127.0.0.1:8000
shell:
	${MANAGE} shell_plus --plain
migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate
collectstatic:
	poetry run python manage.py collectstatic --no-input --clear
test:
	${MANAGE} test
install:
	poetry install
lint:
	poetry run flake8 territory_sectors --exclude migrations
translate:
	${MANAGE} makemessages --locale ru
	${MANAGE} compilemessages --locale ru
