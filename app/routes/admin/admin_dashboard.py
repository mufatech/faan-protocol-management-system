from flask import render_template, redirect, url_for, flash
from app import app, db
from app.utils.decorators import admin_required
from flask_login import login_required, current_user
from app.models.forms import Organization, Passenger, ServiceLevel, SpecialNeed
from app.models.user import User

@app.route('/admin_dashboard', methods=['GET'])
@login_required
def admin_dashboard():

    if current_user.role != 'admin':
        flash('Access denied')
        return redirect(url_for("user_dashboard"))

    user_count = User.query.count()
    organization_count = Organization.query.count()
    passenger_count = Passenger.query.count()
    service_level_count = ServiceLevel.query.count()
    special_need_count = SpecialNeed.query.count()

    return render_template(
        'admin/dashboard.html',
        user_count=user_count,
        organization_count=organization_count,
        passenger_count=passenger_count,
        service_level_count=service_level_count,
        special_need_count=special_need_count
    )