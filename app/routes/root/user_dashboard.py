from flask import render_template, redirect, request, url_for, flash
from app import app, db
from app.utils.decorators import user_required
from app.utils.auth import get_user
from app.models.forms import Passenger, Organization, ServiceLevel, SpecialNeed


@app.route('/user_dashboard', methods=['GET'])
@user_required
def user_dashboard():

    user = get_user()

    passenger_count = Passenger.query.filter_by(
        user_id=user.id
    ).count()

    return render_template(
        'user/user_dashboard.html',
        passenger_count=passenger_count
    )


@app.route('/my-passengers')
@user_required
def my_passengers():

    user = get_user()

    passengers = Passenger.query.filter_by(
        user_id=user.id
    ).order_by(
        Passenger.id.desc()
    ).all()

    return render_template(
        'user/my_passengers.html',
        passengers=passengers
    )


@app.route('/my-passenger/<int:id>')
@user_required
def view_my_passenger(id):

    user = get_user()

    passenger = Passenger.query.filter_by(
        id=id,
        user_id=user.id
    ).first_or_404()

    return render_template(
        'user/view_passenger.html',
        passenger=passenger
    )


@app.route(
    '/edit-my-passenger/<int:id>',
    methods=['GET', 'POST']
)
@user_required
def edit_my_passenger(id):

    user = get_user()

    passenger = Passenger.query.filter_by(
        id=id,
        user_id=user.id
    ).first_or_404()

    organizations = Organization.query.all()
    service_levels = ServiceLevel.query.all()
    special_needs = SpecialNeed.query.all()

    if request.method == 'POST':

        passenger.passenger_name = request.form['passenger_name']
        passenger.travel_date = request.form['travel_date']
        passenger.organization_id = request.form['organization_id']
        passenger.service_level_id = request.form['service_level_id']
        passenger.position = request.form.get('position')
        passenger.flight = request.form['flight']
        passenger.itinerary = request.form.get('itinerary')
        passenger.additional_request = request.form.get(
            'additional_request'
        )

        # Update many-to-many special needs
        passenger.special_needs.clear()

        selected_needs = request.form.getlist('special_need')

        for need_id in selected_needs:

            need = SpecialNeed.query.get(int(need_id))

            if need:
                passenger.special_needs.append(need)

        db.session.commit()

        flash(
            'Passenger updated successfully.',
            'success'
        )

        return redirect(
            url_for(
                'view_my_passenger',
                id=passenger.id
            )
        )

    return render_template(
        'user/edit_passenger.html',
        passenger=passenger,
        organizations=organizations,
        service_levels=service_levels,
        needs=special_needs
    )


@app.route('/my-report')
@user_required
def my_report():

    user = get_user()

    organization_id = request.args.get('organization_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Start with ONLY the currently logged-in user's passengers
    query = Passenger.query.filter_by(
        user_id=user.id
    )

    if organization_id:
        query = query.filter(
            Passenger.organization_id == organization_id
        )

    if start_date:
        query = query.filter(
            Passenger.travel_date >= start_date
        )

    if end_date:
        query = query.filter(
            Passenger.travel_date <= end_date
        )

    passengers = query.order_by(
        Passenger.id.desc()
    ).all()

    organizations = Organization.query.order_by(
        Organization.organization_name
    ).all()

    return render_template(
        'user/my_report.html',
        passengers=passengers,
        organizations=organizations,
        selected_organization=organization_id,
        start_date=start_date,
        end_date=end_date
    )

