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
    memo = Column(UnicodeText)
    done = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return "<Task (title='%s')>" % self.title

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'memo': self.memo,
            'done': self.done,
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }

Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)

session = Session()
