import os

# ORM 적용을 위한 설정부

BASE_DIR = os.path.dirname(__file__)

# DB 접속주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQL Alchemy 이벤트 처리 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False
