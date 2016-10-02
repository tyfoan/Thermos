from flask import render_template

from . import main
from .. import login_manager
from ..models import User, Bookmark, Tag


@login_manager.user_loader
def load_user(userid):
	return User.query.get(int(userid))

@main.route('/')
def index():
	return render_template('index.html', new_bookmarks = Bookmark.newest(5))



@main.errorhandler(403)
def page_forbidden(e):
	return render_template('403.html'), 403


@main.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@main.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500


@main.context_processor # google this. practises.
def inject_tags():
	return dict(all_tags=Tag.all)