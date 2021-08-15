from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix="/")


@bp.route('/')
def hello_world():
    return "hello, world!"


@bp.route("/walwal")
def walwal():
    return "walwalwal!!"