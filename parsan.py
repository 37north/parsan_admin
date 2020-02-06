from flask import Flask, url_for, redirect, render_template, request, session, flash, logging
from models import db, Admin, Blog, services, tours, Home
from flask_sqlalchemy import SQLAlchemy
from forms import adminForm, blogForm, servicesForm, toursForm, homeForm
from werkzeug import generate_password_hash, check_password_hash
from data import Articles
import os
Articles = Articles()

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/parsan'
db.init_app(app)
app.secret_key = "development-key"


@app.route('/index')
def index():
	return render_template('index1.html')
	
	
@app.route('/admin')
def admin():
	if 'username' not in session:

		
		return redirect(url_for('adminLogin'))
		
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from articles')
		blog=rs.fetchall()

	return render_template('admin.html', blog=blog)
	
	
	
@app.route('/adminLogin', methods = ['GET', 'POST'])
def adminLogin():
	form = adminForm()
	if request.method =='POST' and form.validate() == False:
		return render_template('adminLogin.html', form = form)


	elif request.method =='POST' and form.validate() == True:
		if request.form['username'] == 'parsan' and  check_password_hash(generate_password_hash('parsa'), form.pwdhash.data):
			app.config['SQLALCHEMY_DATABASE_URI']
			newlogin = Admin(form.username.data, form.pwdhash.data)
			db.session.add(newlogin)
			db.session.commit()
			session['username'] = form.username.data
			
			
			return redirect(url_for('admin'))
		else:
			return render_template('adminLogin.html', form = form)
			
	elif 'username' in session:
		return redirect(url_for('admin'))
			
	elif request.method =='GET':
		return render_template('adminLogin.html', form = form)
	
	
@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))
	
@app.route('/add_blog', methods=['GET','POST'])
def addBlog():
	if 'username' not in session:
		return redirect(url_for('adminLogin'))
	form = blogForm(request.form)
	if request.method =='POST' and form.validate():
		#~ title = form.title.data
		#~ body = form.body.data
		#~ author = session['username']
		
		main_topic = form.main_topic.data
		topic_expl = form.topic_expl.data
		blog_topic = form.blog_topic.data
		body = form.body.data
		body2 = form.body2.data
		highlight = form.highlight.data
		author_name = form.author_name.data
		author_expl = form.author_expl.data
		key_words = form.key_words.data
		
		
		
		
		app.config['SQLALCHEMY_DATABASE_URI']
		newBlog = Blog(main_topic, topic_expl, blog_topic, body, body2, highlight, author_name, author_expl, key_words)
		db.session.add(newBlog)
		db.session.commit()
		#~ flash('hhhhhhh', 'success')
		#~ session['username'] = form.username.data
		return redirect(url_for('admin'))
	return render_template('add_blog.html', form = form)
		
@app.route('/edit_blog<string:id>', methods=['GET','POST'])
def editBlog(id):
	form = blogForm(request.form)
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from articles where id=%s' , [id])
		blogid=rs.fetchone()
	
	#populate blog form fields
	form.main_topic.data = blogid['main_topic']
	form.topic_expl.data =  blogid['topic_expl']
	form.blog_topic.data=  blogid['blog_topic']
	form.body.data=  blogid['body']
	form.body2.data=  blogid['body2']
	form.highlight.data=  blogid['highlight']
	form.author_name.data=  blogid['author_name']
	form.author_expl.data=  blogid['author_expl']
	form.key_words.data=  blogid['key_words']
	
	if request.method =='POST' and form.validate():

		#~ title = form.title.data
		#~ body = form.body.data
		#~ author = session['username']

		main_topic= request.form['main_topic']
		topic_expl = request.form['topic_expl']
		blog_topic = request.form['blog_topic']
		body = request.form['body']
		body2 = request.form['body2']
		highlight = request.form['highlight']
		author_name = request.form['author_name']
		author_expl = request.form['author_expl']
		key_words = request.form['key_words']
		

		#~ app.config['SQLALCHEMY_DATABASE_URI']
		#~ newBlog = Blog(main_topic, topic_expl, blog_topic, body, body2, highlight, author_name, author_expl, key_words)
		#~ db.session.add(newBlog)
		#~ db.session.commit()
		
		with db.engine.connect() as con:
			con.execute('update articles set main_topic=%s, topic_expl=%s, blog_topic=%s, body=%s, body2=%s, highlight=%s, author_name=%s, author_expl=%s, key_words=%s where id=%s' , [main_topic, topic_expl, blog_topic, body, body2, highlight, 
author_name, author_expl, key_words, id])
			con.close()
		return redirect(url_for('admin'))

	return render_template('edit_blog.html', form = form)





