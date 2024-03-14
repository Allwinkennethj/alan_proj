from config import db
from users.model import User_Details

def s_getall():
    data=db.session.query(User_Details).all()
    res=[]
    for i in data:
        res.append(i.make_json())
    return res

def s_getuser(email):
    data=db.session.query(User_Details).filter_by(email=email).first()
    return data.make_json()

def s_adduser(emaild,passwordd):
    try:
        user=User_Details(
            email=emaild,
            password=passwordd
        )
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        return False

def s_ifexists(email):
    try:
        usr=db.session.query(User_Details).filter_by(email=email).first()
        if usr is None:
            return False
        else:
            return True
    except Exception as e:
        return False

def s_edit_user(email, name=None, designation=None, age=None):
    try:
        user = db.session.query(User_Details).filter_by(email=email).first()
        print(user)
        if user:
            if name:
                user.name = name
            if designation:
                user.designation = designation
            if age:
                user.age = age
            print(user)
            db.session.commit()
            return user.make_json()
        else:
            return False
    except Exception as e:
        return False

def checkpass(emailid,passwordd):
    # print(emailid)
    password_db=db.session.query(User_Details).filter_by(email=emailid).first()
    # print(password_db)
    if password_db.password==passwordd:
        return True
    else:
        return False
    return True