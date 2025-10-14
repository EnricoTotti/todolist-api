from flask import Flask #importando biblioteca flask

app = Flask(__name__) #cria um objeto da classe flask

@app.route('/api', methods=['GET']) #rota do objeto

def index():
    return {
        'message': 'Api Rodando'
    }

#se for o modulo principal roda o projeto em debug
if __name__ == '__main__':
    app.run(debug=True)