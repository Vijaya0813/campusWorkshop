"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr63orddl9mmoi2u30-a.oregon-postgres.render.com",
        database="todo_twqs",
        user="root",
        password="p5cqac9AagBTg15SGdnQI5p1tM4Mz45V")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
