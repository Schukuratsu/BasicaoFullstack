from app import db

class Livro(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "livro"

    # TODAS AS TABELAS TEM ESSA COLUNA
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    titulo = db.Column(db.String(255), unique=True, nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    ano_publicacao = db.Column(db.Integer, nullable=False)

    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    categoria = db.relationship('Categoria', foreign_keys=[id_categoria], back_populates='livros', uselist=False)

    def __init__(self, titulo, autor, ano_publicacao, id_categoria):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.id_categoria = id_categoria
        
    def __repr__(self):
        return "<Livro '{}'>".format(self.titulo)
