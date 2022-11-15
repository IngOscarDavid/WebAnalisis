#Librerias necesarias para el funcionamiento del proyecto
from flask import Flask, render_template, request, Response
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
import io

#Vector donde guardos los valores que se encuentran 
RL1 = []
RL2 = []
RL3 = []
RL4 = []
RL5 = []
RL6 = []
RL7 = []
RL8 = []
RL9 = []
RL10 = []
RL11 = []
RL12 = []


app = Flask(__name__)

#Método de extracción el cual redirecciona al usuario a la página principal ósea la index.html
@app.route("/")
def index():
    return render_template("index.html")

#Método de extracción el cual redirecciona al usuario a la página donde se pide que inserte los datos necesarios para el método y dar solución e este. 
@app.route("/ME", methods=["GET", "POST"])
# Funcion que toma y hace los calculos del metodo Euler
def ME():
    if request.method == "POST":
        try:
            #Limpiar los vectores
            RL1.clear()
            RL2.clear()
            RL3.clear()
            RL4.clear()
            # Funcion
            def Euler(Gx, X0, N, H):
                #Primeros calculos del metodo
                I = 0
                Xi = X0 + I * H
                Yi1 = Xf
                while I <= N:
                    #Se inserta los primeros resultados en los vectores
                    RL1.append(I)
                    RL3.append(Xi)
                    RL4.append(Yi1)
                    #Segundo calculos del metodo
                    Xi = X0 + I * H
                    Yi1 = Xf + H * (Xi-Yi1)
                    I = I + 1
                z = 0
                O = 0
                #Se hace las interacciones a la X con su respectivo indicador subjetivo
                while z <= N :
                    XI = "X" + str(O)
                    RL2.append(XI)
                    O = O + 1
                    z = z + 1
                #Se retorna los resultados en los vectores
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
            #Se llama la funcion del metodo y se le manda los datos capturados anteriormente
            Euler(Gx, X0, N, H)
        except ValueError:
            #En caso de que el usuario no inserte datos
            return "<head> <meta charset='UTF-8'> <meta http-equiv='X-UA-Compatible' content='IE=edge'> <meta name='viewport' content='width=device-width, initial-scale=1.0'> <title>Principal</title> <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi' crossorigin='anonymous'> <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3' crossorigin='anonymous'></script> </head> <body style='background-color: #ECDBF2; display: flex; justify-content: center;'><div style='justify-content: center; flex-direction: column;'><h1>Por Favor Ingrese Datos Validos</h1> <a href='/'><input type='button' class='btn btn-outline-success' value='Volver'></a> </div></body>"
        return render_template("resultado1.html", RL1=RL1, RL2= RL2, RL3= RL3, RL4= RL4) # Se manda las variables que contiene los datos

#Funcion para la Grafica 
@app.route('/GraficaE')
def dibuja_graficaE():
    # Se crea un dataset donde guardamos los vectores que queremos graficar
    df = pd.DataFrame({
        "X":RL3, 
        "Y":RL4
    })
    # Se define que tipo de grafica, tamaño
    df.plot(figsize=(10, 10), title='Gráfico', marker="o", x="X", y="Y")
    output = io.BytesIO()
    plt.legend()
    # Se crea una imagen para la grafica
    plt.savefig(output, format='png')
    # Se retorna la imagen con la grafica
    return Response(output.getvalue(), mimetype='image/png')

# Funcion que toma y hace los calculos del metodo Heun
@app.route("/MH", methods=["GET", "POST"])
#Método de extracción el cual redirecciona al usuario a la página donde se pide que inserte los datos necesarios para el método y dar solución e este. 
def MH():
    if request.method == "POST":
        try:
            # Se limpian los vector para no generar errores
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
                #Primeros calculos del metodo
                dydx = Gx(Xn, Yn)
                Dy = dydx * H
                Xnh = Xn + H
                YnD = Yn + Dy
                dydx1 = Gx(Xnh, YnD)
                P = (dydx + dydx1) / 2
                DC = P * H
                while I <= Xf:
                    #Se inserta los primeros resultados en los vectores
                    RL1.append(Xn)
                    RL2.append(Yn)
                    RL3.append(dydx)
                    RL4.append(Dy)
                    RL5.append(Xnh)
                    RL6.append(YnD)
                    RL7.append(dydx1)
                    RL8.append(P)
                    RL9.append(DC)
                    #Segundos calculos del metodo
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
            #En caso de que el usuario no inserte datos
            return "<head> <meta charset='UTF-8'> <meta http-equiv='X-UA-Compatible' content='IE=edge'> <meta name='viewport' content='width=device-width, initial-scale=1.0'> <title>Principal</title> <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi' crossorigin='anonymous'> <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3' crossorigin='anonymous'></script> </head> <body style='background-color: #ECDBF2; display: flex; justify-content: center;'><div style='justify-content: center; flex-direction: column;'><h1>Por Favor Ingrese Datos Validos</h1> <a href='/'><input type='button' class='btn btn-outline-success' value='Volver'></a> </div></body>"
        return render_template("resultado2.html", RL1=RL1, RL2= RL2, RL3= RL3, RL4= RL4, RL5= RL5, RL6= RL6, RL7= RL7, RL8= RL8, RL9=RL9)


