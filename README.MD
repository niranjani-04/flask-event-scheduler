# Flask Event Scheduling & Resource Allocation System

## Project Description
This project is a web-based Event Scheduling and Resource Allocation System developed using Flask.  
It allows organizations to create events such as workshops, seminars, or classes and assign shared resources like rooms, instructors, and equipment.

The system ensures that resources are not double-booked by validating overlapping time slots during allocation.  
This project was developed as part of the Flask Hiring Test for Tridots Tech.

---

## Technology Stack
- Backend: Flask (Python 3)
- Database: SQLite
- Frontend: HTML, CSS, Bootstrap
- Template Engine: Jinja2

---

## Features Implemented
- Create, edit, and view events
- Create and manage shared resources
- Allocate one or more resources to events
- Backend conflict detection for overlapping time slots
- Clear error messages when conflicts occur
- Resource utilization report with date range filtering
- Clean and responsive UI with basic animations

---

## Installation Instructions

### Step 1: Clone the Repository

git clone https://github.com/niranjani-04/flask-event-scheduler.git
cd flask-event-scheduler
###Step 2: Create Virtual Environment

python -m venv venv
Activate the environment:
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Database Setup

The project uses SQLite, so no external database configuration is required.

The database file (database.db) is created automatically when the application runs for the first time.

How to Run the Application
python run.py

Open your browser and navigate to:

http://127.0.0.1:5000

Database Schema

The application uses the following tables:

Event Table

id (Primary Key)

title

start_time

end_time

description

Resource Table

id (Primary Key)

name

type

EventResourceAllocation Table

id (Primary Key)

event_id (Foreign Key)

resource_id (Foreign Key)

This schema supports a many-to-many relationship between events and resources.

Screenshots

Screenshots of the following screens are included in the screenshots/ folder:


Demo Video Link:
(https://youtu.be/wuizCgIAaeM)

Author

Niranjani
