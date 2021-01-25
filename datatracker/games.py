from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint

import requests

import json

bp = Blueprint('our_views', __name__)


@bp.route('/init', methods=['GET'])
def get_games():
    list_games = []
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()

    for game in games:
        game_year = game['year']
        if game_year is not None:
            if game_year >= 2013:
                list_games.append(game)

    return render_template('our_views/init.html', list_games=list_games, response=response)


@bp.route('/globalSales', methods=['GET'])
def global_sales():
    list_games = []
    list_platforms = []
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()

    for game in games:
        game_year = game['year']
        if game_year is not None:
            if game_year >= 2013:
                list_games.append(game)

    for game in list_games:
        platform = game['platform']
        if platform is not None:
            if platform not in list_platforms:
                list_platforms.append(platform)

    global_values = [sub['globalSales'] for sub in list_games]

    return render_template('our_views/globalSales.html', list_games=list_games, list_platforms=list_platforms, global_values=global_values, response=response)


@bp.route('/namedgames', methods=['GET'])
def get_games_by_name():
    game_names = []
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()

    for game in games:
        game_name = game['name']
        if game_name is not None:
            game_names.append(game_name)

    return render_template('our_views/namedgames.html', game_names=game_names, response=response)


@bp.route('/init', methods=['GET'])
def copies_sold():
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()['items']

    for game in games:
        return game['platform']

    copies = copies_sold()
    games_sold = [copy for copy in copies if copy['platform'] is not None and copy['globalSales'] is not None]

    return render_template('our_views/init.html', response=response)