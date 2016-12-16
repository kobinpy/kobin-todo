from kobin import Kobin
import redis
from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker

Base = declarative.declarative_base()
from .users import User
from .tasks import Task


def setup_models(app: Kobin) -> None:
    engine = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"), echo=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    app.config["DB"] = {
        "METADATA": Base.metadata,
        "ENGINE": engine,
        "SESSION": session,
    }


def setup_redis(app: Kobin) -> None:
    app.config['REDIS'] = redis.StrictRedis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        db=app.config['REDIS_DB'],
    )
