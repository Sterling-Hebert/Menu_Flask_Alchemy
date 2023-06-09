from flask import Blueprint, render_template, redirect, url_for, request
from ..forms import LoginForm
from ..models import Employee
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("session", __name__, url_prefix="/session")

# pip install email_validator

# @bp.route("/")
# @login_required
# def index():
#     return "Order Up!"

# The use of @bp, here, assumes you named the variable "bp"
# that holds your Blueprint object for this routing module
@bp.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("orders.index"))
        return render_template("login.html", form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            empl_number = form.employee_number.data
            employee = Employee.query.filter(Employee.employee_number == empl_number).first()
            print(employee.check_password(form.password.data), employee, form.password.data)
            if not employee or not employee.check_password(form.password.data):
                return redirect(url_for(".login"))
            login_user(employee)
            return redirect(url_for("orders.index"))
@bp.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for('.login'))
