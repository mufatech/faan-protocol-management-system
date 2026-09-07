from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db
from app.models.forms import Organization, Passenger, ServiceLevel, SpecialNeed
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required
import os


@app.route('/organizations')
@login_required
def organizations():

    organizations = Organization.query.order_by(
        Organization.id.desc()
    ).all()

    return render_template(
        'admin/organizations.html',
        organizations=organizations
    )

@app.route('/organization/<int:id>')
@login_required
def view_organization(id):

    organization = Organization.query.get_or_404(id)

    return render_template(
        'admin/view_organization.html',
        organization=organization
    )

@app.route('/edit-organization/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_organization(id):

    organization = Organization.query.get_or_404(id)

    if request.method == 'POST':

        organization.organization_name = request.form['organization_name']
        organization.address = request.form['address']
        organization.contact_person = request.form['contact_person']
        organization.phone_number = request.form['phone_number']
        organization.email = request.form['email']

        db.session.commit()

        flash(
            'Organization updated successfully.',
            'success'
        )

        return redirect(
            url_for(
                'view_organization',
                id=organization.id
            )
        )

    return render_template(
        'admin/edit_organization.html',
        organization=organization
    )

@app.route('/delete-organization/<int:id>', methods=['POST'])
@login_required
def delete_organization(id):

    organization = Organization.query.get_or_404(id)

    if organization.passengers:

        flash(
            'This organization cannot be deleted because it has registered passengers.',
            'danger'
        )

        return redirect(url_for('organizations'))

    db.session.delete(organization)
    db.session.commit()

    flash(
        'Organization deleted successfully.',
        'success'
    )

    return redirect(url_for('organizations'))


@app.route('/service-levels')
@login_required
def service_levels():

    service_levels = ServiceLevel.query.order_by(
        ServiceLevel.id.desc()
    ).all()

    return render_template(
        'admin/service_levels.html',
        service_levels=service_levels
    )

@app.route('/service-level/<int:id>')
@login_required
def view_service_level(id):

    service_level = ServiceLevel.query.get_or_404(id)

    return render_template(
        'admin/view_service_level.html',
        service_level=service_level
    )

@app.route('/edit-service-level/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_service_level(id):

    service_level = ServiceLevel.query.get_or_404(id)

    if request.method == 'POST':

        service_level.service_name = request.form['service_name']
        service_level.description = request.form['description']

        db.session.commit()

        flash(
            'Service Level updated successfully.',
            'success'
        )

        return redirect(
            url_for(
                'view_service_level',
                id=service_level.id
            )
        )

    return render_template(
        'admin/edit_service_level.html',
        service_level=service_level
    )


@app.route('/delete-service-level/<int:id>', methods=['POST'])
@login_required
def delete_service_level(id):

    service_level = ServiceLevel.query.get_or_404(id)

    if service_level.passengers:

        flash(
            'This Service Level cannot be deleted because passengers are assigned to it.',
            'danger'
        )

        return redirect(url_for('service_levels'))

    db.session.delete(service_level)
    db.session.commit()

    flash(
        'Service Level deleted successfully.',
        'danger'
    )

    return redirect(url_for('service_levels'))


@app.route('/special-needs')
@login_required
def special_needs():

    needs = SpecialNeed.query.order_by(
        SpecialNeed.id.desc()
    ).all()

    return render_template(
        'admin/special_needs.html',
        needs=needs
    )

@app.route('/special-need/<int:id>')
@login_required
def view_special_need(id):

    need = SpecialNeed.query.get_or_404(id)

    return render_template(
        'admin/view_special_need.html',
        need=need
    )

@app.route('/edit-special-need/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_special_need(id):

    need = SpecialNeed.query.get_or_404(id)

    if request.method == 'POST':

        need.need_name = request.form['need_name']
        need.description = request.form.get('description')

        db.session.commit()

        flash(
            'Special Need updated successfully.',
            'success'
        )

        return redirect(
            url_for(
                'view_special_need',
                id=need.id
            )
        )

    return render_template(
        'admin/edit_special_need.html',
        need=need
    )

@app.route('/delete-special-need/<int:id>', methods=['POST'])
@login_required
def delete_special_need(id):

    need = SpecialNeed.query.get_or_404(id)

    # Remove relationships with passengers
    need.passengers = []

    db.session.delete(need)
    db.session.commit()

    flash(
        'Special Need deleted successfully.',
        'danger'
    )

    return redirect(
        url_for('special_needs')
    )

