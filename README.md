# flaskstarter
Loitd Flask Starter Template

# How to run
## Install VirtualEnvironment
	pip3 install virtualenvwrapper
	pip3 install virtualenvwrapper-win
### Create new virtualenvironment if not exist
	mkvirtualenv -p C:\Python36\python.exe rocket
### Show all virtual environments:
	lsvirtualenv
	rmvirtualenv rocket
	cpvirtualenv ENVNAME [TARGETENVNAME]
	allvirtualenv pip install -U pip
### Switch to new created environment
	workon rocket
### Save and reinstall the requirement
	(rocket)$ pip freeze > requirements.txt
	pip install -r requirements.txt
## Database Migration
### Alembic init
Alembic is a database migrations tool written by the author of SQLAlchemy.
We’ll create our alembic “migration environment” via the alembic init command.
	alembic init alembic
Editing the alembic.ini File
	sqlalchemy.url = postgresql://scott:tiger@localhost/test
### Create first revision
First we run alembic revision to generate a migration script.
	alembic revision -m "create account table"
	alembic revision
Then we’ll open up the newly generated Python file in `myapp/alembic/versions/` and fill in the `upgrade` and `downgrade` functions using the tools provided by Alembic’s `op` object. 
### Upgrade or downgrade using revisions
Once we have our migration script ready, we can run `alembic upgrade head` to migrade our data to the latest version.
	alembic upgrade head
Above, we use ae1 to refer to revision ae1027a6acf. Alembic will stop and let you know if more than one version starts with that prefix.
	alembic upgrade ae1
To move two versions from the current
	alembic upgrade +2
Negative values are accepted for downgrades:
	alembic downgrade -1
	alembic downgarde base
Relative identifiers may also be in terms of a specific revision. For example, to upgrade to revision ae1027a6acf plus two additional steps:
	alembic upgrade ae10+2
### Getting some information with Alembic
	alembic current -v
	alembic history -v
	alembic history -r1975ea:ae1027
### Cons
There's currently no command to delete migrations from your versions directory
