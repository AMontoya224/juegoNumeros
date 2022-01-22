from flask import Flask, render_template, redirect, session, request
import random 

app = Flask(__name__)
app.secret_key = "estoessecreto"

@app.route( '/', methods=['GET'] )
def paginaInicio():
    global numero
    numero = random.randint(1, 100)
    return render_template( "index.html")

@app.route( '/guess', methods=['POST'] )
def paginaAdivinar():
    valor = {
        "numeroAdivinado" : int(request.form["numeroAdivinado"])
    }
    session["numeroAdivinado"] = request.form["numeroAdivinado"]

    if valor["numeroAdivinado"] < numero:
        return render_template( "incorrecto.html", palabra="bajo")
    elif valor["numeroAdivinado"] > numero:
        return render_template( "incorrecto.html", palabra="alto")
    else:
        return render_template( "correcto.html", palabra=numero)


@app.route( '/again', methods=["POST"] )
def resetearContador():
    session.clear()
    return redirect( '/' )

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"

if __name__ == "__main__":
    app.run(debug=True)