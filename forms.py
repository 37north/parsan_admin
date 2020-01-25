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
	Length(min=50)
])
	blog_topic = StringField('Blog Topic', [DataRequired(),
	Length(min=2)
])
	body = TextAreaField('Body 1', [DataRequired(),
	Length(min=50)
])
	highlight = TextAreaField('Highlight', [DataRequired(),
	Length(min=50)
])
	body2 = TextAreaField('Body 2', [DataRequired(),
	Length(min=50)
])
	author_name = StringField('Author Name', [DataRequired(),
	Length(min=2)
])
	author_expl = TextAreaField('Author Explanation', [DataRequired(),
	Length(min=50)
])
	key_words = StringField('key Words', [DataRequired(),
	Length(min=2)
])


	submit = SubmitField('Submit')