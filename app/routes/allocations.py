from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Event, Resource, EventResourceAllocation

allocations_bp = Blueprint('allocations', __name__, url_prefix='/allocations')

@allocations_bp.route('/', methods=['GET', 'POST'])
def allocate():
    events = Event.query.all()
    resources = Resource.query.all()

    if request.method == 'POST':
        event_id = int(request.form['event'])
        resource_id = int(request.form['resource'])

        event = Event.query.get(event_id)

        conflict = db.session.query(Event).join(EventResourceAllocation).filter(
            EventResourceAllocation.resource_id == resource_id,
            Event.start_time < event.end_time,
            Event.end_time > event.start_time
        ).first()

        if conflict:
            flash('Resource already booked for overlapping time')
            return redirect(url_for('allocations.allocate'))

        allocation = EventResourceAllocation(event_id=event_id, resource_id=resource_id)
        db.session.add(allocation)
        db.session.commit()

    allocations = EventResourceAllocation.query.all()
    return render_template('allocate.html', events=events, resources=resources, allocations=allocations)
