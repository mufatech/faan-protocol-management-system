from flask import render_template, request, redirect, url_for, flash, session
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

        # Store the user in the appropriate independent session
        if user.role == "admin":

            session["admin_user_id"] = user.id

            flash("Admin login successful.", "success")

            return redirect(url_for("admin_dashboard"))

        elif user.role == "protocol":

            session["protocol_user_id"] = user.id

            flash("Login successful.", "success")

            return redirect(url_for("protocol_dashboard"))

        else:

            session["user_user_id"] = user.id

            flash("Login successful.", "success")

            return redirect(url_for("user_dashboard"))

    return render_template("admin/login.html")


@app.route('/admin-logout')
def admin_logout():

    session.pop("admin_user_id", None)

    flash("Admin logged out successfully.", "success")

    return redirect(url_for("login"))


@app.route('/user-logout')
def user_logout():

    session.pop("user_user_id", None)

    flash("Logged out successfully.", "success")

    return redirect(url_for("login"))


@app.route('/protocol-logout')
def protocol_logout():

    session.pop("protocol_user_id", None)

    flash("Logged out successfully.", "success")

    return redirect(url_for("login"))
