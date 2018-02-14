from . import main
from flask import render_template, redirect, url_for
from ..models import User, Pitch
from flask_login import login_required
from .form import PitchForm


@main.route('/')
def index():
    pitches = Pitch.query.all()
    return render_template('index.html', pitches=pitches)


@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    '''
    View new pitch route function that returns a page with a form to create a category
    '''
    form = PitchForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pitch = Pitch(name=name)
        new_pitch.save_pitches()

        return redirect(url_for('.index'))

    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, pitch_form=form)
