from config import create_app, db
from controllers.user_controller import user_bp

app = create_app()
app.register_blueprint(user_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)