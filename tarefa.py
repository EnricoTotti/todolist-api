from flask import jsonify


def buscar_tarefas():
    tarefas = [
        {
            'id': 1,
            'nome': 'Aprender digitação',
            'descricao': 'Vamos Aumentar o zoom para não errar a digitação',
            'status': 'Pendente'
        },
        {
            'id': 2,
            'nome': 'Aprender Python',
            'descricao': 'Aprender python para programar JSON',
            'status': 'Pendente'
        }
    ]

    return jsonify(tarefas)