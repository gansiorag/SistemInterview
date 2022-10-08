from flask import Flask

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

tsession={"regim":'0',
          "rul":'0'}

from app.controllers import rootFirst