@app.route('/edit_services', methods=['GET','POST'])
def editServices():
	if 'username' not in session:
		return redirect(url_for('adminLogin'))
	
	form = servicesForm(request.form)
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from services where id=1')
		service=rs.fetchone()
	
	#populate blog form fields
	#~ try:
	form.guide.data = service['guide']
	form.hotel.data =  service['hotel']
	form.transportation.data=  service['transportation']
	form.insurance.data=  service['insurance']
	form.flight.data=  service['flight']
	form.visa.data=  service['visa']
	#~ except:
		#~ pass

	
	if request.method =='POST' and form.validate():
		guide = request.form['guide']
		hotel = request.form['hotel']
		transportation = request.form['transportation']
		insurance = request.form['insurance']
		flight = request.form['flight']
		visa = request.form['visa']

	
		form.guide.data = guide
		form.hotel.data =  hotel
		form.transportation.data=  transportation
		form.insurance.data=  insurance
		form.flight.data=  flight
		form.visa.data=  visa		
		
		with db.engine.connect() as con:
			con.execute('update services set guide=%s, hotel=%s, transportation=%s, insurance=%s, flight=%s, visa=%s where id=1' , [guide, hotel, transportation, insurance, flight, visa])
			con.close()
		return render_template('edit_services.html', form = form)


	return render_template('edit_services.html', form = form)



