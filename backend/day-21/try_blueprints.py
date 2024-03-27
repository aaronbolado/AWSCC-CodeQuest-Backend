from flask import Flask, Blueprint

app = Flask(__name__)

main_blueprint = Blueprint('main',__name__)

@main_blueprint.route('/')
def home():
    return "Welcome to the home page"

@main_blueprint.route('/about')
def about():
    return "This is the about page"

# Tell the flask app that this blueprint is included in the main app
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()