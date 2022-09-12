from ninja import Schema

class AccountIn(Schema):
    name:str
    phone: str
    password1: str
    password2: str
    
class AccountOut(Schema):
    name:str
    phone: str
    
    
class AothorizationOut(Schema):
    tokken: str
    UserAccount: AccountOut
    
    
    
class SignIn(Schema):
    phone: str
    password: str
    
    
class ErrorSchema(Schema):
    detail:str