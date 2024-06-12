import DB.Models as models
from sqlalchemy.orm import Session

def check_pwd(db :Session,uname:str,pwd:str):
    return db.query(models.User).filter(models.User.uname == uname).first() == pwd

def check_user_exists(db :Session,uname:str):
    q = db.query(models.User).filter(models.User.uname == uname)
    return db.query(q.exists())


def create_user(db :Session,uname:str,pwd:str):
    return True