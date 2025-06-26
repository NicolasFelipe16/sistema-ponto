from flask import Flask, url_for
from models import db, usuarios
from routes import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sistema_ponto.db"
db.init_app(app)
app.register_blueprint(routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        admin = usuarios.query.filter_by(nome="Admin").first()

        if not admin: 
            admin = usuarios(
                permissao="administrator",
                nome="Admin",
                sobrenome="",
                senha="123"
            )
            
            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)