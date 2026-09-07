from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import app
from app.models.user import User


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        # User does not exist
        if not user:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))

        # User has been deactivated
        if not user.is_active:
            flash(
                'Your account has been deactivated. Please contact the administrator.',
                'danger'
            )
            return redirect(url_for('login'))

        # Incorrect password
        if not user.check_password(password):
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))

        # Login user
        login_user(user)

        flash("Login successful.", "success")

        # Redirect based on role
        if user.role == "admin":
            return redirect(url_for("admin_dashboard"))

        elif user.role == "protocol":
            return redirect(url_for("protocol_dashboard"))

        else:
            return redirect(url_for("user_dashboard"))

    return render_template("admin/login.html")


@app.route('/logout')
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.", "success")

    return redirect(url_for("login"))