import collections
import operator
import functools
from collections import defaultdict
from types import SimpleNamespace
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
    global_val = defaultdict(int)
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()
    games_dct = response.content
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

    #get global sales from the api (games)
    #iterate thru dataset
    #if comparison == platform, then add global sales to the value of global_values

    for game in games:
        global_stuff = 0
        for key in global_values:
            if game['platform'] == global_values[key]:
                global_values[key] += game['globalSales']
                global_values.update(global_stuff)


    #for game in games:
     #   for key in global_values:
      #      if game['platform'] in global_values.keys():
       #         global_values[key] += game['globalSales']

    return render_template('our_views/globalSales.html', list_games=list_games,
                           list_platforms=list_platforms, global_values=global_values,
                           response=response)


@bp.route('/namedGames', methods=('GET', 'POST'))
def search_for_game():
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()
    found_game = []

    if request.method == 'POST':
        searched_game = request.form['title']
        error = None

    for game in games:
        if game is not None:
            if game['name'] == searched_game:
                found_game.append(game)

    return render_template('our_views/namedGames.html', found_game=found_game, searched_game=searched_game,
                           response=response)


#@bp.route('/init', methods=['GET'])
#def copies_sold():
 #   response = requests.get('https://api.dccresource.com/api/games')
  #  games = response.json()['items']

   # for game in games:
    #    return game['platform']

    #copies = copies_sold()
    #games_sold = [copy for copy in copies if copy['platform'] is not None and copy['globalSales'] is not None]

    #return render_template('our_views/init.html', response=response)
