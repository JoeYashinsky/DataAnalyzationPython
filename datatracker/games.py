import collections
import math
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests
import json


bp = Blueprint('our_views', __name__)


@bp.route('/init', methods=['GET'])
def get_games():
    list_games = []
    list_years = []
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
    print(games)

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

    global_values = dict.fromkeys(list_platforms, 0)
    print(global_values)

    for game in games:

        for item in global_values:
            if game['platform'] == item:
                global_values[item] += math.trunc(game['globalSales'])

    return render_template('our_views/globalSales.html', list_games=list_games,
                           list_platforms=list_platforms, global_values=global_values,
                           response=response)


# How many copies of each game per console were sold in North America?


@bp.route('/naSales', methods=(['GET']))
def na_sales_games():
    list_games = []
    list_platforms = []
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()

    for game in games:
        platform = game['platform']
        if platform is not None:
            if platform not in list_platforms:
                list_platforms.append(platform)

    global_values = dict.fromkeys(list_platforms, 0)
    for game in games:
        for item in global_values:
            if game['platform'] == item:
                global_values[item] += math.trunc(game['naSales'])
    return render_template('our_views/naSales.html', list_games=list_games, list_platforms=list_platforms,
                           global_values=global_values, response=response)


@bp.route('/namedGames', methods=('GET', 'POST'))
def search_for_game():
    response = requests.get('https://api.dccresource.com/api/games')
    searched_game = ''
    games = response.json()
    list_platforms = []
    found_game = []

    if request.method == 'POST':
        searched_game = request.form['title']
        error = None

    for game in games:
        if game is not None:
            if game['name'] == searched_game:
                found_game.append(game)

    # display chart repping #of copies sold per platform
    # iterate through games
    # if game[name] == searched_game
    # iterate through global_values
    # global_values[key] += game[globalSales]

    for game in games:
        platform = game['platform']
        if platform is not None:
            if platform not in list_platforms:
                list_platforms.append(platform)

    global_values = dict.fromkeys(list_platforms, 0)
    for game in games:
        # if game['name'] == searched_game:
        for item in global_values:
            if game['platform'] == item and game['name'] == searched_game:
                global_values[item] += game['globalSales']

    return render_template('our_views/namedGames.html', global_values=global_values, found_game=found_game,
                           searched_game=searched_game, list_platforms=list_platforms, response=response)






