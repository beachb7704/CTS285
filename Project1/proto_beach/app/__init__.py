from flask import Flask

from config import Config


# This is the Flask application factory function
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

   
   
    # Initialize Flask extensions here

    
    
    # Register blueprints here
    # This is for all of the folders that are created with an __init__.py file to go with it
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.memory_bank import bp as memory_bank_bp
    app.register_blueprint(memory_bank_bp, url_prefix='/memory_bank')
    
    from app.answer_checker import bp as answer_checker_bp
    app.register_blueprint(answer_checker_bp, url_prefix='/answer_checker')
    
    

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    
    
    return app