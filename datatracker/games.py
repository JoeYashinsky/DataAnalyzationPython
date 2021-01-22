from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests
import json
from types import SimpleNamespace

bp = Blueprint('our_views', __name__)


@bp.route('/init', methods=['GET'])
def get_games():
    response = requests.get('https://api.dccresource.com/api/games')
    games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
    games = json.load()
    return render_template()


