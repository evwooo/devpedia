from flask import Blueprint, jsonify
import os, json

main = Blueprint('main', __name__)

@main.route('/api/git')
def git_cheats():
    path = os.path.join(os.path.dirname(__file__), 'cheatsheets', 'git.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)
