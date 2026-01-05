from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Resource

resources_bp = Blueprint('resources', __name__, url_prefix='/resources')

@resources_bp.route('/')
def list_resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)

@resources_bp.route('/add', methods=['POST'])
def add_resource():
    name = request.form['name']
    rtype = request.form['type']
    resource = Resource(resource_name=name, resource_type=rtype)
    db.session.add(resource)
    db.session.commit()
    return redirect(url_for('resources.list_resources'))
