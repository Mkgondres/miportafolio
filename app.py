from flask import Flask, render_template
from proyectos import LISTA_PROYECTOS

app = Flask(__name__)

@app.route("/")
def inicio():
    # Toma la lista de 'proyectos.py' y la envía al 'index.html'
    return render_template("index.html", proyectos=LISTA_PROYECTOS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

