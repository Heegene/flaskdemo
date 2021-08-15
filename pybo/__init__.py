from flask import Flask


# create_app 이 이름은 바꾸면 flask 내부에서 호출 안하니까 함수명 이걸로 해야함
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return "hello, kongE!"

    return app
