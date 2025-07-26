from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Kết nối tới cơ sở dữ liệu SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Tạo session cho truy cập CSDL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Khởi tạo Base cho các mô hình
Base = declarative_base()

# Hàm lấy kết nối cơ sở dữ liệu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mô hình User
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
# Mô hình Token (có thể để lưu trữ JWT tokens)
class Token(Base):
    __tablename__ = 'tokens'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    token = Column(String, unique=True)

# Khởi tạo cơ sở dữ liệu
def init_db():
    Base.metadata.create_all(bind=engine)