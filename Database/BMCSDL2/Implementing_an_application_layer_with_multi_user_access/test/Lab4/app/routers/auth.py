from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from app.database import get_db
from app.models import User, Role
from werkzeug.security import generate_password_hash, check_password_hash

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Trang đăng ký
@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# Xử lý đăng ký
@router.post("/register")
async def register_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    role: str = Form(...),
    db: AsyncSession = Depends(get_db),
):
    hashed_password = generate_password_hash(password)

    # Kiểm tra tên người dùng đã tồn tại
    result = await db.execute(select(User).where(User.username == username))
    existing_user = result.scalar()
    if existing_user:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Username already exists.",
        })

    # Lấy ID vai trò từ cơ sở dữ liệu
    result = await db.execute(select(Role).where(Role.name == role))
    role_obj = result.scalar()
    if not role_obj:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Invalid role selected.",
        })

    # Tạo người dùng mới
    new_user = User(username=username, password=hashed_password, role_id=role_obj.id)
    db.add(new_user)
    await db.commit()
    return RedirectResponse(url="/auth/login", status_code=303)

# Trang đăng nhập
@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Xử lý đăng nhập
@router.post("/login")
async def login_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db),
):
    # Truy vấn thông tin người dùng và vai trò
    result = await db.execute(
        select(User, Role)
        .join(Role, User.role_id == Role.id)
        .where(User.username == username)
    )
    row = result.first()
    if not row:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Invalid username or password.",
        })

    user, role = row
    if not check_password_hash(user.password, password):
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Invalid username or password.",
        })

    # Lưu thông tin đăng nhập vào session
    request.session["username"] = user.username
    request.session["role"] = role.name

    # Đăng nhập thành công
    return RedirectResponse(url="/query", status_code=303)

# Danh sách người dùng (giữ nguyên chức năng cũ)
@router.get("/users", response_class=HTMLResponse)
async def list_users(request: Request, db: AsyncSession = Depends(get_db)):
    username = request.session.get("username")
    role = request.session.get("role")

    if role != "role_manager":
        raise HTTPException(status_code=403, detail="Access forbidden: Managers only.")

    result = await db.execute(select(User).join(Role).order_by(User.id))
    users = result.fetchall()
    return templates.TemplateResponse("users.html", {
        "request": request,
        "users": users,
        "username": username,
        "role": role,
    })

# Thêm chức năng đăng xuất
@router.get("/logout")
async def logout(request: Request):
    request.session.clear()  # Xóa toàn bộ session
    return RedirectResponse(url="/auth/login", status_code=303)
