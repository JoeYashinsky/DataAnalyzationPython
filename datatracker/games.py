from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint

import requests

import json


bp = Blueprint('our_views', __name__)


@bp.route('/init', methods=['GET'])
def get_global_sales():
    list_games = []
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()
    for game in games:
        game_year = game['year']
        if game_year is not None:
            if game_year >= 2013:
                list_games.append(game)
    return render_template('our_views/init.html', list_games=list_games, response=response)

