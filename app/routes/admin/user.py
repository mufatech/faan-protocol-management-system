from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app import app, db
from app.models.user import User
from app.utils.decorators import admin_required
from werkzeug.utils import secure_filename
from uuid import uuid4
from flask import send_from_directory
import os


@app.route('/create_user', methods=['GET', 'POST'])
@admin_required
def create_user():

    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('User already exists', 'danger')
            return redirect(url_for('create_user'))

       
        officer_signature = request.files.get('officer_signature')

        if not officer_signature:
            flash('Please select a signature file.', 'danger')
            return redirect(url_for('create_user'))

        if officer_signature.filename == '':
            flash('Please select a signature file.', 'danger')
            return redirect(url_for('create_user'))

        signature_name = secure_filename(
            officer_signature.filename
        )

        allowed_extensions = {'png', 'jpg', 'jpeg'}

        if '.' not in signature_name:
            flash('Invalid file selected.', 'danger')
            return redirect(url_for('create_user'))
       
        extension = signature_name.rsplit('.', 1)[1].lower()
        signature_name = f"{uuid4().hex}.{extension}"

        if extension not in allowed_extensions:
            flash('Only PNG, JPG and JPEG files are allowed.', 'danger')
            return redirect(url_for('create_user'))
        

        upload_folder = os.path.join(
            app.config['UPLOAD_FOLDER'],
            'officer_signatures'
        )

        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(
            upload_folder,
            signature_name
        )

        print("Saving to:", file_path)
        print("UPLOAD_FOLDER:", app.config['UPLOAD_FOLDER'])
        print("DIR EXISTS:", os.path.exists(upload_folder))
        print("IS DIRECTORY:", os.path.isdir(upload_folder))
        print("IS FILE:", os.path.isfile(upload_folder))    
        
        officer_signature.save(file_path)

        
        user = User(
            fullname=fullname,
            email=email,
            officer_signature=
                f'uploads/officer_signatures/{signature_name}'
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('User created successfully', 'success')

        return redirect(url_for('users'))

    users = User.query.all()

    return render_template(
    'admin/create_user.html',
    users=users
)


@app.route('/users')
@admin_required
def users():

    users = User.query.order_by(
        User.id.desc()
    ).all()

    return render_template(
        'admin/users.html',
        users=users
    )

@app.route('/user/<int:id>')
@admin_required
def view_user(id):

    user = User.query.get_or_404(id)

    return render_template(
        'admin/view_user.html',
        user=user
    )

@app.route('/edit-user/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_user(id):

    user = User.query.get_or_404(id)

    if request.method == 'POST':

        fullname = request.form['fullname'].strip()
        email = request.form['email'].strip().lower()
        password = request.form.get('password')

        # Check if another user already has this email
        existing_user = User.query.filter(
            User.email == email,
            User.id != user.id
        ).first()

        if existing_user:

            flash(
                'Another user already exists with this email.',
                'danger'
            )

            return redirect(
                url_for('edit_user', id=user.id)
            )

        user.fullname = fullname
        user.email = email

        # Change password only if a new password was entered
        if password:

            user.set_password(password)

        # Replace signature if a new one was uploaded
        officer_signature = request.files.get(
            'officer_signature'
        )

        if officer_signature and officer_signature.filename:

            signature_name = secure_filename(
                officer_signature.filename
            )

            allowed_extensions = {
                'png',
                'jpg',
                'jpeg'
            }

            if '.' not in signature_name:

                flash(
                    'Invalid signature file.',
                    'danger'
                )

                return redirect(
                    url_for('edit_user', id=user.id)
                )

            extension = signature_name.rsplit(
                '.',
                1
            )[1].lower()

            if extension not in allowed_extensions:

                flash(
                    'Only PNG, JPG and JPEG files are allowed.',
                    'danger'
                )

                return redirect(
                    url_for('edit_user', id=user.id)
                )

            signature_name = (
                f"{uuid4().hex}.{extension}"
            )

            upload_folder = os.path.join(
                app.config['UPLOAD_FOLDER'],
                'officer_signatures'
            )

            os.makedirs(
                upload_folder,
                exist_ok=True
            )

            file_path = os.path.join(
                upload_folder,
                signature_name
            )

            officer_signature.save(file_path)

            user.officer_signature = (
                f'uploads/officer_signatures/{signature_name}'
            )

        db.session.commit()

        flash(
            'User updated successfully.',
            'success'
        )

        return redirect(
            url_for(
                'view_user',
                id=user.id
            )
        )

    return render_template(
        'admin/edit_user.html',
        user=user
    )

@app.route('/toggle-user-status/<int:id>', methods=['POST'])
@admin_required
def toggle_user_status(id):

    user = User.query.get_or_404(id)

    user.is_active = not user.is_active

    db.session.commit()

    if user.is_active:
        flash(
            f'{user.fullname} has been activated successfully.',
            'success'
        )
    else:
        flash(
            f'{user.fullname} has been deactivated successfully.',
            'warning'
        )

    return redirect(url_for('users'))


@app.route('/uploads/<path:filename>')
@admin_required
def uploaded_file(filename):

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename
    )