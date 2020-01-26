from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class adminForm(Form):
	username = StringField('Username', [DataRequired('What is your username ? '),
	Length(min=4)
])
	pwdhash = PasswordField('Password', validators = [DataRequired()])
	submit = SubmitField('Submit')


class blogForm(Form):
	main_topic = StringField('Main Topic', [DataRequired(),
	Length(min=2)
])

	topic_expl = TextAreaField('Topic Explanation', [DataRequired(),
	Length(min=20)
])
	blog_topic = StringField('Blog Topic')
	body = TextAreaField('Body 1')
	highlight = TextAreaField('Highlight')
	body2 = TextAreaField('Body 2')
	author_name = StringField('Author Name')
	author_expl = TextAreaField('Author Explanation')
	key_words = StringField('Key Words')


	submit = SubmitField('Submit')
	update = SubmitField('Update')