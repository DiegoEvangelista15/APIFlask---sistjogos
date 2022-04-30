from flask import Flask
from api import bp_api

app = Flask(__name__)
app.register_blueprint(bp_api)
# Utilize a comunicacao padrao!!

app.run(debug=True)