@app.route('/GraficaH')
def dibuja_graficaH():
    # Se crea un dataset donde guardamos los vectores que queremos graficar
    df = pd.DataFrame({
        "X":RL1, 
        "Y":RL2
    })
    # Se define que tipo de grafica, tamaño
    df.plot(figsize=(10, 10), title='Gráfico', marker="o", x="X", y="Y")
    output = io.BytesIO()
    plt.legend()
    # Se crea una imagen para la grafica
    plt.savefig(output, format='png')
    # Se retorna la imagen con la grafica
    return Response(output.getvalue(), mimetype='image/png')

#Método de extracción el cual redirecciona al usuario a la página donde se pide que inserte los datos necesarios para el método y dar solución e este. 
@app.route("/MR", methods=["GET", "POST"])
# Funcion que toma y hace los calculos del metodo Ruge
def MR():
    if request.method == "POST":
        try:
            # Se limpian los vector para no generar errores
            RL1.clear()
            RL2.clear()
            RL3.clear()
            RL4.clear()
            RL5.clear()
            RL6.clear()
            RL7.clear()
            RL8.clear()
            RL9.clear()
            RL10.clear()
            RL11.clear()
            RL12.clear()

            # Funcion
            def Euler(Gx, X0, Y0, Xf, H):
                I = 0
                float (I)
                #Primeros calculos del metodo
                K1 = Gx(X0, Y0)
                XH2 = X0 + (H/2)
                YK1H2 = Y0 + K1 * (H/2)
                K2 = Gx(XH2, YK1H2)
                XH22 = X0 + (H/2)
                YK2H2 = Y0 + K2 * (H/2)
                K3 = Gx(XH2, YK2H2)
                XH = X0 + H
                YK3H = Y0 + K3 * H
                K4 = Gx(XH, YK3H)

                while I <= Xf:
                    #Se inserta los primeros resultados en los vectores
                    RL1.append(X0)
                    RL2.append(Y0)
                    RL3.append(K1)
                    RL4.append(XH2)
                    RL5.append(YK1H2)
                    RL6.append(K2)
                    RL7.append(XH22)
                    RL8.append(YK2H2)
                    RL9.append(K3)
                    RL10.append(XH)
                    RL11.append(YK3H)
                    RL12.append(K4)
                    #Segundos calculos del metodo
                    X0 = X0 + H
                    Y0 = Y0 +(H/26)*(K1 + 2*K2 + 2*K3 + K4)
                    K1 = Gx(X0, Y0)
                    XH2 = X0 + (H/2)
                    YK1H2 = Y0 + K1 * (H/2)
                    K2 = Gx(XH2, YK1H2)
                    XH22 = X0 + (H/2)
                    YK2H2 = Y0 + K2 * (H/2)
                    K3 = Gx(XH2, YK2H2)
                    XH = X0 + H
                    YK3H = Y0 + K3 * H
                    K4 = Gx(XH, YK3H)

                    I = I + H
                return (RL1, RL2, RL3, RL4, RL5, RL6, RL7, RL8, RL9, RL10, RL11, RL12)

            # Asignacion De valor
            X0 = float(request.form["T11"])
            Y0 = float(request.form["T12"])
            Xf = float(request.form["T13"])
            H = float(request.form["T14"])
            G = request.form["T15"]

            # Guardar la funcion
            x = sp.symbols("x")
            y = sp.symbols("y")
            Gx = sp.lambdify([x, y], G)

            Euler(Gx, X0, Y0, Xf, H)
        except ValueError:
            #En caso de que el usuario no inserte datos
            return "<head> <meta charset='UTF-8'> <meta http-equiv='X-UA-Compatible' content='IE=edge'> <meta name='viewport' content='width=device-width, initial-scale=1.0'> <title>Principal</title> <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi' crossorigin='anonymous'> <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3' crossorigin='anonymous'></script> </head> <body style='background-color: #ECDBF2; display: flex; justify-content: center;'><div style='justify-content: center; flex-direction: column;'><h1>Por Favor Ingrese Datos Validos</h1> <a href='/'><input type='button' class='btn btn-outline-success' value='Volver'></a> </div></body>"
        return render_template("resultado3.html", RL1=RL1, RL2= RL2, RL3= RL3, RL4= RL4, RL5= RL5, RL6= RL6, RL7= RL7, RL8= RL8, RL9=RL9, RL10= RL10, RL11= RL11, RL12= RL12)


@app.route('/GraficaR')
def dibuja_graficaR():
    # Se crea un dataset donde guardamos los vectores que queremos graficar
    df = pd.DataFrame({
        "X":RL1, 
        "Y":RL2
    })
    # Se define que tipo de grafica, tamaño
    df.plot(figsize=(10, 10), title='Gráfico', marker="o", x="X", y="Y")
    output = io.BytesIO()
    plt.legend()
    # Se crea una imagen para la grafica
    plt.savefig(output, format='png')
    # Se retorna la imagen con la grafica
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