@app.route('/edit_home', methods=['GET','POST'])
def editHome():
	if 'username' not in session:
		return redirect(url_for('adminLogin'))
	
	form = homeForm(request.form)
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from home where id=3')
		home=rs.fetchone()



	form.slide1_place.data = home['slide1_place']
	form.slide1_discover.data = home['slide1_discover']
	form.slide1_title.data = home['slide1_title']
	form.slide1_text.data = home['slide1_text']
	form.slide2_place.data = home['slide2_place']
	form.slide2_discover.data = home['slide2_discover']
	form.slide2_title.data = home['slide2_title']
	form.slide2_text.data = home['slide2_text']
	form.slide3_place.data = home['slide3_place']
	form.slide3_discover.data = home['slide3_discover']
	form.slide3_title.data = home['slide3_title']
	form.slide3_text.data = home['slide3_text']
	form.plan_motto.data = home['plan_motto']
	form.plan_title.data = home['plan_title']
	form.plan_expl.data = home['plan_expl']
	form.travel_motto.data = home['travel_motto']
	form.travel_title.data = home['travel_title']
	form.travel_expl.data = home['travel_expl']
	form.travel_city1.data = home['travel_city1']
	form.travel_place1.data = home['travel_place1']
	form.travel_expl1.data = home['travel_expl1']
	form.travel_city2.data = home['travel_city2']
	form.travel_place2.data = home['travel_place2']
	form.travel_expl2.data = home['travel_expl2']
	form.travel_city3.data = home['travel_city3']
	form.travel_place3.data = home['travel_place3']
	form.travel_expl3.data = home['travel_expl3']
	form.travel_city4.data = home['travel_city4']
	form.travel_place4.data = home['travel_place4']
	form.travel_expl4.data = home['travel_expl4']
	form.travel_city5.data = home['travel_city5']
	form.travel_place5.data = home['travel_place5']
	form.travel_expl5.data = home['travel_expl5']
	form.travel_city6.data = home['travel_city6']
	form.travel_place6.data = home['travel_place6']
	form.travel_expl6.data = home['travel_expl6']
	form.service_motto.data = home['service_motto']
	form.service_title.data = home['service_title']
	form.service_expl.data = home['service_expl']
	form.service_title1.data = home['service_title1']
	form.service_expl1.data = home['service_expl1']
	form.service_title2.data = home['service_title2']
	form.service_expl2.data = home['service_expl2']
	form.service_title3.data = home['service_title3']
	form.service_expl3.data = home['service_expl3']
	form.service_title4.data = home['service_title4']
	form.service_expl4.data = home['service_expl4']
	form.testimonia1_motto.data = home['testimonia1_motto']
	form.testimonia1_title.data = home['testimonia1_title']
	form.testimonia1_expl1.data = home['testimonia1_expl1']
	form.testimonia1_name1.data = home['testimonia1_name1']
	form.testimonia1_position1.data = home['testimonia1_position1']
	form.testimonia1_expl2.data = home['testimonia1_expl2']
	form.testimonia1_name2.data = home['testimonia1_name2']
	form.testimonia1_position2.data = home['testimonia1_position2']
	form.testimonia1_expl3.data = home['testimonia1_expl3']
	form.testimonia1_name3.data = home['testimonia1_name3']
	form.testimonia1_position3.data = home['testimonia1_position3']
	form.testimonia1_expl4.data = home['testimonia1_expl4']
	form.testimonia1_name4.data = home['testimonia1_name4']
	form.testimonia1_position4.data = home['testimonia1_position4']
	form.testimonia1_expl5.data = home['testimonia1_expl5']
	form.testimonia1_name5.data = home['testimonia1_name5']
	form.testimonia1_position5.data = home['testimonia1_position5']
	form.blog_motto.data = home['blog_motto']
	form.blog_title.data = home['blog_title']
	form.blog_expl.data = home['blog_expl']
	form.about_motto.data = home['about_motto']
	form.about_title.data = home['about_title']
	form.about_expl.data = home['about_expl']
	form.about_main_title.data = home['about_main_title']
	form.about_main.data = home['about_main']

	
	if request.method =='POST' and form.validate():
		slide1_place = request.form["slide1_place"] 
		slide1_discover = request.form["slide1_discover"] 
		slide1_title = request.form["slide1_title"] 
		slide1_text = request.form["slide1_text"] 
		slide2_place = request.form["slide2_place"] 
		slide2_discover = request.form["slide2_discover"] 
		slide2_title = request.form["slide2_title"] 
		slide2_text = request.form["slide2_text"] 
		slide3_place = request.form["slide3_place"] 
		slide3_discover = request.form["slide3_discover"] 
		slide3_title = request.form["slide3_title"] 
		slide3_text = request.form["slide3_text"] 
		plan_motto = request.form["plan_motto"] 
		plan_title = request.form["plan_title"] 
		plan_expl = request.form["plan_expl"] 
		travel_motto = request.form["travel_motto"] 
		travel_title = request.form["travel_title"] 
		travel_expl = request.form["travel_expl"] 
		travel_city1 = request.form["travel_city1"] 
		travel_place1 = request.form["travel_place1"] 
		travel_expl1 = request.form["travel_expl1"] 
		travel_city2 = request.form["travel_city2"] 
		travel_place2 = request.form["travel_place2"] 
		travel_expl2 = request.form["travel_expl2"] 
		travel_city3 = request.form["travel_city3"] 
		travel_place3 = request.form["travel_place3"] 
		travel_expl3 = request.form["travel_expl3"] 
		travel_city4 = request.form["travel_city4"] 
		travel_place4 = request.form["travel_place4"] 
		travel_expl4 = request.form["travel_expl4"] 
		travel_city5 = request.form["travel_city5"] 
		travel_place5 = request.form["travel_place5"] 
		travel_expl5 = request.form["travel_expl5"] 
		travel_city6 = request.form["travel_city6"] 
		travel_place6 = request.form["travel_place6"] 
		travel_expl6 = request.form["travel_expl6"] 
		service_motto = request.form["service_motto"] 
		service_title = request.form["service_title"] 
		service_expl = request.form["service_expl"] 
		service_title1 = request.form["service_title1"] 
		service_expl1 = request.form["service_expl1"] 
		service_title2 = request.form["service_title2"] 
		service_expl2 = request.form["service_expl2"] 
		service_title3 = request.form["service_title3"] 
		service_expl3 = request.form["service_expl3"] 
		service_title4 = request.form["service_title4"] 
		service_expl4 = request.form["service_expl4"] 
		testimonia1_motto = request.form["testimonia1_motto"] 
		testimonia1_title = request.form["testimonia1_title"] 
		testimonia1_expl1 = request.form["testimonia1_expl1"] 
		testimonia1_name1 = request.form["testimonia1_name1"] 
		testimonia1_position1 = request.form["testimonia1_position1"] 
		testimonia1_expl2 = request.form["testimonia1_expl2"] 
		testimonia1_name2 = request.form["testimonia1_name2"] 
		testimonia1_position2 = request.form["testimonia1_position2"] 
		testimonia1_expl3 = request.form["testimonia1_expl3"] 
		testimonia1_name3 = request.form["testimonia1_name3"] 
		testimonia1_position3 = request.form["testimonia1_position3"] 
		testimonia1_expl4 = request.form["testimonia1_expl4"] 
		testimonia1_name4 = request.form["testimonia1_name4"] 
		testimonia1_position4 = request.form["testimonia1_position4"] 
		testimonia1_expl5 = request.form["testimonia1_expl5"] 
		testimonia1_name5 = request.form["testimonia1_name5"] 
		testimonia1_position5 = request.form["testimonia1_position5"] 
		blog_motto = request.form["blog_motto"] 
		blog_title = request.form["blog_title"] 
		blog_expl = request.form["blog_expl"] 
		about_motto = request.form["about_motto"] 
		about_title = request.form["about_title"] 
		about_expl = request.form["about_expl"] 
		about_main_title = request.form["about_main_title"] 
		about_main = request.form["about_main"] 
					
		form.slide1_place.data = slide1_place 
		form.slide1_discover.data = slide1_discover 
		form.slide1_title.data = slide1_title 
		form.slide1_text.data = slide1_text 
		form.slide2_place.data = slide2_place 
		form.slide2_discover.data = slide2_discover 
		form.slide2_title.data = slide2_title 
		form.slide2_text.data = slide2_text 
		form.slide3_place.data = slide3_place 
		form.slide3_discover.data = slide3_discover 
		form.slide3_title.data = slide3_title 
		form.slide3_text.data = slide3_text 
		form.plan_motto.data = plan_motto 
		form.plan_title.data = plan_title 
		form.plan_expl.data = plan_expl 
		form.travel_motto.data = travel_motto 
		form.travel_title.data = travel_title 
		form.travel_expl.data = travel_expl 
		form.travel_city1.data = travel_city1 
		form.travel_place1.data = travel_place1 
		form.travel_expl1.data = travel_expl1 
		form.travel_city2.data = travel_city2 
		form.travel_place2.data = travel_place2 
		form.travel_expl2.data = travel_expl2 
		form.travel_city3.data = travel_city3 
		form.travel_place3.data = travel_place3 
		form.travel_expl3.data = travel_expl3 
		form.travel_city4.data = travel_city4 
		form.travel_place4.data = travel_place4 
		form.travel_expl4.data = travel_expl4 
		form.travel_city5.data = travel_city5 
		form.travel_place5.data = travel_place5 
		form.travel_expl5.data = travel_expl5 
		form.travel_city6.data = travel_city6 
		form.travel_place6.data = travel_place6 
		form.travel_expl6.data = travel_expl6 
		form.service_motto.data = service_motto 
		form.service_title.data = service_title 
		form.service_expl.data = service_expl 
		form.service_title1.data = service_title1 
		form.service_expl1.data = service_expl1 
		form.service_title2.data = service_title2 
		form.service_expl2.data = service_expl2 
		form.service_title3.data = service_title3 
		form.service_expl3.data = service_expl3 
		form.service_title4.data = service_title4 
		form.service_expl4.data = service_expl4 
		form.testimonia1_motto.data = testimonia1_motto 
		form.testimonia1_title.data = testimonia1_title 
		form.testimonia1_expl1.data = testimonia1_expl1 
		form.testimonia1_name1.data = testimonia1_name1 
		form.testimonia1_position1.data = testimonia1_position1 
		form.testimonia1_expl2.data = testimonia1_expl2 
		form.testimonia1_name2.data = testimonia1_name2 
		form.testimonia1_position2.data = testimonia1_position2 
		form.testimonia1_expl3.data = testimonia1_expl3 
		form.testimonia1_name3.data = testimonia1_name3 
		form.testimonia1_position3.data = testimonia1_position3 
		form.testimonia1_expl4.data = testimonia1_expl4 
		form.testimonia1_name4.data = testimonia1_name4 
		form.testimonia1_position4.data = testimonia1_position4 
		form.testimonia1_expl5.data = testimonia1_expl5 
		form.testimonia1_name5.data = testimonia1_name5 
		form.testimonia1_position5.data = testimonia1_position5 
		form.blog_motto.data = blog_motto 
		form.blog_title.data = blog_title 
		form.blog_expl.data = blog_expl 
		form.about_motto.data = about_motto 
		form.about_title.data = about_title 
		form.about_expl.data = about_expl 
		form.about_main_title.data = about_main_title 
		form.about_main.data = about_main 		
		
		with db.engine.connect() as con:
			con.execute('update home set '
					     'slide1_place = %s,'
	'slide1_discover = %s,'
	'slide1_title =%s,'
	'slide1_text = %s,'
	'slide2_place = %s,'
	'slide2_discover = %s,'
	'slide2_title = %s,'
	'slide2_text = %s,'
	'slide3_place = %s,'
	'slide3_discover = %s,'
	'slide3_title = %s,'
	'slide3_text = %s,'
	'plan_motto = %s,'
	'plan_title = %s,'
	'plan_expl = %s,'
	'travel_motto = %s,'
	'travel_title = %s,'
	'travel_expl = %s,'
	'travel_city1  = %s,'
	'travel_place1  = %s,'
	'travel_expl1 = %s,'
	'travel_city2 = %s,'
	'travel_place2 = %s,'
	'travel_expl2 = %s,'
	'travel_city3 = %s,'
	'travel_place3 = %s,'
	'travel_expl3 = %s,'
	'travel_city4 = %s,'
	'travel_place4 = %s,'
	'travel_expl4 = %s,'
	'travel_city5 = %s,'
	'travel_place5 = %s,'
	'travel_expl5 = %s,'
	'travel_city6 = %s,'
	'travel_place6 = %s,'
	'travel_expl6 = %s,'
	'service_motto = %s,'
	'service_title = %s,'
	'service_expl = %s,'
	'service_title1 = %s,'
	'service_expl1 = %s,'
	'service_title2 = %s,'
	'service_expl2 = %s,'
	'service_title3 = %s,'
	'service_expl3 = %s,'
	'service_title4 = %s,'
	'service_expl4 = %s,'
	'testimonia1_motto = %s,'
	'testimonia1_title = %s,'
	'testimonia1_expl1 = %s,'
	'testimonia1_name1 = %s,'
	'testimonia1_position1 = %s,'
	'testimonia1_expl2 = %s,'
	'testimonia1_name2 = %s,'
	'testimonia1_position2 = %s,'
	'testimonia1_expl3 = %s,'
	'testimonia1_name3 = %s,'
	'testimonia1_position3 = %s,'
	'testimonia1_expl4 = %s,'
	'testimonia1_name4 = %s,'
	'testimonia1_position4 = %s,'
	'testimonia1_expl5 = %s,'
	'testimonia1_name5 = %s,'
	'testimonia1_position5 = %s,'
	'blog_motto = %s,'
	'blog_title = %s,'
	'blog_expl = %s,'
	'about_motto = %s,'
	'about_title = %s,'
	'about_expl = %s,'
	'about_main_title = %s,'
	'about_main = %s'
	'where id=3' ,  [slide1_place,
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
	blog_motto,
	blog_title,
	blog_expl,
	about_motto, 
	about_title,
	about_expl,
	about_main_title, 
	about_main])
			con.close()
		return render_template('edit_home.html', form = form)


	return render_template('edit_home.html', form = form)




