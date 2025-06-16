from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import plotly
import plotly.express as px
import json
from sklearn.datasets import load_iris

app = Flask(__name__)

# Memuat model dan scaler
knn_model = joblib.load('model/knn_model.pkl')
scaler = joblib.load('model/scaler.pkl')
iris = load_iris()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Mengambil input dari form
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Menyiapkan data untuk prediksi
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    input_scaled = scaler.transform(input_data)

    # Melakukan prediksi
    prediction = knn_model.predict(input_scaled)[0]
    probabilities = knn_model.predict_proba(input_scaled)[0]

    # Membuat grafik menggunakan plotly
    fig = px.bar(
        x=iris.target_names,
        y=probabilities * 100,
        labels={'x': 'Jenis Bunga', 'y': 'Probabilitas (%)'},
        title='Probabilitas Prediksi Jenis Bunga Iris'
    )
    fig.update_layout(
        template='plotly_white',
        title_x=0.5,
        title_font_size=20
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('result.html', 
                         prediction=iris.target_names[prediction],
                         probabilities=probabilities,
                         graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True) 