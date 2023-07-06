from flask import Flask, render_template

app = Flask(__name__)

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
  
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)