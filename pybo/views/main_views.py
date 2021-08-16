from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix="/")

# 분리를 위해 이동
# @bp.route('/')
# def index():
#     # 질문 목록 출력(생성일 desc order by로 정렬)
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html', question_list=question_list)
#     # render_template는 템플릿 파일을 화면에 렌더링해 줌. 조회된 질문 목록을 템플릿으로 전달하면 전달된 데이터로 알아서 화면 구성
#     # 이 경우에는 quesition/question_list.html이라는 파일에 렌더링을 수행하고, 이때 데이터는 question_list라는 이름으로
#     # question_list 내용 받아서 들어감


# main_views로 인덱스 리디렉션
@bp.route("/")
def index():
    return redirect(url_for('question.qlist'))
# url for를 이용해서 question.qlist에 해당하는 url로 리디렉션하도록 함
# redirect는 해당 url로 리디렉션해주는 역할, url_for는 라우트가 설정된 함수명으로 url을 역으로 찾아주는 역할
# 이때 url_for에 전달된 question.qlist는 question, qlist 순서로 해석되고
# question은 등록된 블루프린트의 이름, qlist는 해당 블루프린트에 등록된 함수명임
# 그래서 bp의 기본 라우팅인 question + 그리고 qlist에 등록된 list가 합쳐져 /question/list로 url 반환



@bp.route("/walwal")
def walwal():
    return "walwalwal!!"

# question_views로 이동
# # 질문 상세 url
# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     # question = Question.query.get(question_id)
#     # 그냥 get 사용하면 쿼리 날렸을때 데이터가 없으면 빈페이지가 떠서 404 띄우기 위해 get_or_404로 선언
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question)
