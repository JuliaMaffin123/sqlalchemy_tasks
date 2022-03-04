db_file = input()

global_init(db_file)

db_sess = create_session()

for user in db_sess.query(User).filter(User.age < 18):
    print(user, user.age, 'years')
