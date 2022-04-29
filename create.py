from data import db_session
from data.jobs import Jobs
from data.users import User


def main():
    db_session.global_init("db/mars.db")
    db_sess = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.set_password("123456789")
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
