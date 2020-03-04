from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(191), nullable=False)
    email = db.Column(db.String(191), unique=True,  nullable=False)
    senha = db.Column(db.String(191),  nullable=False)
    admin = db.Column(db.Boolean,  nullable=False)

    def __repr__(self):
        return '< Usuario: %s >' % self.nome

class Atividade(db.Model):
    __tablenome__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(191),  nullable=False)
    tipo = db.Column(db.String(191),  nullable=False)
    data = db.Column(db.DateTime,  nullable=False)
    carga_horaria = db.Column(db.Float,  nullable=False)
    arquivo = db.Column(db.String(191),  nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'),  nullable=False)

    def __repr__(self):
        return 'Atividade: %s>' % self.nome

