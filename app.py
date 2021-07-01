from flask import Flask, request, render_template
from Paskola import Paskola
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        suma = request.form['suma']
        terminas = request.form['terminas']
        palukanos = request.form['palukanos']
        return render_template("home.html", suma=suma, terminas=terminas, palukanos=palukanos)
    else:
        return render_template("form.html")

@app.route("/home", methods=['POST'])
def grafikas():
    Paskola.mokejimo_grafikas()



if __name__ == "__main__":
    app.run()