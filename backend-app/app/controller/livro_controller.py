from flask import request
from flask_restx import Resource

from app.util.dto import LivroDto
from app.service.livro_service import editar_livro, excluir_livro, listar_todas_livros, criar_livro

api = LivroDto.api
_livro = LivroDto.livro

@api.route('/')
class Livro(Resource):
    def post(self):
        data = request.json
        return criar_livro(data)

    @api.marshal_list_with(_livro, envelope='data')
    def get(self):
        return listar_todas_livros()


@api.route('/<id_livro>')
@api.param('id_livro', 'id da livro')
class LivroComId(Resource):
    def put(self, id_livro):
        data = request.json
        return editar_livro(id_livro, data)

    def delete(self, id_livro):
        return excluir_livro(id_livro)