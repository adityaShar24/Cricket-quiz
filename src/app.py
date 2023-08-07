from flask import Flask

app = Flask(__name__)

from flask_jwt_extended import JWTManager
from middlewares.user_middleware import register_middleware , login_middleware
from routes.user_router import auth_bp , cache

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'
app.config['CACHE_TYPE'] = 'simple'


JWTManager(app)
cache.init_app(app)

app.before_request(register_middleware)
app.before_request(login_middleware)

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug= True)