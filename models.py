from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import datetime
db = SQLAlchemy()

class Admin(db.Model):
	__tablename__ = 'admin'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(120), unique = True)
	pwdhash = db.Column(db.String(54))
	
	def __init__(self, username, pwdhash):
		self.username = username.lower()
		self.set_password(pwdhash)
	
	
	def set_password(self, pwdhash):
		self.pwdhash = generate_password_hash(pwdhash)
		
	def check_password(self, password):
		return check_password_hash(self.pwdhash, pwdhash)


class Blog(db.Model):
	__tablename__ = 'articles'
	id = db.Column(db.Integer, primary_key = True)
	main_topic = db.Column(db.String(255))
	topic_expl = db.Column(db.Text())
	blog_topic = db.Column(db.String(255))
	body = db.Column(db.Text())
	body2 = db.Column(db.Text())
	highlight = db.Column(db.Text())
	author_name = db.Column(db.String(255))
	author_expl = db.Column(db.Text())
	key_words = db.Column(db.String(255))
	#~ create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	def __init__(self, main_topic, topic_expl, blog_topic, body, body2, highlight, author_name, author_expl, key_words):
		
		self.main_topic = main_topic
		self.topic_expl = topic_expl
		self.blog_topic = blog_topic
		self.body = body
		self.body2 = body2
		self.highlight = highlight
		self.author_name = author_name
		self.author_expl = author_expl
		self.key_words = key_words
		