from datetime import datetime
from sqlalchemy import (
    Column, Integer, Unicode, UnicodeText, Boolean, DateTime, ForeignKey
)

from . import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    detail = Column(UnicodeText)
    done = Column(Boolean, nullable=False, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"<Task (title='{self.title}')>"

    def update(self, title=None, detail=None, done=None, **kwargs):
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail
        if done is not None:
            self.done = done
        self.updated_at = datetime.now()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'detail': self.detail,
            'done': self.done,
            'user_id': self.user_id,
            'updated_at': self.updated_at.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d'),
        }
