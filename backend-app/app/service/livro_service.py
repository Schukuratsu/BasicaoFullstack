from app.model.livro_model import Livro
from app.extensions import db


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def criar_livro(data):
    livro = Livro(
        titulo=data['titulo'],
        autor=data['autor'],
        ano_publicacao=data['ano_publicacao'],
        id_categoria=data['id_categoria'],
    )
    save_changes(livro)
    return { "id": livro.id }


def listar_todas_livros():
    return Livro.query.all()

def editar_livro(id, data):
    livro = Livro.query.get(id)

    livro.titulo = data['titulo']
    livro.autor = data['autor']
    livro.ano_publicacao = data['ano_publicacao']
    livro.id_categoria = data['id_categoria']
    
    save_changes(livro)
    return { "id": livro.id }

def excluir_livro(id):
    livro = Livro.query.get(id)
    db.session.delete(livro)
    db.session.commit()
    return { "id": livro.id }