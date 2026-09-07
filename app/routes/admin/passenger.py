from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from app.models.forms import  Organization, Passenger, ServiceLevel, SpecialNeed
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

@app.route('/passengers')
@login_required
def passengers():

    passengers = Passenger.query.order_by(
        Passenger.id.desc()
    ).all()

    return render_template(
        'admin/passengers.html',
        passengers=passengers
    )

@app.route('/passenger/<int:id>')
def view_passenger(id):
    passenger = Passenger.query.get_or_404(id)
    return render_template('admin/view_passenger.html', passenger=passenger)



@app.route('/edit-passenger/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_passenger(id):

    passenger = Passenger.query.get_or_404(id)

    organizations = Organization.query.all()
    service_levels = ServiceLevel.query.all()
    special_needs = SpecialNeed.query.all()

    if request.method == 'POST':

        passenger.passenger_name = request.form['passenger_name']
        passenger.travel_date = request.form['travel_date']
        passenger.service_level_id = request.form['service_level_id']
        passenger.organization_id = request.form['organization_id']
        passenger.position = request.form['position']
        passenger.flight = request.form['flight']
        passenger.itinerary = request.form['itinerary']
        passenger.additional_request = request.form.get('additional_request')

        # Update special needs
        selected_needs = request.form.getlist('special_need')

        passenger.special_needs.clear()

        for need_id in selected_needs:

            need = SpecialNeed.query.get(int(need_id))

            if need:
                passenger.special_needs.append(need)

        #Update Signature
        signature = request.files.get('passenger_signature')

        if signature and signature.filename:

            filename = secure_filename(signature.filename)

            signature.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    'passenger_signatures',
                    filename
                )
            )

            passenger.passenger_signature = (
                f'uploads/passenger_signatures/{filename}'
            )
        db.session.commit()

        return redirect(
            url_for(
                'view_passenger',
                id=passenger.id
            )
        )

    return render_template(
        'admin/edit_passenger.html',
        passenger=passenger,
        organizations=organizations,
        service_levels=service_levels,
        needs=special_needs
    )

@app.route('/delete-passenger/<int:id>', methods=['POST'])
@login_required
def delete_passenger(id):

    passenger = Passenger.query.get_or_404(id)

    db.session.delete(passenger)
    db.session.commit()

    return redirect(url_for('passengers'))

