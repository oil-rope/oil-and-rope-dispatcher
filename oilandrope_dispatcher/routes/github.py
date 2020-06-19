import logging

from flask import json, request

from .. import app

LOGGER = logging.getLogger(__name__)


@app.route('/github/', methods=['POST'])
def github_payload():
    if request.headers['Content-Type'] == 'application/json':
        payload = request.json
        LOGGER.info('Payload received: %s', payload)
        return json.dumps(request.json)
