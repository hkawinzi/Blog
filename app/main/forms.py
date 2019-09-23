from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you!',validators= [Required()])
    submit = SubmitField('update bio')

class PostBlog(FlaskForm):
    category = SelectField('Select the category',choices=[('Business','Business'),('Nutrition','Nutrition'),('Education','Education'),('Politics','Politics'),('General','General')])
    title = TextAreaField('Title')
    text = TextAreaField('Type your blog or quote')
    submit = SubmitField('Post your blog or quote')

class PostCommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment')
    submit = SubmitField('Comment')

class SubscribeForm(FlaskForm):
    email = TextAreaField('Your email')
    submit = SubmitField('Subscribe')