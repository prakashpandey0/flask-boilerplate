from flask import render_template, Blueprint, flash, url_for

campaign = Blueprint('campaign',__name__)

@campaign.route('/campaign')
def index():
    return "hey"
