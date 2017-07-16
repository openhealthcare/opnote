"""
opnote - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/opnote/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/opnote/flow.js',
    ]