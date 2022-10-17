from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='')

from . import routes, models
from app import routes, models
from app.models import models