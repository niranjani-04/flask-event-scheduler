from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from app.models import Event

events_bp = Blueprint('events', __name__)

@events_bp.route('/')
def index():
    events = Event.query.all()
    return render_template('events.html', events=events)

@events_bp.route('/add', methods=['POST'])
def add_event():
    title = request.form['title']
    start = datetime.fromisoformat(request.form['start'])
    end = datetime.fromisoformat(request.form['end'])
    desc = request.form['description']

    if start >= end:
        flash('Start time must be before end time')
        return redirect(url_for('events.index'))

    event = Event(title=title, start_time=start, end_time=end, description=desc)
    db.session.add(event)
    db.session.commit()
    return redirect(url_for('events.index'))
