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
		
class Home(db.Model):
	__tablename__ = 'home'
	id = db.Column(db.Integer, primary_key = True)
	slide1_place = db.Column(db.String())
	slide1_discover = db.Column(db.String())
	slide1_title = db.Column(db.String())
	slide1_text = db.Column(db.Text())
	slide2_place = db.Column(db.String())
	slide2_discover = db.Column(db.String())
	slide2_title = db.Column(db.String())
	slide2_text = db.Column(db.Text())
	slide3_place = db.Column(db.String())
	slide3_discover = db.Column(db.String())
	slide3_title = db.Column(db.String())
	slide3_text = db.Column(db.Text())
	plan_motto = db.Column(db.String())
	plan_title = db.Column(db.String())
	plan_expl = db.Column(db.Text())
	travel_motto = db.Column(db.String())
	travel_title = db.Column(db.String())
	travel_expl = db.Column(db.Text())
	travel_city1 = db.Column(db.String())
	travel_place1 = db.Column(db.String())
	travel_expl1 = db.Column(db.Text())
	travel_city2 = db.Column(db.String())
	travel_place2 = db.Column(db.String())
	travel_expl2 = db.Column(db.Text())	
	travel_city3 = db.Column(db.String())
	travel_place3 = db.Column(db.String())
	travel_expl3 = db.Column(db.Text())	
	travel_city4 = db.Column(db.String())
	travel_place4 = db.Column(db.String())
	travel_expl4 = db.Column(db.Text())
	travel_city5 = db.Column(db.String())
	travel_place5 = db.Column(db.String())
	travel_expl5 = db.Column(db.Text())	
	travel_city6 = db.Column(db.String())
	travel_place6 = db.Column(db.String())
	travel_expl6 = db.Column(db.Text())	
	service_motto = db.Column(db.String())
	service_title = db.Column(db.String())
	service_expl = db.Column(db.Text())
	service_title1 = db.Column(db.String())
	service_expl1 = db.Column(db.Text())
	service_title2 = db.Column(db.String())
	service_expl2 = db.Column(db.Text())
	service_title3 = db.Column(db.String())
	service_expl3 = db.Column(db.Text())
	service_title4 = db.Column(db.String())
	service_expl4 = db.Column(db.Text())
	testimonia1_motto = db.Column(db.String())
	testimonia1_title = db.Column(db.String())
	testimonia1_expl1 = db.Column(db.Text())
	testimonia1_name1 = db.Column(db.String())
	testimonia1_position1 = db.Column(db.String())
	testimonia1_expl2 = db.Column(db.Text())
	testimonia1_name2 = db.Column(db.String())
	testimonia1_position2 = db.Column(db.String())
	testimonia1_expl3 = db.Column(db.Text())
	testimonia1_name3 = db.Column(db.String())
	testimonia1_position3 = db.Column(db.String())
	testimonia1_expl4 = db.Column(db.Text())
	testimonia1_name4 = db.Column(db.String())
	testimonia1_position4 = db.Column(db.String())
	testimonia1_expl5 = db.Column(db.Text())
	testimonia1_name5 = db.Column(db.String())
	testimonia1_position5 = db.Column(db.String())
	route_motto = db.Column(db.String())
	route_title = db.Column(db.String())
	route_expl = db.Column(db.Text())
	route_city1 = db.Column(db.String())
	route_place1 = db.Column(db.String())
	route_expl1 = db.Column(db.Text())
	route_city2 = db.Column(db.String())
	route_place2 = db.Column(db.String())
	route_expl2 = db.Column(db.Text())	
	route_city3 = db.Column(db.String())
	route_place3 = db.Column(db.String())
	route_expl3 = db.Column(db.Text())	
	blog_motto = db.Column(db.String())
	blog_title = db.Column(db.String())
	blog_expl = db.Column(db.Text())
	about_motto = db.Column(db.String())
	about_title = db.Column(db.String())
	about_expl = db.Column(db.Text())
	about_main_title = db.Column(db.String())
	about_main = db.Column(db.Text())
	#~ create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	def __init__(self,
	id,
	slide1_place,
	slide1_discover,
	slide1_title, 
	slide1_text,
	slide2_place, 
	slide2_discover, 
	slide2_title,
	slide2_text,
	slide3_place, 
	slide3_discover, 
	slide3_title,
	slide3_text,
	plan_motto,
	plan_title, 
	plan_expl,
	travel_motto, 
	travel_title,
	travel_expl,
	travel_city1, 
	travel_place1, 
	travel_expl1,
	travel_city2,
	travel_place2, 
	travel_expl2,	
	travel_city3,
	travel_place3, 
	travel_expl3,	
	travel_city4,
	travel_place4, 
	travel_expl4,
	travel_city5,
	travel_place5, 
	travel_expl5,	
	travel_city6,
	travel_place6, 
	travel_expl6,	
	service_motto,
	service_title,
	service_expl,
	service_title1, 
	service_expl1,
	service_title2, 
	service_expl2,
	service_title3, 
	service_expl3,
	service_title4, 
	service_expl4,
	testimonia1_motto, 
	testimonia1_title,
	testimonia1_expl1,
	testimonia1_name1,
	testimonia1_position1, 
	testimonia1_expl2,
	testimonia1_name2,
	testimonia1_position2, 
	testimonia1_expl3,
	testimonia1_name3,
	testimonia1_position3, 
	testimonia1_expl4,
	testimonia1_name4,
	testimonia1_position4, 
	testimonia1_expl5,
	testimonia1_name5,
	testimonia1_position5,
	route_motto,
	route_title,
	route_expl,
	route_city1,
	route_place1,
	route_expl1,
	route_city2,
	route_place2,
	route_expl2,
	route_city3,
	route_place3,
	route_expl3,
	blog_motto,
	blog_title,
	blog_expl,
	about_motto, 
	about_title,
	about_expl,
	about_main_title, 
	about_main):
		for i in [slide1_place,
	slide1_discover,
	slide1_title, 
	slide1_text,
	slide2_place, 
	slide2_discover, 
	slide2_title,
	slide2_text,
	slide3_place, 
	slide3_discover, 
	slide3_title,
	slide3_text,
	plan_motto,
	plan_title, 
	plan_expl,
	travel_motto, 
	travel_title,
	travel_expl,
	travel_city1, 
	travel_place1, 
	travel_expl1,
	travel_city2,
	travel_place2, 
	travel_expl2,	
	travel_city3,
	travel_place3, 
	travel_expl3,	
	travel_city4,
	travel_place4, 
	travel_expl4,
	travel_city5,
	travel_place5, 
	travel_expl5,	
	travel_city6,
	travel_place6, 
	travel_expl6,	
	service_motto,
	service_title,
	service_expl,
	service_title1, 
	service_expl1,
	service_title2, 
	service_expl2,
	service_title3, 
	service_expl3,
	service_title4, 
	service_expl4,
	testimonia1_motto, 
	testimonia1_title,
	testimonia1_expl1,
	testimonia1_name1,
	testimonia1_position1, 
	testimonia1_expl2,
	testimonia1_name2,
	testimonia1_position2, 
	testimonia1_expl3,
	testimonia1_name3,
	testimonia1_position3, 
	testimonia1_expl4,
	testimonia1_name4,
	testimonia1_position4, 
	testimonia1_expl5,
	testimonia1_name5,
	testimonia1_position5,
	route_motto,
	route_title,
	route_expl,
	route_city1,
	route_place1,
	route_expl1,
	route_city2,
	route_place2,
	route_expl2,
	route_city3,
	route_place3,
	route_expl3,
	blog_motto,
	blog_title,
	blog_expl,
	about_motto, 
	about_title,
	about_expl,
	about_main_title, 
	about_main]:
		
			self.i = i
		
		





		

class services(db.Model):
	__tablename__ = 'services'
	id = db.Column(db.Integer, primary_key = True)
	guide = db.Column(db.Text())
	hotel = db.Column(db.Text())
	transportation = db.Column(db.Text())
	insurance = db.Column(db.Text())
	flight = db.Column(db.Text())
	visa = db.Column(db.Text())
	

	#~ create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	def __init__(self, guide, hotel, transportation, insurance, flight, visa):
		
		self.guide = guide
		self.hotel = hotel
		self.transportation = transportation
		self.insurance = insurance
		self.flight = flight
		self.visa = visa
		

class tours(db.Model):
	__tablename__ = 'tours'
	id = db.Column(db.Integer, primary_key = True)
	paragraph_title = db.Column(db.String())
	paragraph = db.Column(db.Text())

	

	#~ create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	def __init__(self, paragraph_title, paragraph):
		
		self.paragraph_title = paragraph_title
		self.paragraph = paragraph



		