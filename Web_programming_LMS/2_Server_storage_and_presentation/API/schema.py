from pydantic import BaseModel

# Lớp schema cho đăng ký người dùng
class UserRegister(BaseModel):
    username: str
    password: str
    secret: str

# Lớp schema cho đăng nhập người dùng
class UserLogin(BaseModel):
    username: str
    password: str

# Lớp schema cho phản hồi sau khi đăng ký
class RegisterResponse(BaseModel):
    id: int
    username: str

# Lớp schema cho phản hồi sau khi lấy thông tin người dùng
class UserResponse(BaseModel):
    id: int
    username: str

# Lớp schema cho phản hồi token
class TokenResponse(BaseModel):
    token: str