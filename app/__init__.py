from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "12323546546546sssf"

from app.routes.stocks import index