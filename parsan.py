from flask import Flask, url_for, redirect, render_template, request, session, flash, logging
from models import db, Admin, Blog
from flask_sqlalchemy import SQLAlchemy
from forms import adminForm, blogForm
from werkzeug import generate_password_hash, check_password_hash
from data import Articles

Articles = Articles()

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/parsan'
db.init_app(app)
app.secret_key = "development-key"


@app.route('/index')
def index():
	return render_template('index1.html')
	
	
@app.route('/admin1')
def admin():
	if 'username' not in session:

		
		return redirect(url_for('adminLogin'))
		
	app.config['SQLALCHEMY_DATABASE_URI']
	with db.engine.connect() as con:
		rs = con.execute('select * from articles where id>13')
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
		return redirect('admin1')
	return render_template('add_blog.html', form = form)
		



@app.route("/")
def home():
    return render_template("index.html", articles = Articles)

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
    return render_template("tours1.html")


@app.route("/grand_tour")
def grand_tour():
    return render_template("grand_tour.html")
    
    
@app.route("/tour8")
def tour8():
    return render_template("tour8.html")
    
    
@app.route("/hotels")
def hotels():
    return render_template("hotels.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/services1")
def services1():
    return render_template("services1.html")

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