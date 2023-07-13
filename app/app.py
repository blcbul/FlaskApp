from flask import Flask
#Imports from DB


#Imports from Forms

from views.home_views import home_views

from views.error_views import error_views

from views.category_views import category_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

app.register_blueprint(home_views)

app.register_blueprint(category_views)

app.register_blueprint(error_views)


if __name__ == '__main__':
    app.run(debug=True)