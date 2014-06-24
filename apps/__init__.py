"""
Initialize Flask app

"""
from flask import Flask
import os

import pusher

app = Flask('apps')
app.config.from_object('apps.settings.Test')


# pusher instance
pi = pusher.Pusher(
    app_id='79133',
    key='1c903b586c466374d972',
    secret='3c225b62987621c41c4e'
)

# Pull in URL dispatch routes
import urls