from app.model.categoria_model import Categoria
from app.extensions import db


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def criar_categoria(data):
    nova_categoria = Categoria(
        nome=data['nome'],
    )
    save_changes(nova_categoria)
    return { "id": nova_categoria.id }


def listar_todas_categorias():
    return Categoria.query.all()

def editar_categoria(id, data):
    categoria = Categoria.query.get(id)
    categoria.nome = data['nome']
    save_changes(categoria)
    return { "id": categoria.id }

def excluir_categoria(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return { "id": categoria.id }