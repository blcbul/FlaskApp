from flask import (Flask, render_template, request, redirect, url_for, flash )

#Imports from DB
from db.categories import Category 

#Imports from Forms
from forms.category_forms import CreateCategory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/saludo/<name>")
def saludo(name):
    user = 'admin'
    return render_template('saludo.html', name=name, user=user)

@app.route("/drinks")
def drinks():
    drinks = ["agua", "jugo", "limonada", "coca", "sprite"]
    return render_template('drinks.html', drinks=drinks)

@app.route('/categories/')
def categories():
    cats = Category.get_all()
    return render_template('categories.html', cats=cats)

@app.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    form = CreateCategory()
    if form.validate_on_submit():
        category = form.category.data
        description = form.decription.data
        cat = category(category, description)
        cat.save()
        return redirect(url_for('categories'))
    return render_template('create_cat.html', form=form)

@app.route('/categories/<int:id>/update/')
def update_cat(id):
    return f"Vamos a editar con id { id }"

@app.route('/categories/<int:id>/delete/')
def delete_cat(id):
    cat = Category.get(id)
    cat.delete()
    return redirect(url_for('categories'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)