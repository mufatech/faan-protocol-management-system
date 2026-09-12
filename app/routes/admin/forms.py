from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.forms import Organization, Passenger, ServiceLevel, SpecialNeed
from flask_login import login_required, current_user
from app.utils.decorators import admin_required
from app.utils.auth import get_admin_user
from app.utils.auth import get_admin_user, get_protocol_user, get_user
from werkzeug.utils import secure_filename
import os


# =========================
# REGISTER ORGANIZATION
# =========================
@app.route('/register-organization', methods=['GET', 'POST'])
@admin_required
def register_organization():

    if request.method == 'POST':

        organization = Organization(
            organization_name=request.form['organization_name'],
            address=request.form['address'],
            contact_person=request.form['contact_person'],
            phone_number=request.form['phone_number'],
            email=request.form['email']
        )

        db.session.add(organization)
        db.session.commit()

        return redirect(url_for('register_organization'))

    return render_template(
        'admin/register_organization.html'
    )


# =========================
# REGISTER SERVICE LEVEL
# =========================
@app.route('/register-service-level', methods=['GET', 'POST'])
@admin_required
def register_service_level():

    if request.method == 'POST':

        service_name = request.form['service_name']
        description = request.form['description']

        # Check if service level already exists
        existing_service = ServiceLevel.query.filter_by(
            service_name=service_name
        ).first()

        if existing_service:
            return "Service Level Already Exists"

        service_level = ServiceLevel(
            service_name=service_name,
            description=description
        )

        db.session.add(service_level)
        db.session.commit()

        return redirect(url_for('register_service_level'))

    # Display all service levels
    service_levels = ServiceLevel.query.all()

    return render_template(
        'admin/register_service_level.html',
        service_levels=service_levels
    )


# =========================
# REGISTER SPECIAL NEED
# =========================
@app.route('/register-special-need', methods=['GET', 'POST'])
@admin_required
def register_special_need():

    if request.method == 'POST':

        need = SpecialNeed(
            need_name=request.form['need_name'],
            description=request.form['description']
        )

        db.session.add(need)
        db.session.commit()

        return redirect(url_for('register_special_need'))

    needs = SpecialNeed.query.all()

    return render_template(
        'admin/register_special_need.html',
        needs=needs
    )


# =========================
# REGISTER PASSENGER
# =========================
@app.route('/register-passenger', methods=['GET', 'POST'])
def register_passenger():

     
    organizations = Organization.query.all()
    service_levels = ServiceLevel.query.all()
    special_needs = SpecialNeed.query.all()

    # ---------------------------------
    # DETERMINE CORRECT DASHBOARD
    # ---------------------------------
    if current_user.role == 'admin':
        dashboard_endpoint = 'admin_dashboard'

    else:
        dashboard_endpoint = 'user_dashboard'


    if request.method == 'POST':

        signature = request.files.get('passenger_signature')

        filename = None

        if signature and signature.filename:
            filename = secure_filename(signature.filename)

            signature_folder = os.path.join(
                app.config['UPLOAD_FOLDER'],
                'passenger_signatures'
            )

            os.makedirs(
                signature_folder,
                exist_ok=True
            )

            signature.save(
                os.path.join(
                    signature_folder,
                    filename
                )
            )

        passenger = Passenger(
            passenger_name=request.form['passenger_name'],
            travel_date=request.form['travel_date'],
            service_level_id=request.form['service_level_id'],
            organization_id=request.form['organization_id'],
            position=request.form['position'],
            flight=request.form['flight'],
            itinerary=request.form['itinerary'],
            additional_request=request.form.get('additional_request'),
            passenger_signature=(
                f'uploads/passenger_signatures/{filename}'
                if filename else None
            ),

            # IMPORTANT:
            # Use the Admin obtained from our custom session
            # instead of Flask-Login current_user.
            user_id=admin.id
        )

        # Get selected checkbox values
        selected_needs = request.form.getlist('special_need')

        # Add selected special needs
        for need_id in selected_needs:

            need = SpecialNeed.query.get(int(need_id))

            if need:
                passenger.special_needs.append(need)

        db.session.add(passenger)
        db.session.commit()

        return "Passenger Registered Successfully"

    return render_template(
        'admin/register_passenger.html',
        organizations=organizations,
        service_levels=service_levels,
        needs=special_needs
    )

