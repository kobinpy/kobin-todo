from datetime import datetime

from sqlalchemy import (
    Column, Integer, Unicode, UnicodeText, Boolean, DateTime,
    create_engine
)
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker


Base = declarative.declarative_base()
engine = create_engine('sqlite:///db.sqlite3', echo=True)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    detail = Column(UnicodeText)
    done = Column(Boolean, nullable=False, default=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return "<Task (title='%s')>" % self.title

    def update(self, title=None, detail=None, done=None):
        if title:
            self.title = title
        if detail:
            self.detail = detail
        if done:
            self.done = done
        self.updated_at = datetime.now()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'detail': self.detail,
            'done': self.done,
            'updated_at': self.updated_at.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d'),
        }

Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)

session = Session()
