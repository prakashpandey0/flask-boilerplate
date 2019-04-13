from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##############################################
############### DATABASE #####################
##############################################




from push.core.views import core
app.register_blueprint(core)

from push.campaign.views import campaign
app.register_blueprint(campaign)
