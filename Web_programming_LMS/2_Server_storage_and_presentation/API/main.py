from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
import database
import schema
from database import User, Token, get_db
from passlib.context import CryptContext

app = FastAPI()

# Khởi tạo thư viện mã hóa mật khẩu
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Biến toàn cục để lưu trữ thông tin người dùng tạm thời
last_user_data = []

# Khởi tạo cơ sở dữ liệu
@app.on_event("startup")
def on_startup():
    database.init_db()

# Hàm hash mật khẩu
def get_password_hash(password):
    return pwd_context.hash(password)

# Hàm kiểm tra mật khẩu
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#Home
@app.get("/")
def home():
    return "Ok"
    
# Endpoint đăng ký người dùng
@app.post("/register", response_model=schema.RegisterResponse)
def register_user(user: schema.UserRegister, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Lưu thông tin người dùng vào biến toàn cục bao gồm secret
    last_user_data.append(user.dict())

    return schema.RegisterResponse(id=db_user.id, username=db_user.username)

# Endpoint đăng nhập người dùng
@app.post("/login", response_model=schema.TokenResponse)
def login_user(user: schema.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # Giả sử rằng chúng ta tạo một token đơn giản
    token = f"fake-token-{db_user.username}"
    db_token = Token(user_id=db_user.id, token=token)
    db.add(db_token)
    db.commit()
    

    return schema.TokenResponse(token=token)

# Endpoint lấy thông tin người dùng (không cần token)
@app.get("/me")
def get_user_me():
    if not last_user_data:
        raise HTTPException(status_code=404, detail="No user data found")
    
    return last_user_data[0]