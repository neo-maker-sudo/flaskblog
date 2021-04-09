from flask import Blueprint, render_template, url_for

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def error_404(error):
    image_file = url_for('static', filename='errors_pics/404-error.jpg')
    return render_template('errors/404.html', image_file=image_file), 404

@errors.app_errorhandler(403)
def error_403(error):
    image_file = url_for('static', filename='errors_pics/403-Error.jpg')
    return render_template('errors/403.html', image_file=image_file), 403

@errors.app_errorhandler(500)
def error_500(error):
    image_file = url_for('static', filename='errors_pics/500-Error.jpg')
    return render_template('errors/500.html', image_file=image_file), 500
