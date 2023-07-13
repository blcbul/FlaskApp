from flask import Blueprint, render_template

error_views = Blueprint('error', __name__)

@error_views.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
