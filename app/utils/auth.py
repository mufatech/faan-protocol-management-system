from functools import wraps
from flask import session, redirect, url_for, abort
from app.models.user import User


def get_admin_user():
    """Return the currently logged-in admin."""
    user_id = session.get("admin_user_id")

    if not user_id:
        return None

    user = User.query.get(user_id)

    if not user:
        session.pop("admin_user_id", None)
        return None

    if user.role != "admin":
        session.pop("admin_user_id", None)
        return None

    if not user.is_active:
        session.pop("admin_user_id", None)
        return None

    return user


def get_protocol_user():
    """Return the currently logged-in protocol officer."""
    user_id = session.get("protocol_user_id")

    if not user_id:
        return None

    user = User.query.get(user_id)

    if not user:
        session.pop("protocol_user_id", None)
        return None

    if user.role != "protocol":
        session.pop("protocol_user_id", None)
        return None

    if not user.is_active:
        session.pop("protocol_user_id", None)
        return None

    return user


def get_user():
    """Return the currently logged-in normal user."""
    user_id = session.get("user_user_id")

    if not user_id:
        return None

    user = User.query.get(user_id)

    if not user:
        session.pop("user_user_id", None)
        return None

    if user.role != "user":
        session.pop("user_user_id", None)
        return None

    if not user.is_active:
        session.pop("user_user_id", None)
        return None

    return user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        user = get_admin_user()

        if not user:
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return decorated_function


def protocol_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        user = get_protocol_user()

        if not user:
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return decorated_function


def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        user = get_user()

        if not user:
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return decorated_function


def get_current_dashboard():
    """
    Return the dashboard endpoint for the currently
    authenticated role.
    """

    if get_admin_user():
        return "admin_dashboard"

    if get_protocol_user():
        return "protocol_dashboard"

    if get_user():
        return "user_dashboard"

    return "login"
