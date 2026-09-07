from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime
import random

# # Generate unique agency code
# def generate_agency_code():
#     while True:
#         code = f"AGY-{random.randint(10000, 99999)}"

#         existing = Agency.query.filter_by(agency_code=code).first()

#         if not existing:
#             return code

# # class for agency
      
# class Agency(db.Model):
#     __tablename__ = "agencies"

#     id = db.Column(db.Integer, primary_key=True)

#     agency_name = db.Column(db.String(150), nullable=False)

#     address = db.Column(db.Text, nullable=False)

#     contact_person = db.Column(db.String(100), nullable=False)

#     phone_number = db.Column(db.String(20), nullable=False)

#     email = db.Column(db.String(120), unique=True, nullable=False)

#     agency_code = db.Column(
#         db.String(20),
#         unique=True,
#         nullable=False,
#         default=generate_agency_code
#     )

#     # Relationship with Passenger
#     passengers = db.relationship('Passenger', backref='agency', lazy=True)

# Generate unique organization code
def generate_organization_code():
    while True:
        code = f"ORG-{random.randint(10000, 99999)}"

        existing = Organization.query.filter_by(organization_code=code).first()

        if not existing:
            return code

# class for organization
      
class Organization(db.Model):
    __tablename__ = "organizations"

    id = db.Column(db.Integer, primary_key=True)

    organization_name = db.Column(db.String(150), nullable=False)

    address = db.Column(db.Text, nullable=False)

    contact_person = db.Column(db.String(100), nullable=False)

    phone_number = db.Column(db.String(20), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    organization_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        default=generate_organization_code
    )

    # Relationship with Passenger
    passengers = db.relationship('Passenger', backref='organization', lazy=True)


class ServiceLevel(db.Model):
    __tablename__ = "service_levels"

    id = db.Column(db.Integer, primary_key=True)

    service_name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    description = db.Column(db.Text)

    # Relationship with Passenger
    passengers = db.relationship(
        'Passenger',
        backref='service_level',
        lazy=True
    )

# Class for Special Need
class SpecialNeed(db.Model):
    __tablename__ = "special_needs"

    id = db.Column(db.Integer, primary_key=True)

    need_name = db.Column(db.String(150), unique=True, nullable=False)

    description = db.Column(db.Text, nullable=True)

   

# class for passenger

passenger_special_needs = db.Table(
    'passenger_special_needs',

    db.Column(
        'passenger_id',
        db.Integer,
        db.ForeignKey('passengers.id'),
        primary_key=True
    ),

    db.Column(
        'special_need_id',
        db.Integer,
        db.ForeignKey('special_needs.id'),
        primary_key=True
    )
)

class Passenger(db.Model):
    __tablename__ = "passengers"

    id = db.Column(db.Integer, primary_key=True)

    passenger_name = db.Column(db.String(100), nullable=False)
    travel_date = db.Column(
        db.Date,
        nullable=False
    )

    position = db.Column(
        db.String(100),
        nullable=True
    )

    flight = db.Column(
        db.String(100),
        nullable=False
    )

    itinerary = db.Column(
        db.Text,
        nullable=True
    )

    additional_request = db.Column(
        db.Text,
        nullable=True
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

        # Foreign key to organization
    organization_id = db.Column(
        db.Integer,
        db.ForeignKey('organizations.id'),
        nullable=False
    ) 

    # Foreign key to Service Level
    service_level_id = db.Column(
    db.Integer,
    db.ForeignKey('service_levels.id'),
    nullable=False
)  
    
    special_needs = db.relationship(
    'SpecialNeed',
    secondary=passenger_special_needs,
    backref=db.backref('passengers', lazy='dynamic')
)
    
    passenger_signature = db.Column(db.String(255))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

   
    
    

