import DB.Models as models
from sqlalchemy.orm import Session

def check_pwd(db :Session,uname:str,pwd:str):
    return db.query(models.User).filter(models.User.uname == uname).first() == pwd