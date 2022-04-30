from flask import Blueprint, jsonify, make_response, request
from flask_httpauth import HTTPBasicAuth
from banco import Banco

bp_api = Blueprint('api', __name__, url_prefix='/jogos/api/vi/lista')
banco = Banco()

# Manage the User
auth = HTTPBasicAuth()


@auth.get_password
def verificar_acesso(username):
    if username == 'diego':  # YOUR USERNAME AND PASSWORD
        return '123'
    return None


@auth.error_handler
def acesso_negado():
    return make_response(jsonify({'error': 'Acesso negado!'}), 403)  # esse para acesso negado


lista = []


@bp_api.route('/', methods=['GET'])
@bp_api.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_games(id=None):
    lista = banco.list_jogos()
    if lista is not False:
        if id is not None:
            lista = banco.get_jogo(id)
            return jsonify({'lista': lista})
        return jsonify({'lista': lista})
    return make_response(jsonify({'error': 'Nenhum dado encontrado!'}), 404)


@bp_api.route('/add/', methods=['POST'])
@auth.login_required
def add_games():
    if request.json:
        banco.save_jogo(request.json[0])

        #  If doesnt have DB
        # lista.append(
        #     {'id': len(lista) + 1,
        #      'Plataforma': request.json[0]['Plataforma'],
        #      'Nome': request.json[0]['Nome'],
        #      'Preco': request.json[0]['Preco']
        #      })
    return make_response(jsonify({'Mensagem': 'Dados inseridos com sucesso!'}), 200)


@bp_api.route('/alter/<int:id>', methods=['PUT'])
@auth.login_required
def put_games(id=None):
    if request.json and id is not None:
        banco.update_jogo(id, request.json[0])

        #  If doesnt have DB
        # lista[(id - 1)]['Plataforma'] = request.json[0]['Plataforma']
        # lista[(id - 1)]['Nome'] = request.json[0]['Nome']
        # lista[(id - 1)]['Preco'] = request.json[0]['Preco']
    return make_response(jsonify({'Mensagem': 'Dados alterados com sucesso!'}), 200)


@bp_api.route('/del/<int:id>', methods=['DELETE'])
@auth.login_required
def del_games(id=None):
    if id is not None:
        banco.delete_jogo(id)
        # lista.pop(id - 1)
    return make_response(jsonify({'Mensagem': 'Dados do id {} foi excluido com sucesso!'.format(id)}), 200)
    # return jsonify({'lista': lista})


@bp_api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'URL nao encontrada!'}), 404)

#TESTED WITH POSTMAN
