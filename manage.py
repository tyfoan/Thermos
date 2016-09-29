from thermos import app, db
from thermos.models import User
from flask_script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
	db.create_all()
	db.session.add(User(username='reindert', email='reindert@example.com'))
	db.session.add(User(username='arjen', email='arjen@example.com'))
	db.session.commit()
	print('Initialized the database')


@manager.command
def dropdb():
	if prompt_bool("Are you sure you want to loose all your data?"):
		db.drop_all()
		print('Dropped the database')

if __name__ == '__main__':
	manager.run()
