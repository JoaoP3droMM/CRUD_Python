from config import create_app, db
from controllers.user_controller import user_bp
# from controllers.associations_controller import association_bp
# from controllers.empresa_controller import empresa_bp
# from controllers.estabelecimento_controller import estabelecimento_bp
# from controllers.socio_controller import socio_bp

app = create_app()
app.register_blueprint(user_bp)
# app.register_blueprint(association_bp)
# app.register_blueprint(empresa_bp)
# app.register_blueprint(estabelecimento_bp)
# app.register_blueprint(socio_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)