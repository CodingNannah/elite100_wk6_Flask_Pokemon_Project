from flask import Flask


app = Flask(__name__)
    
@app.route('/')
def index():
    return "Not sure what this will become, right now."

# flask run Error: Failed to find Flask application or factory in module 'app'. Use 'app:name' to specify one.

# Stack Overflow suggested fix:
# def create_app():
#     app - Flask(__name__)
#     @app.route('/')
#     def app_working():
#         return "Let's see if this app is working!"
#     return app
# app = create_app()

# app = Flask(__name__)
    

