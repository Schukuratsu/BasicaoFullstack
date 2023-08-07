from flask_restx import Namespace, fields


class CategoriaDto:
    api = Namespace('categoria', description='categoria')
    categoria = api.model('categoria', {
        'id': fields.Integer(),
        'nome': fields.String(required=True)
    })

class LivroDto:
    api = Namespace('livro', description='livro')
    livro = api.model('livro', {
        'id': fields.Integer(),
        'titulo': fields.String(required=True),
        'autor': fields.String(required=True),
        'ano_publicacao': fields.String(required=True),
        'id_categoria': fields.Integer(required=True),
    })