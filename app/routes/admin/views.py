from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from app import app, db

from app.models.forms import (
    Organization,
    Passenger,
    ServiceLevel,
    SpecialNeed
)

from app.utils.decorators import admin_required


# =========================
# ORGANIZATIONS
# =========================
@app.route('/organizations')
@admin_required
def organizations():

    organizations = Organization.query.order_by(
        Organization.id.desc()
    ).all()

    return render_template(
        'admin/organizations.html',
        organizations=organizations
    )


# =========================
# VIEW ORGANIZATION
# =========================
@app.route('/organization/<int:id>')
@admin_required
def view_organization(id):

    organization = Organization.query.get_or_404(
        id
    )

    return render_template(
        'admin/view_organization.html',
        organization=organization
    )


# =========================
# EDIT ORGANIZATION
# =========================
@app.route(
    '/edit-organization/<int:id>',
    methods=['GET', 'POST']
)
@admin_required
def edit_organization(id):

    organization = Organization.query.get_or_404(
        id
    )

    if request.method == 'POST':

        organization.organization_name = (
            request.form['organization_name']
        )

        organization.address = (
            request.form['address']
        )

        organization.contact_person = (
            request.form['contact_person']
        )

        organization.phone_number = (
            request.form['phone_number']
        )

        organization.email = (
            request.form['email']
        )

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


# =========================
# DELETE ORGANIZATION
# =========================
@app.route(
    '/delete-organization/<int:id>',
    methods=['POST']
)
@admin_required
def delete_organization(id):

    organization = Organization.query.get_or_404(
        id
    )

    if organization.passengers:

        flash(
            'This organization cannot be deleted because it has registered passengers.',
            'danger'
        )

        return redirect(
            url_for('organizations')
        )

    db.session.delete(
        organization
    )

    db.session.commit()

    flash(
        'Organization deleted successfully.',
        'success'
    )

    return redirect(
        url_for('organizations')
    )


# =========================
# SERVICE LEVELS
# =========================
@app.route('/service-levels')
@admin_required
def service_levels():

    service_levels = ServiceLevel.query.order_by(
        ServiceLevel.id.desc()
    ).all()

    return render_template(
        'admin/service_levels.html',
        service_levels=service_levels
    )


# =========================
# VIEW SERVICE LEVEL
# =========================
@app.route('/service-level/<int:id>')
@admin_required
def view_service_level(id):

    service_level = ServiceLevel.query.get_or_404(
        id
    )

    return render_template(
        'admin/view_service_level.html',
        service_level=service_level
    )


# =========================
# EDIT SERVICE LEVEL
# =========================
@app.route(
    '/edit-service-level/<int:id>',
    methods=['GET', 'POST']
)
@admin_required
def edit_service_level(id):

    service_level = ServiceLevel.query.get_or_404(
        id
    )

    if request.method == 'POST':

        service_level.service_name = (
            request.form['service_name']
        )

        service_level.description = (
            request.form['description']
        )

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


# =========================
# DELETE SERVICE LEVEL
# =========================
@app.route(
    '/delete-service-level/<int:id>',
    methods=['POST']
)
@admin_required
def delete_service_level(id):

    service_level = ServiceLevel.query.get_or_404(
        id
    )

    if service_level.passengers:

        flash(
            'This Service Level cannot be deleted because passengers are assigned to it.',
            'danger'
        )

        return redirect(
            url_for('service_levels')
        )

    db.session.delete(
        service_level
    )

    db.session.commit()

    flash(
        'Service Level deleted successfully.',
        'success'
    )

    return redirect(
        url_for('service_levels')
    )


# =========================
# SPECIAL NEEDS
# =========================
@app.route('/special-needs')
@admin_required
def special_needs():

    needs = SpecialNeed.query.order_by(
        SpecialNeed.id.desc()
    ).all()

    return render_template(
        'admin/special_needs.html',
        needs=needs
    )


# =========================
# VIEW SPECIAL NEED
# =========================
@app.route('/special-need/<int:id>')
@admin_required
def view_special_need(id):

    need = SpecialNeed.query.get_or_404(
        id
    )

    return render_template(
        'admin/view_special_need.html',
        need=need
    )


# =========================
# EDIT SPECIAL NEED
# =========================
@app.route(
    '/edit-special-need/<int:id>',
    methods=['GET', 'POST']
)
@admin_required
def edit_special_need(id):

    need = SpecialNeed.query.get_or_404(
        id
    )

    if request.method == 'POST':

        need.need_name = (
            request.form['need_name']
        )

        need.description = request.form.get(
            'description'
        )

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


# =========================
# DELETE SPECIAL NEED
# =========================
@app.route(
    '/delete-special-need/<int:id>',
    methods=['POST']
)
@admin_required
def delete_special_need(id):

    need = SpecialNeed.query.get_or_404(
        id
    )

    # Remove relationships with passengers
    need.passengers = []

    db.session.delete(
        need
    )

    db.session.commit()

    flash(
        'Special Need deleted successfully.',
        'danger'
    )

    return redirect(
        url_for('special_needs')
    )