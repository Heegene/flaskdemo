import dateutil
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

# create_app 이 이름은 바꾸면 flask 내부에서 호출 안하니까 함수명 이걸로 해야함
def create_app():
    app = Flask(__name__)

    # ORM (object relational mapping)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # blueprint 적용 => main_views에 라우팅 적용해주면됨
    from .views import main_views, question_views, answer_views
    # main_views에 있는 bp 객체 등록
    app.register_blueprint(main_views.bp)
    # question_views로 분리해줬으니 이것도 blueprint 적용
    app.register_blueprint(question_views.bp)

    app.register_blueprint(answer_views.bp)

    return app
