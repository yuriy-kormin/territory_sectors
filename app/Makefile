MANAGE := poetry run python3 manage.py

start:
	${MANAGE} runserver 127.0.0.1:8000
shell:
	${MANAGE} shell_plus --plain
migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate
collectstatic:
	${MANAGE} collectstatic --no-input --clear
test:
	${MANAGE} test --keepdb
install:
	poetry install --no-root
lint:
	poetry run flake8 territory_sectors --exclude migrations
coverage:
	poetry run python -m coverage run app/manage.py test --keepdb
translate:
	${MANAGE} makemessages --locale ru --ignore=venv
	${MANAGE} compilemessages --locale ru
