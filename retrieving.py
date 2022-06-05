from main import User, Session, engine

local_session = Session(bind=engine)

### return all objects
# users = local_session.query(User).all()[:3]
# for user in users:
#     print(user.username)


### query one object

mina = local_session.query(User).filter(User.username == "Wilhelmina").first()
print(mina.username)
print(mina.email)
