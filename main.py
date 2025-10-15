from flask import Flask #importando biblioteca flask

from tarefa import buscar_tarefas, buscar_tarefa

app = Flask(__name__) #cria um objeto da classe flask

@app.route('/api', methods=['GET']) #rota do objeto

def index():
    return {
        'message': 'Api Rodando'
    }

@app.route('/api/tarefas', methods=['GET'])

def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

@app.route('/api/tarefa', methods=['GET'])

def get_tarefa():
    tarefa = buscar_tarefa()
    return tarefa

#se for o modulo principal roda o projeto em debug
if __name__ == '__main__':
    app.run(debug=True)