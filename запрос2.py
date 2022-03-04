db_file = input()

global_init(db_file)

db_sess = create_session()

for user in db_sess.query(User).filter(User.address.like('module_1'), User.speciality.notilike("%engineer%"),
                            User.position.notilike("%engineer%")):
    print(user.id)
