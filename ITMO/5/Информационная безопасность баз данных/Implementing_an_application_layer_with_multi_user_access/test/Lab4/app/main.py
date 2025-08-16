from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.future import select
from app.database import engine, Base, get_db
from app.models import Role
from app.routers import auth, query

app = FastAPI()

# Thêm SessionMiddleware để quản lý session
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")  # Đổi "your_secret_key" thành giá trị an toàn

# Templates setup
templates = Jinja2Templates(directory="app/templates")

# Mount static files để phục vụ tệp tĩnh
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Database setup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Tạo bảng nếu chưa tồn tại
        await conn.run_sync(Base.metadata.create_all)

        # Thêm vai trò mặc định nếu chưa có
        result = await conn.execute(select(Role).where(Role.name.in_(["role_manager", "role_staff"])))
        existing_roles = [row.name for row in result.fetchall()]
        if "role_manager" not in existing_roles:
            await conn.execute(Role.__table__.insert().values(name="role_manager"))
        if "role_staff" not in existing_roles:
            await conn.execute(Role.__table__.insert().values(name="role_staff"))
        await conn.commit()

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(query.router, prefix="/query", tags=["query"])

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    username = request.session.get("username")
    role = request.session.get("role")
    if not username or not role:
        return templates.TemplateResponse("base.html", {"request": request, "error": "Please log in to continue."})
    return templates.TemplateResponse("base.html", {"request": request, "username": username, "role": role})

# Thêm router mặc định để kiểm tra server hoạt động
@app.get("/healthcheck", response_class=HTMLResponse)
async def health_check():
    return {"status": "ok"}

# Quản lý lỗi 404 (Page Not Found)
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
