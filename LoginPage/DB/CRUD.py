import DB.Models as models
from sqlalchemy.orm import Session

def check_pwd(db :Session,uname:str,pwd:str):
    return db.query(models.User).filter(models.User.uname == uname).first() == pwd

def check_user_exists(db :Session,uname:str):
    return db.query(models.User).exists(models.User.uname == uname)


def create_user(db :Session,uname:str,pwd:str):
    return True