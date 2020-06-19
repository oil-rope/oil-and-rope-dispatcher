import logging

from .. import app

LOGGER = logging.getLogger(__name__)


@app.route('/dashboard/', methods=['GET'])
def dashboard():
    return '<h1>Dashboard</h1>'
