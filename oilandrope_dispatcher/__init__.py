import logging

from flask import Flask

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
