import json

from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import json
from datatracker.api_data import games


bp = Blueprint('sample', __name__)


@bp.route('/test')
def test():
    with open('games.txt', "w") as json_file:
        json.dump(games, json_file, indent=4, sort_keys=True)


@bp.route('/sample')
def index():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)


@bp.route('/postform', methods=('GET', 'POST'))
def other_example():
    if request.method == 'POST':
        page_title = request.form['title']
        error = None

        if not page_title:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        elif request.form['title'] == "go home":
            return redirect(url_for('sample.index'))
        else:
            return render_template('sample/postform.html', page_title=page_title)

    else:
        return render_template('sample/postform.html', page_title="PostForm from Module Function")


