
# keep social for chatting -- not the main thing of this project!
from flask import Blueprint

bp = Blueprint('social', __name__, url_prefix='')

from . import routes