import dataset


class Banco:
    def list_jogos(self):
        with dataset.connect('sqlite:///apijogos.db') as db:
            jogos = db['jogos'].all()
            if db['jogos'].count() > 0:
                listajogos = [dict(id=data['id'], nome=data['nome'], plataforma=data['plataforma'], preco=data['preco']) for data in
                              jogos]
                return listajogos
            else:
                return False

    def save_jogo(self, data):
        with dataset.connect('sqlite:///apijogos.db') as db:
            return db['jogos'].insert(dict(nome=data['nome'], plataforma=data['plataforma'], preco=data['preco']))

    def get_jogo(self, id):
        with dataset.connect('sqlite:///apijogos.db') as db:
            jogo = db['jogos'].find_one(id=id)
            if jogo:
                return jogo
            else:
                return False

    def update_jogo(self, id, data):
        with dataset.connect('sqlite:///apijogos.db') as db:
            return db['jogos'].update(
                dict(id=id, nome=data['nome'], plataforma=data['plataforma'], preco=data['preco']), ['id'])

    def delete_jogo(self, id):
        with dataset.connect('sqlite:///apijogos.db') as db:
            return db['jogos'].delete(id=id)
