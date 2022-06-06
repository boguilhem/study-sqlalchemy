from main import User, Session, engine

local_session = Session(bind=engine)

users = [
    {"username": "Johnathan", "email": "harker@email.com"},
    {"username": "Abraham", "email": "vanhelsing@email.com"},
    {"username": "Quincey", "email": "morris@email.com"},
    {"username": "Wilhelmina", "email": "mina@email.com"},
    {"username": "John", "email": "seward@email.com"},
    {"username": "Arthur", "email": "goldaming@email.com"},
]

# new_user = User(username="Hugo", email="hugo@email.com")

for u in users:
    new_user = User(username=u["username"], email=u["email"])
    local_session.add(new_user)
    local_session.commit()

    print(f"Added {u['username']}")
