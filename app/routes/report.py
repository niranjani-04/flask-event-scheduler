from flask import Blueprint, render_template, request
from datetime import datetime
from app.models import Event, Resource, EventResourceAllocation
from app import db

report_bp = Blueprint('report', __name__, url_prefix='/report')

@report_bp.route('/', methods=['GET', 'POST'])
def report():
    data = []

    if request.method == 'POST':
        start = datetime.fromisoformat(request.form['start'])
        end = datetime.fromisoformat(request.form['end'])

        resources = Resource.query.all()
        for r in resources:
            events = db.session.query(Event).join(EventResourceAllocation).filter(
                EventResourceAllocation.resource_id == r.resource_id,
                Event.start_time >= start,
                Event.end_time <= end
            ).all()

            total_hours = sum((e.end_time - e.start_time).seconds / 3600 for e in events)
            upcoming = db.session.query(Event).join(EventResourceAllocation).filter(
                EventResourceAllocation.resource_id == r.resource_id,
                Event.start_time > datetime.now()
            ).count()

            data.append({
                'name': r.resource_name,
                'type': r.resource_type,
                'hours': total_hours,
                'bookings': len(events),
                'upcoming': upcoming
            })

    return render_template('report.html', report=data)
