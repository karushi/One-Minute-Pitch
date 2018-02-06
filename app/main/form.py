from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    name = StringField('Category name', validators=[Required()])
    submit = SubmitField('Create')


class LineForm(FlaskForm):
    '''
   Class to create a wtf form for creating a pitch
    '''
   line_content = StringField('One Minute Pitch', validators=[Required()])
   submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    '''
   Class to create a wtf form for creating a feedback on a pitch
    '''
   comment_content =  TextAreaField('Comment', validators=[Required()])
   submit = SubmitField('Submit')


class UpvoteForm(FlaskForm):
    '''
   Class to create a wtf form for upvoting a pitch
    '''
   submit = SubmitField('Upvote')
