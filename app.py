from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola mundo desde Flask y Render! Y desde mi casa'

if __name__ == '__main__':
    app.run(debug=True)