@app.route('/edit_tours', methods=['GET','POST'])
def editTours():
	if 'username' not in session:
		return redirect(url_for('adminLogin'))
	
	
	form = toursForm(request.form)
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from tours where id=1')
		tour=rs.fetchone()
	
	#populate blog form fields
	#~ try:
	form.paragraph_title.data = tour['paragraph_title']
	form.paragraph.data =  tour['paragraph']
	#~ except:
		#~ pass

	
	if request.method =='POST' and form.validate():
		paragraph_title = request.form['paragraph_title']
		paragraph = request.form['paragraph']

	
		form.paragraph_title.data = paragraph_title
		form.paragraph.data =  paragraph
	
		
		with db.engine.connect() as con:
			con.execute('update tours set paragraph_title=%s, paragraph=%s  where id=1' , [paragraph_title, paragraph])
			con.close()
		return render_template('edit_tours.html', form = form)


	return render_template('edit_tours.html', form = form)








@app.route('/delete_blog<string:id>', methods=['POST'])
def delete_blog(id):
	with db.engine.connect() as con:
		con.execute('delete from articles where id=%s' , [id])
	return redirect(url_for('admin'))

app.config["IMAGE_UPLOADS"]= "/media/dina-tech/D0CAAF7ACAAF5C0A/IT/parsan/parsan_v26/static/photo"
			
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if 'username' not in session:
		return redirect(url_for('adminLogin'))
	
	photo_name = ['1_Tour_Culture.jpg',
	'2_Eco_Tours.jpg',
	'3_Wellness_Tours.jpg',
	'4_Services1.jpg',
	'5_Services2.jpg',
	'6_Services3.jpg',
	'7_About_Parsan.jpg',
	'8_Travel1.jpg',
	'9_Travel2.jpg',
	'10_Travel3.jpg',
	'11_Travel4.jpg',
	'12_Travel5.jpg',
	'13_Travel6.jpg',
	'14_Person1.jpg',
	'15_Person2.jpg',
	'16_Person3.jpg',
	'17_Person4.jpg',
	'18_Person5.jpg',
	'19_Route1.jpg',
	'20_Route2.jpg',
	'21_Route3.jpg',
	'22_Blog1.jpg',
	'23_Blog2.jpg',
	'24_Blog3.jpg',
	'25_About_Us.jpg',
	'26_ONE.jpg',
	'27_HOLIDAY.jpg',
	'28_A.jpg',
	'29_MILLION.jpg',
	'30_SMILES.jpg',
	'88_Slider1.jpg',
	'89_Slider2.jpg',
	'90_Slider3.jpg',
	'31_Tours_Banner.jpg',
	'32_Tours1.jpg',
	'33_Tours2.jpg',
	'34_Tours3.jpg',
	'35_Tours4.jpg',
	'36_Tours5.jpg',
	'37_Tours6.jpg',
	'37_Services_Banner.jpg',
	'38_Guide.jpg',
	'39_Hotel.jpg',
	'40_Transporatation.jpg',
	'41_Insurance.jpg',
	'42_Flight.jpg',
	'43_Visa.jpg',
	'44_Tour11_Banner.jpg'
	]
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from articles')
		blog=rs.fetchall()
		for i in blog:
			photo_name.append(str(i.id)+i.main_topic.split()[0]+'.jpg')
			photo_name.append(str(i.id)+i.blog_topic.split()[0]+'.jpg')
	if request.method == "POST":
		if request.files:
			n=0
			for i in photo_name:
				try:
					n+=1
					image = request.files["image"+str(n)]
					image.save(os.path.join(app.config["IMAGE_UPLOADS"], i))
				except:
					try:
						image1 = request.files[i.split()[0]]
						image1.save(os.path.join(app.config["IMAGE_UPLOADS"], i))
					except:
						pass
						

				else:
					pass
					

			
			
			return redirect(request.url)

	return render_template('upload.html', photo_name=photo_name, blog=blog)
	


