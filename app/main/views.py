from . import main
from flask import render_template, request, redirect, url_for, abort
from ..models import User, Pitch
from flask_login import login_required


@main.route('/')
def index():
    pitches = 'hello world'
    return render_template('index.html', pitches=pitches)
