import os
from datetime import datetime

from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from forms import BookmarkForm
import models



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#app.logger.debug(basedir)

bookmarks = []
app.config['SECRET_KEY'] = b"hNk)\xd0u\x95\x7fl\xf2\xa6\xbe\x03\xec\xcc'\xc9\x07\xc2,\x05\x0e\xef("
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

# def store_bookmark(url, description):
# 	bookmarks.append(dict(
# 		url = url,
# 		description = description,
# 		user = 'reindert',
# 		date = datetime.utcnow()
# 	))


#def new_bookmarks(num): //to bookmark model
	 # return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

# class User:
# 	"""docstring for User"""
# 	def __init__(self, firstname, lastname):
# 		self.firstname = firstname
# 		self.lastname = lastname

# 	def initials(self):
# 		return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', new_bookmarks = models.Bookmark.newest(5))#, title="Title passed from view to template")
										 #user=User('Alexander', 'Ogurtsov'))


@app.route('/add', methods=['GET', 'POST'])
def add():
	form = BookmarkForm()
	if form.validate_on_submit():
		url = form.url.data
		description = form.description.data
		bm = models. Bookmark(url=url, description=description)
		db.session.add(bm)
		db.session.commit()
		#store_bookmark(url, description)
	# if request.method == "POST":
		# url = request.form['url']
		# store_bookmark(url)
		# flash("stored url: '{}'".format(url))
		# app.logger.debug('Bookmarks: ' + str(bookmarks))		
		flash("Stored: '{}'".format(description))
		return redirect(url_for('index'))
	return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500


if __name__ == '__main__':
	app.run(debug=True)