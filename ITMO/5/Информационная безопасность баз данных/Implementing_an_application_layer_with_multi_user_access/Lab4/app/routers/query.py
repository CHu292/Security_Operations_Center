from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from app.database import get_db
from fastapi.templating import Jinja2Templates
import logging
import time

# Cấu hình logging
logging.basicConfig(filename="query.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Khai báo router
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Lưu lịch sử truy vấn
query_history = []

# Danh sách quyền cho các vai trò
ALLOWED_TABLES_MANAGER = ["orders", "product", "customer"]
ALLOWED_VIEWS_STAFF = ["sales_employee_view", "customer_view"]
FORBIDDEN_KEYWORDS = ["drop", "truncate", "alter"]

# Endpoint GET để hiển thị dashboard
@router.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    username = request.session.get("username")
    role = request.session.get("role")

    if not username or not role:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Unauthorized. Please log in."
        })

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "username": username,
        "role": role,
        "history": query_history,
        "result": None,
        "last_query": None,
        "error": None
    })

# Endpoint POST để thực hiện truy vấn
@router.post("/", response_class=HTMLResponse)
async def execute_query(
    request: Request,
    query: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    try:
        # Lấy vai trò và tên người dùng từ session
        role = request.session.get("role")
        username = request.session.get("username")

        if not role or not username:
            return templates.TemplateResponse("dashboard.html", {
                "request": request,
                "error": "Unauthorized. Please log in.",
                "last_query": None,
                "history": query_history,
            })

        # Kiểm tra từ khóa nguy hiểm
        if any(keyword in query.lower() for keyword in FORBIDDEN_KEYWORDS):
            return templates.TemplateResponse("dashboard.html", {
                "request": request,
                "error": "Dangerous queries are not allowed.",
                "last_query": query,
                "history": query_history,
                "username": username,
                "role": role,
            })

        # Phân tích câu truy vấn
        query_lower = query.strip().lower()
        query_parts = query_lower.split()
        command = query_parts[0]  # Lệnh SQL (SELECT, INSERT, ...)

        # Xác định bảng mục tiêu
        target_table_or_view = None
        if command in ["insert", "update", "delete"]:
            if command == "insert":
                target_table_or_view = query_parts[query_parts.index("into") + 1]
            elif command == "update":
                target_table_or_view = query_parts[1]
            elif command == "delete" and "from" in query_parts:
                target_table_or_view = query_parts[query_parts.index("from") + 1]
        elif "from" in query_parts:
            target_table_or_view = query_parts[query_parts.index("from") + 1]

        if target_table_or_view:
            target_table_or_view = target_table_or_view.rstrip(";").strip()

        # Kiểm tra quyền
        if role == "role_manager":
            if command not in ["select", "insert", "update", "delete"]:
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": f"Command '{command.upper()}' is not allowed for manager.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })
            if target_table_or_view and target_table_or_view not in [table.lower() for table in ALLOWED_TABLES_MANAGER]:
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": f"Access to '{target_table_or_view}' is not allowed for manager.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })
        elif role == "role_staff":
            if command != "select":
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": "Only SELECT queries are allowed for staff.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })
            if target_table_or_view and target_table_or_view not in [view.lower() for view in ALLOWED_VIEWS_STAFF]:
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": f"Access to '{target_table_or_view}' is not allowed for staff.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })

        # Ghi log truy vấn
        logging.info(f"[{role.upper()}] {username} executed query: {query}")

        # Thực thi truy vấn SQL
        result = await db.execute(text(query))
        if command in ["insert", "update", "delete"]:
            await db.commit()

        rows = []
        column_names = []
        data = []

        if command == "select":
            try:
                rows = result.fetchall()
                column_names = result.keys()
                # Chuyển đổi kết quả thành danh sách dictionary
                data = [dict(zip(column_names, row)) for row in rows]
            except Exception as e:
                logging.error(f"Error fetching rows: {str(e)}")
        
        # Thêm truy vấn vào lịch sử
        query_history.append(query)
        if len(query_history) > 10:
            query_history.pop(0)

        # Hiển thị kết quả trên dashboard
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "result": data,
            "last_query": query,
            "history": query_history,
            "total_rows": len(data) if command == "select" else None,
            "username": username,
            "role": role,
        })
    except SQLAlchemyError as e:
        logging.error(f"Error executing query: {query} - {str(e)}")
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "error": f"Error executing query: {str(e)}",
            "last_query": query,
            "history": query_history,
            "username": username,
            "role": role,
        })
