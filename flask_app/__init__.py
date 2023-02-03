from flask import Flask
from flask_app.home.views import home_bp
from flask_app.dash_app import init_dash



def init_flask():
    app = Flask(__name__, instance_relative_config=False)
    
    
    with app.app_context():
        app.register_blueprint(home_bp)
        init_dash(app)
        return app
        