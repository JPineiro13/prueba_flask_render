from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Cargar modelo y el imputador
model = joblib.load('model.pkl')
imputer = joblib.load('imputer.pkl')

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Obtener los 9 valores del formulario
            values = [
                float(request.form.get('max_temp')),
                float(request.form.get('mean_temp')),
                float(request.form.get('min_temp')),
                float(request.form.get('max_hum')),
                float(request.form.get('mean_hum')),
                float(request.form.get('min_hum')),
                float(request.form.get('max_wind')),
                float(request.form.get('mean_wind')),
                float(request.form.get('precip')),
            ]

            # Convertir y preparar para el modelo
            X_input = np.array(values).reshape(1, -1)
            X_input_imputed = imputer.transform(X_input)
            prediction = model.predict(X_input_imputed)[0]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)
