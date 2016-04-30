from app import app


def migrate():
    metadata = app.config["DB"].get("METADATA")
    engine = app.config["DB"].get("ENGINE")
    metadata.create_all(engine)

if __name__ == '__main__':
    migrate()
    app.run()
