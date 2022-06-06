from main import User, Session, engine

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username == "Hugo").first()

user_to_update.username = "Vlad"
user_to_update.email = "dracula@gmail.com"

local_session.commit()
