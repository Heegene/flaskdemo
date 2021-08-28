from flask import Blueprint, render_template, request, url_for
from datetime import datetime

from werkzeug.utils import redirect

from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question
from .. import db

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def qlist():
    # 질문 목록 출력(생성일 desc order by로 정렬)
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)
    # render_template는 템플릿 파일을 화면에 렌더링해 줌. 조회된 질문 목록을 템플릿으로 전달하면 전달된 데이터로 알아서 화면 구성
    # 이 경우에는 quesition/question_list.html이라는 파일에 렌더링을 수행하고, 이때 데이터는 question_list라는 이름으로
    # question_list 내용 받아서 들어감


# 질문 상세 url
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # question = Question.query.get(question_id)
    # 그냥 get 사용하면 쿼리 날렸을때 데이터가 없으면 빈페이지가 떠서 404 띄우기 위해 get_or_404로 선언
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template('question/question_detail.html', question=question, form = form)


@bp.route('/create/', methods=["GET","POST"])
def create():
    form = QuestionForm()
    # GET, POST 로 받고 GET은 question_form 을 렌더링만 해서 보여주고
    # POST 인 경우 데이터 저장 후 목록화면으로 리디렉션

    # validate_on_submit = 전송된 폼 데이터의 정합성 점검. DataRequired 등에 이상 없는지 확인
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject = form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)