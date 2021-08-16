from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)

    # 데이터 임시로 입력해줌
    # sudo flask shell
    # Instance: / opt / python / flask - demo / instance
    # >> > from pybo.models import Question, Answer
    # >> > from datetime import datetime
    # >> > q = Question(subject='이동네 얼굴 맛집이 누구냐', content='한국에서 제일  귀여운 강아지 이름을 알고 싶어요', create_date=datetime.now())
    # >> >
    # >> > from pybo import db
    # >> > db.session.add(q)
    # >> > db.session.commit()
    # >> >
    #     >> > q.id
    #     1
    #     >> > q.subject
    #     '이동네 얼굴 맛집이 누구냐'
    #     >> > q.content
    #     '한국에서 제일 귀여운 강아지 이름을 알고 싶어요'
    #     >> > Quesion.query.all()
    #     Traceback(most
    #     recent
    #     call
    #     last):
    #     File
    #     "<console>", line
    #     1, in < module >
    #
    #
    # NameError: name
    # 'Quesion' is not defined
    # >> > Question.query.all()
    # [ < Question
    # 1 >]
    # >> > q = Question(subject='콩이 몇살인가요', content='얼굴 보니 어제 태어난듯', create_date=datetime.now())
    # >> > db.session.add(q)
    # >> > db.session.commit()
    # >> > Question.query.all()
    # [ < Question
    # 1 >, < Question
    # 2 >]
    # >> >

    # 데이터 수정하기
    # get 으로 가져와서 그냥 = 로 대치해주고 commit 만 해주면 됨
    # >> > q = Question.query.get(2)
    # >> > q
    # < Question
    # 2 >
    # >> > q.subject
    # '콩이 몇살인가요'
    # >> > q.subject = '콩이 나이가?'
    # >> > q.subject
    # '콩이 나이가?'
    # >> > db.session.commit()

    # 데이터 삭제
    # 그냥 삭제 하고 커밋하면 됨
    # >> > q = Question.query.get(1)
    # >> > db.session.delete(q)
    # >> > db.session.commit()
    # >> > Question.query.all()
    # [ < Question
    # 2 >]
    # >> >

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # question table과 연결, delete cascading이라 question table 에서 삭제되면 같이 삭제됨
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # question 속성은 answer이 question 을 참조하기 위해 추가함 (answer.question.subject 이런식으로 제목 참조 가능해짐
    # 이때 db.relationship에 저장할 첫 값은 참조할 모델명이고, 두번째 backref에 지정한 값은 역참조 설정
    # == 질문에서도 답변 참조 가능
    # 추가 기능 https://docs.sqlalchemy.org/en/13/core/type_basics.html
    # cascade 관련 옵션은 위에서도 넣어줬긴 한데 저 ondelete 옵션은 쿼리로 delete 날렸을 때만 적용되는거라
    # 파이썬 코드상에서 날렸을때도 cascade 로 날아가길 원한다면 여기에 넣어줘야함
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan' ))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


    # answer 모델 crud
    # 답변생성
    # >> > from datetime import datetime
    # >> > from pybo.models import Question, Answer
    # >> > from pybo import db
    # >> > q = Question.query.get(2)
    # >> > a = Answer(question=q, content='2018년생이요', create_date=datetime.now())
    # >> > db.session.add(a)
    # >> > db.session.commit()
    # 연결된 질문에 액세스
    # >> > a.question.subject
    # '콩이 나이가?'

    # 연결된 답변에 액세스(answer_set은 리스트 접근하듯이 접근)
    # >> > q.answer_set[0].content
    # '2018년생이요'