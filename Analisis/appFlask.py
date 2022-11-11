from flask import Flask, render_template, request, Response
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
import io

#Diccionario y lista 
RL1 = []
RL2 = []
RL3 = []
RL4 = []
RL5 = []
RL6 = []
RL7 = []
RL8 = []
RL9 = []

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/ME", methods=["GET", "POST"])
def ME():
    if request.method == "POST":
        try:
            RL1.clear()
            RL2.clear()
            RL3.clear()
            RL4.clear()
            # Funcion
            def Euler(Gx, X0, N, H):
                I = 0
                Xi = X0 + I * H
                Yi1 = Xf
                while I <= N:
                    RL1.append(I)
                    RL3.append(Xi)
                    RL4.append(Yi1)
                    Xi = X0 + I * H
                    Yi1 = Xf + H * (Xi-Yi1)
                    I = I + 1
                z = 0
                O = 0
                while z <= N :
                    XI = "X" + str(O)
                    RL2.append(XI)
                    O = O + 1
                    z = z + 1
                return (RL1, RL2, RL3, RL4)

            # Asignacion De valor
            X0 = float(request.form["T01"])
            Xf = float(request.form["T02"])
            N = float(request.form["T03"])
            H = float(request.form["T04"])
            G = request.form["T05"]

            # Guardar la funcion
            x = sp.symbols("x")
            y = sp.symbols("y")
            Gx = sp.lambdify([x, y], G)

            Euler(Gx, X0, N, H)
        except ValueError:
            return "<body style='background-color: #ECDBF2;'><div style='justify-content: center; display: flex;'><h1>Por Favor Ingrese Datos Validos</h1></div></body>"
        return render_template("resultado1.html", RL1=RL1, RL2= RL2, RL3= RL3, RL4= RL4)


@app.route('/GraficaE')
def dibuja_graficaE():
    df = pd.DataFrame({
        "X":RL3, 
        "Y":RL4
    })
    df.plot(figsize=(10, 10), title='Gráfico', marker="o", x="X", y="Y")
    output = io.BytesIO()
    plt.legend()
    plt.savefig(output, format='png')
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/MH", methods=["GET", "POST"])
def MH():
    if request.method == "POST":
        try:
            RL1.clear()
            RL2.clear()
            RL3.clear()
            RL4.clear()
            RL5.clear()
            RL6.clear()
            RL7.clear()
            RL8.clear()
            RL9.clear()
            # Funcion
            def Euler(Gx, Xn, Yn, Xf, H):
                I = 0
                float (I)
                dydx = Gx(Xn, Yn)
                Dy = dydx * H
                Xnh = Xn + H
                YnD = Yn + Dy
                dydx1 = Gx(Xnh, YnD)
                P = (dydx + dydx1) / 2
                DC = P * H
                while I <= Xf:
                    RL1.append(Xn)
                    RL2.append(Yn)
                    RL3.append(dydx)
                    RL4.append(Dy)
                    RL5.append(Xnh)
                    RL6.append(YnD)
                    RL7.append(dydx1)
                    RL8.append(P)
                    RL9.append(DC)

                    Xn = Xn + H
                    Yn = Yn + DC
                    dydx = Gx(Xn, Yn)
                    Dy = dydx * H
                    Xnh = Xn + H
                    YnD = Yn + H
                    dydx1 = Gx(Xnh, YnD)
                    P = (dydx + dydx1 ) / 2
                    DC = P * H
                    I = I + H
                return (RL1, RL2, RL3, RL4, RL5, RL6, RL7, RL8, RL9)

            # Asignacion De valor
            Xn = float(request.form["T06"])
            Yn = float(request.form["T07"])
            Xf = float(request.form["T08"])
            H = float(request.form["T09"])
            G = request.form["T10"]

            # Guardar la funcion
            x = sp.symbols("x")
            y = sp.symbols("y")
            Gx = sp.lambdify([x, y], G)

            Euler(Gx, Xn, Yn, Xf, H)
        except ValueError:
            return "<body style='background-color: #ECDBF2;'><div style='justify-content: center; display: flex;'><h1>Por Favor Ingrese Datos Validos</h1></div></body>"
        return render_template("resultado2.html", RL1=RL1, RL2= RL2, RL3= RL3, RL4= RL4, RL5= RL5, RL6= RL6, RL7= RL7, RL8= RL8, RL9=RL9)


@app.route('/GraficaH')
def dibuja_graficaH():
    df = pd.DataFrame({
        "X":RL1, 
        "Y":RL2
    })
    df.plot(figsize=(10, 10), title='Gráfico', marker="o", x="X", y="Y")
    output = io.BytesIO()
    plt.legend()
    plt.savefig(output, format='png')
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
