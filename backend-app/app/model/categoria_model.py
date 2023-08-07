from app import db

class Categoria(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "categoria"

    # TODAS AS TABELAS TEM ESSA COLUNA
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nome = db.Column(db.String(255), unique=True, nullable=False)

    livros = db.relationship('Livro', back_populates='categoria', uselist=True)

    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return "<Categoria '{}'>".format(self.nome)
