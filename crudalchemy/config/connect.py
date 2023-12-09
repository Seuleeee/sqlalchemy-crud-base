from crudalchemy.config.session import SessionLocal


def get_db():
    db = SessionLocal()
    return db
    # try:
    #     yield db
    # finally:
    #     db.close()

