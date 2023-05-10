from flask import Blueprint
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required


bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    return "Order Up!"
