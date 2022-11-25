.PHONY: run \
		shell \
		mdb \
		db \
		csu \


PIP_VERSION = 22.0.4


run: ./venv/bin/activate ## Local Run
	./venv/bin/activate; python blog_site/manage.py runserver

shell: ./venv/bin/activate ## Run django shell
	./venv/bin/activate; python blog_site/manage.py shell


mdb: ./venv/bin/activate ## Make migrations
	./venv/bin/activate; python blog_site/manage.py makemigrations


db: ./venv/bin/activate ## Migrate to database
	./venv/bin/activate; python blog_site/manage.py migrate

csu: ./venv/bin/activate ## Migrate to database
	./venv/bin/activate; python blog_site/manage.py createsuperuser