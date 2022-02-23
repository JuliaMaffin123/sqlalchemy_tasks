from data import db_session
from data.models import User


db_session.global_init("db/mars_explorer.sqlite")

db_sess = db_session.create_session()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Bang Chan"
user.name = "Christopher"
user.age = 24
user.position = "leader of Stray Kids"
user.speciality = "rapper, producer"
user.address = "module_97"
user.email = "Chan_woof_woof@mars.org"
user.hashed_password = "Baby Stays"
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Zhopenpopel"
user.name = "Genrybrihen"
user.age = 31
user.position = "chef"
user.speciality = "german chef of atomic cuisine"
user.address = "module_32"
user.email = "liebe_Schmetterlinge@mars.org"
user.hashed_password = "password"
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Pilotov"
user.name = "Pilot"
user.age = 23
user.position = "pilot"
user.speciality = "spaceship pilot"
user.address = "module_2"
user.email = "pilot@mars.org"
db_sess.add(user)
db_sess.commit()
