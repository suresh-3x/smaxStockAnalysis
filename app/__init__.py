from flask import Flask

app = Flask(__name__)

from app.routes.stocks import index