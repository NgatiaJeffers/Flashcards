from . import main
from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db, photos
import markdown2

@main.route('/')
def index():
    '''
    Getting the vaious categories we are goin to use
    '''
    categories = [
        'pickup lines',
        'Elevator Pitch'
        'Tech Quotes',
        'Playlists',
        'Extensions',
        'Trends'
    ]

    title = 'Pitch Perfect'
    pitches = Pitch.query.all()

    return render_template('index.html', title = title, pitches = pitches, categories = categories)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    pitches_posted = Pitch.query.filter_by(user_id = current_user).all()
    return render_template('profile/profile.html', user = user, pitches = pitches_posted)

@main.route('/user/<uname>/update', methods = ['GET', POST])
@login_required
def update_profile(unam):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.usename))

    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = USer.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photo.save(request.files['photo'])
        path = 'photo/{}'.format(filename)
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))

@main.route('/new/pitch', methods = ['GET', 'POST'])
@login_required
def new_pitch():