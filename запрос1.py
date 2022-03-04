from data import db_session
from data.models import User

db_file = input()
db_session.global_init(f"db/{db_file}")

db_sess = db_session.create_session()

for user in db_sess.query(User).filter(User.address.like('module_1')):
    print(user)
