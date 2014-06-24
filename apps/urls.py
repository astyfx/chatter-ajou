"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from apps import app
from apps import views

# Home page
app.add_url_rule('/', 'home', view_func=views.home, methods=['GET'])
app.add_url_rule('/login', 'login', view_func=views.login, methods=['GET', 'POST'])
app.add_url_rule('/join', 'join', view_func=views.join, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', view_func=views.logout, methods=['GET', 'POST'])

app.add_url_rule('/send_message', 'send_message', view_func=views.send_message, methods=['POST'])

# # Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500