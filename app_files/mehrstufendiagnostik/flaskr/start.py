# -*- coding: utf-8 -*-
import os

import datetime
from flask import Flask


def create_app():
    test_config=None

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    import mehrstufendiagnostik.flaskr.blog

    app.register_blueprint(mehrstufendiagnostik.flaskr.blog.bp)
    app.add_url_rule('/', endpoint='index')

    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=30)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

