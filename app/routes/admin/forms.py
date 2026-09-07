from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from app.models.forms import Organization, Passenger, ServiceLevel, SpecialNeed
from werkzeug.utils import secure_filename
from flask_login import current_user
import os


# REGISTER Organization
# =========================
@app.route('/register-organization', methods=['GET', 'POST'])
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

    return render_template('admin/register_organization.html')

# =========================
# REGISTER SERVICE LEVEL
# =========================
@app.route('/register-service-level', methods=['GET', 'POST'])
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

# REGISTER SPECIAL NEED
@app.route('/register-special-need', methods=['GET', 'POST'])
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

    
    if request.method == 'POST':

        signature = request.files['passenger_signature']
        filename = secure_filename(signature.filename)

        signature.save(
            os.path.join(
                app.config['UPLOAD_FOLDER'],
                'passenger_signatures',
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
            passenger_signature=f'uploads/passenger_signatures/{filename}',
            user_id=current_user.id
            
        )

        # ✅ FIXED: get selected checkbox values
        selected_needs = request.form.getlist('special_need')

        # ✅ FIXED: loop selected IDs (NOT database query)
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



# # TO EDIT SPECIAL SpecialNeed
# @app.route('/edit-special-need/<int:id>', methods=['GET', 'POST'])
# def edit_special_need(id):

#     need = SpecialNeed.query.get_or_404(id)

#     if request.method == 'POST':

#         need.need_name = request.form['need_name']
#         need.description = request.form['description']

#         db.session.commit()

#         return redirect(url_for('register_special_need'))

#     return render_template('admin/edit_special_need.html', need=need)


# # TO DELETE ITEM

# @app.route('/delete-special-need/<int:id>')
# def delete_special_need(id):

#     need = SpecialNeed.query.get_or_404(id)

#     db.session.delete(need)
#     db.session.commit()

#     return redirect(url_for('register_special_need'))

# @app.route('/edit-service-level/<int:id>', methods=['GET', 'POST'])
# def edit_service_level(id):

#     service = ServiceLevel.query.get_or_404(id)

#     if request.method == 'POST':

#         service.service_name = request.form['service_name']
#         service.description = request.form['description']

#         db.session.commit()

#         return redirect(url_for('register_service_level'))

#     return render_template(
#         'admin/edit_service_level.html',
#         service=service
#     )

# @app.route('/delete-service-level/<int:id>')
# def delete_service_level(id):

#     service = ServiceLevel.query.get_or_404(id)

#     db.session.delete(service)
#     db.session.commit()

#     return redirect(url_for('register_service_level'))