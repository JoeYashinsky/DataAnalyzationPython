import os

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import sample
    app.register_blueprint(sample.bp)
    # app.add_url_rule('/', endpoint='index')

    from . import games
    app.register_blueprint(games.bp)
    # app.add_url_rule('/', endpoint='init')

    @app.route('/')
    def hello():
        return render_template('our_views/init.html')

    return app
