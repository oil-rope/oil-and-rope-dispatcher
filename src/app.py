import logging

from flask import Flask, json, request

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/github/', methods=['POST'])
def github_payload():
    if request.headers['Content-Type'] == 'application/json':
        payload = request.json
        LOGGER.info('Payload received: %s', payload)
        return json.dumps(request.json)


if __name__ == '__main__':
    app.run(debug=True)
