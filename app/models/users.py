from datetime import datetime
from sqlalchemy import (
    Column, Integer, Unicode, DateTime
)

from . import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    nickname = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False)
    avatar_url = Column(Unicode(512), nullable=False)
    auth_service = Column(Unicode(16))  # Now, Support only github.
    auth_service_id = Column(Unicode(255), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"<User (name='{self.name}')>"

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.name,
            'email': self.email,
            'avatar_url': self.avatar_url,
            'updated_at': self.updated_at.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d'),
        }
