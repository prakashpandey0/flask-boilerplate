from flask import render_template, Blueprint, url_for, flash, redirect


core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('base.html')
