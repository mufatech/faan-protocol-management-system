from flask import render_template
from app import app, db
from app.utils.decorators import admin_required
from app.models.forms import Organization, Passenger, ServiceLevel, SpecialNeed
from app.models.user import User

@app.route('/admin_dashboard', methods=['GET'])
@admin_required
def admin_dashboard():

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