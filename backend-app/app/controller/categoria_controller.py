from flask import request
from flask_restx import Resource

from app.util.dto import CategoriaDto
from app.service.categoria_service import editar_categoria, excluir_categoria, listar_todas_categorias, criar_categoria

api = CategoriaDto.api
_categoria = CategoriaDto.categoria

@api.route('/')
class Categoria(Resource):
    def post(self):
        data = request.json
        return criar_categoria(data)

    @api.marshal_list_with(_categoria, envelope='data')
    def get(self):
        return listar_todas_categorias()


@api.route('/<id_categoria>')
@api.param('id_categoria', 'id da categoria')
class CategoriaComId(Resource):
    def put(self, id_categoria):
        data = request.json
        return editar_categoria(id_categoria, data)

    def delete(self, id_categoria):
        return excluir_categoria(id_categoria)