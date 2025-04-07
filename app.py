from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    valores = []

    if request.method == 'POST':
        try:
            valores = [float(request.form[f'num{i}']) for i in range(1, 4)]

            if 'sumar' in request.form:
                resultado = sum(valores)
            elif 'duplicar' in request.form:
                resultado = [v * 2 for v in valores]
        except ValueError:
            resultado = "Por favor, introduce solo números válidos."

    return render_template('index.html', resultado=resultado, valores=valores)
