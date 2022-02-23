import datetime
import sqlalchemy as sa

from .db_session import ORMBase
from sqlalchemy import orm


class User(ORMBase):
    # Имя таблицы
    __tablename__ = 'users'

    # Поля
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String, nullable=True)
    name = sa.Column(sa.String, nullable=True)
    age = sa.Column(sa.Integer, nullable=True)
    position = sa.Column(sa.String, nullable=True)
    speciality = sa.Column(sa.String, nullable=True)
    address = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)
    modified_date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    team_lead = orm.relation("Jobs", back_populates='user')


class Jobs(ORMBase):
    # Имя таблицы
    __tablename__ = 'jobs'

    # Поля
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    job = sa.Column(sa.String, nullable=True)
    work_size = sa.Column(sa.Integer, nullable=True)
    collaborators = sa.Column(sa.String, nullable=True)
    start_date = sa.Column(sa.DateTime, nullable=True)
    end_date = sa.Column(sa.DateTime, nullable=True)
    is_finished = sa.Column(sa.Boolean, nullable=True)

    user = orm.relation('User')