@app.route("/")
def home():
	with db.engine.connect() as con:
		rs = con.execute('select * from home where id=3')
		home=rs.fetchone()
	return render_template("index.html", home = home)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact1")
def contact1():
    return render_template("contact1.html")



@app.route("/tour11")
def tour11():
    return render_template("tour11.html")
  
@app.route("/tours1")
def tours1():
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from tours where id=1')
		tour=rs.fetchone()
	return render_template("tours1.html", tour = tour)


@app.route("/grand_tour")
def grand_tour():
    return render_template("grand_tour.html")
    
    
@app.route("/tour8")
def tour8():
    return render_template("tour8.html")
    
    
@app.route("/hotels")
def hotels():
    return render_template("hotels.html")

#~ @app.route("/services")
#~ def services():
    #~ return render_template("services.html")

@app.route("/services1")
def services1():
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from services where id=1')
		service=rs.fetchone()
		    
	return render_template("services1.html", service = service)

@app.route("/Abbasi")
def Abbasi():
    return render_template("Abbasi.html")
    
@app.route("/blog<string:id>")
def blog(id):
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from articles where id=%s' , [id])
		blog=rs.fetchone()
		print(blog)
	return render_template("blog_id.html", blog=blog)

@app.route("/imap")
def imap():
    return render_template("imap.html")
    
if __name__ == "__main__":
    app.run(debug='True', port='4000')