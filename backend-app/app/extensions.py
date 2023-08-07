from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
api = Api(title='Basicão Fullstack',
          version='1.0',
          description='API braba 🔥',
          )