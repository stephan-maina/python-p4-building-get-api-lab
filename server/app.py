#!/usr/bin/env python3

from flask import Flask, jsonify
from models import db, Book, Team

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/players', methods=['GET'])
def get_players():
    players = Book.query.all()
    player_list = [player.to_dict() for player in players]
    return jsonify(player_list)

@app.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    team_list = [team.to_dict() for team in teams]
    return jsonify(team_list)

if __name__ == '__main__':
    app.run(debug=True)
