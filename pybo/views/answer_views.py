from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import AnswerForm
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

# create의 parameter question_id는 url에서 전달. ~/answer/create/2 로 페이지 요청받으면 question_id에 2가 넘어옴
# method POST로 지정(template 에 있는 html에서 지정한 method와 일치하게 선언하여야 함 일치하지 않으면 method not allowed 에러)
# <form action="{{ url_for('answer.create', question_id=question_id) }}" method="post">


# @bp.route('/create/<int:question_id>', methods=["POST"])
# def create(question_id):
#     question = Question.query.get_or_404(question_id)
#     # POST 폼 방식으로 전송된 데이터 항목 중 name 속성이 'content' 인 항목을 content에 담겠단 소리
#     content = request.form['content']
#     # request 객체는 flask에서 생성 없이 사용할 수 있는 내장 객체. 브라우저의 요청부터 응답까지의 처리구간에서 request를 사용할 수 있게 해줌
#     # 브라우저에서 요청한 정보를 확인할 수 있음
#
#     answer = Answer(content=content, create_date = datetime.now())
#     # answer_set => 질문에 달린 답변들
#     question.answer_set.append(answer)
#     db.session.commit()
#     return redirect(url_for('question.detail', question_id=question_id))
#
#     # 이렇게 question에서 달지 않고 answer 로 바로 추가해도 같은 결과 가능
#     # answer = Answer(question=question, content=content, create_date=datetime.now())
#     # db.session.add(answer)

@bp.route('/create/<int:question_id>', methods=["POST"])
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now())
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)

