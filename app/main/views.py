from . import main
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db, photos
