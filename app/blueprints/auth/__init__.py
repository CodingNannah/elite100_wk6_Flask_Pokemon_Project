from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import routes, models
from app import routes, models
from app.models import models