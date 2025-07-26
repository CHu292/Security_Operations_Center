#  FastAPI

## Khái niệm
- FastApi là 1 web framework dùng để build API có hiệu năng cao, code dễ ẹc, đơn giản nhưng cũng hỗ trợ tốt cho việc làm sản phẩm.
- Đặc điểm:

  - Fast: Hiệu suất cao ngang với NodeJS và Go.
  - Fast to code: Code nhanh hơn, tốc độ code các features tăng khoảng 200 đến 300 %.
  - Fewer bugs: do đơn giản nên giảm số bugs của developper đến 40%.
  - Intuitive: hỗ trợ code dễ hơn với tự động gợi ý, debug cần ít thời gian hơn so với trước.
  - Easy: được thiết kế sao cho dễ dùng dễ học.
  - Short: Tối thiểu việc lặp code. Các tham số truyền vào có nhiều tính năng. Ít bugs.
  - Robust: hiệu năng mạnh mẽ, có thể tương tác API qua docs.

---

## Cách cài đặt
- Yêu cầu: Python 3.6+.
- FastAPI được build dựa trên OpenAPI (trước có tên Swagger), phần web được support bởi Starlette, còn phần data được support bởi Pydantic.

### FastAPI CLI

- Để cài đặt framework này trên Ubuntu, bạn cần phiên bản python ≥ 3.6.
  
  ```pip install fastapi```
- Bạn cũng cần ASGI server khi deploy sản phẩm như Uvicorn hoặc Hypercorn.
``` pip install uvicorn```
- ASGI kế thừa từ WSGI. Mà WSGI là 1 chuẩn giao tiếp giữa web server và Python application server.
- WSGI có những tác dụng như sau:
  - WSGI mang tính linh hoạt: dev có thể chuyển đổi thành phần web như chuyển từ Gunicorn sang uWSGI.
  - WSGI xử lý nhiều request cùng lúc thay webserver và quyết định request nào được chuyển tới application web.

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Hinh_minh_.png" alt="" width="1000">
</p>
<p align="center"><b>Hình minh họa</b></p>

- Nếu như WSGI là tiêu chuẩn cho các ```synchronous Python apps``` thì ASGI là tiêu chuẩn cho cả ```synchronous``` và ```asynchronous Python apps```. ASGI phù hợp với tất cả ứng dụng sử dụng WSGI do có cơ chế tương thích ngược.

### FastAPI Docs

- Do based trên OpenAI mà trước đó có tên là Swagger nên FastAPI cung cấp doc có giao diện dễ nhìn, dễ sử dụng. Ví dụ minh họa:
- Khi bật doc bằng local url ```http://0.0.0.0:8000/docs```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/code_run_result.png" alt="" width="1000">
</p>
<p align="center"><b>Docs</b></p>

- 1 giao diện khác của FastAPI docs ```http://0.0.0.0:8000/redoc```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/code_run_result_redoc.png" alt="" width="1000">
</p>
<p align="center"><b>Redoc</b></p>

### Performance
Các bạn có thể test hiệu năng của các web framework trên [trang này](https://www.techempower.com/benchmarks/)

### Optional Depencies

- Do FastAPI based trên Pydantic và Starlette nên có hỗ trợ thêm 1 số thư viện
- Pydantic:

  - ujson: JSON "parsing" nhanh hơn.
  - email_validator: validate email.

- Starlette:

  - requests: khi bạn muốn tạo request, dùng TestClient.
  - aiofiles: khi bạn muốn dùng FileResponse hoặc StaticFile.
  - jinja2: nếu bạn muốn dùng các mẫu config mặc định.
  - python-multipart: hỗ trợ "parsing" với request.form().
  - itsdangerous: hỗ trợ SessionMiddleware.
  -graphene: hỗ trợ GraphQL.

- FastAPI:

  - uvicorn: ASGI server phục vụ cho ứng dụng của bạn.
  - orjson: nếu muốn dùng ORJSONResponse.

- Nếu muốn dùng hết thư viện trên thì bạn chỉ cần dùng 1 câu lệnh đơn giản.

```pip install fastapi[all]```

---

# Hướng dẫn cơ bản
## Create a simple API
---
Các bước

Nói chung bạn chỉ cần 6 bước để tạo 1 API

- Bước 1: import fastapi
- Bước 2: tạo 1 instance của class FastAPI
- Bước 3: tạo đường dẫn, bắt đầu từ /
- Bước 4: khai báo phương thức HTTP: post, get, put, delete hay options, head, patch, trace
- Bước 5: khai báo hàm
- Bước 6: trả về content với format dict, list, str, int, ...
---

- Tạo một file main.py như sau:
  
```python
from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi

app = FastAPI() # gọi constructor và gán vào biến app

@app.get("/") #giống flask, khai báo phương thức get và url
async def root(): #do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async
	return {"message": "Hello world"}
```

sau đó chạy app:
```uvicorn main:app --host 0.0.0.0 --port 8000```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/run_code_fastapi.png" alt="chạy app" width="1000">
</p>
<p align="center"><b>Chạy app </b></p>

**P/S: nếu bạn làm trong môi trường phát triển có thể thêm --reload để tự động restart sau khi thay đổi code.**

-  Chúng ta cùng xem trên giao diện Docs ```http://127.0.0.1:8000/docs```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/code_run_result.png" alt="chạy app" width="1000">
</p>
<p align="center"><b>Xem kết quả trên giao diện Docs </b></p>

- Ấn vào Try it out -> Execute -> API trả về response.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/API_returns_response.png" alt="API trả về response" width="1000">
</p>
<p align="center"><b>API trả về response</b></p>

- Giao diện API này được thiết kế dựa trên OpenAPI. Có 1 khái niệm để define API gọi là "Schema". 
- Truy cập vào:  ```http://127.0.0.1:8000/openapi.json```

```
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/": {
      "get": {
        "summary": "Root",
        "operationId": "root__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {

                }
              }
            }
          }
        }
      }
    }
  }
}
```
---

## Path Parameters

- Bạn có thể truyền param thông qua đường dẫn.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
	return {"item_id": item_id}
```

- Biến item_id trên đường dẫn sẽ truyền vào hàm read_item với thông qua param trùng tên item_id. Test thử ```http://127.0.0.1:8000/items/abc```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/path_parameters_1.png" alt="" width="1000">
</p>
<p align="center"><b>Ví dụ thử trên web</b></p>

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/path_parameters_2.png" alt="" width="1000">
</p>
<p align="center"><b>Kiểm tra trạng thái</b></p>


### Path parameters with types
- Bạn cũng có thể khai báo định dạng của param để trả về khi truyền biến đúng định dạng sẽ trả về giá trị.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
	return {"item_id": item_id}
```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Path_parameters_with_types.png" alt="" width="1000">
</p>
<p align="center"><b>Path parameters with types</b></p>

### Data validation

- Còn nếu không đúng định dạng thì trả về thông báo. Mọi dữ liệu được validate đều dựa trên Pydantic.

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Data_validation.png" alt="" width="1000">
</p>
<p align="center"><b>Data validation</b></p>

### Order

Nếu bạn có khai báo đường dẫn trùng lặp như thế này:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_users_me():
	return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
	return {"user_id": user_id}
```
Thì nhớ để theo thứ tự /users/me trước rồi đến /users/{user_id} sau, ngược lại nếu /users/{user_id} ở trước thì sẽ nghĩ rằng "user_id" được nhận giá trị me.

### Path in path

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
	return {"file_fath": file_path}
```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/path_in_path.png" alt="" width="1000">
</p>
<p align="center"><b>Path in path</b></p>

---

## Query Parameters

- Nếu bạn truyền param dưới dạng key-value thì ở trong FastAPI có hỗ trợ với tên gọi "query" parameters.

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Ch"}, {"item_name": "Mi"}, {"item_name": "ran"}] # pair format: key-value

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
	return fake_items_db[skip: skip+limit] # trả về dữ liệu từ skip đến skip  + limit
```

- Cùng kiểm tra kết quả
  
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/query_parameters.png" alt="" width="700">
</p>
<p align="center"><b>Query Parameters</b></p>

- Nếu bạn để ý skip và limit có format string khi làm đường dẫn nhưng một khi truyền về hàm thì sẽ ngay lập tức được convert từ string về int.

### Optional parameters

- Ngoài ra FastAPI cung cấp một cách khai báo optional query parameters, mặc định là None.

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    '''
    param item_id: format string
    param q: format string, default value: None, Optional: help you find error that happen
    '''
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```
- Như bạn thấy ở trên param truyền ở đường dẫn là item_id, nhưng trong hàm có thêm param q. FastAPI chỉ sử dụng str để nhận định format của param còn Optional thì FastAPI không sử dụng, chỉ có tác dụng check lỗi nếu xảy ra.

- Bạn có thể test bằng đường dẫn sau.

``` http://127.0.0.1:8000/items/1?q=1 # 1 là item_id và ?q=1 là giá trị của q```


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/optional_parameters.png" alt="" width="700">
</p>
<p align="center"><b>Optional parameters</b></p>

### Query parameter type conversion

Thay đổi giá trị mặc định bằng cách truyền giá trị trên đường dẫn.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, short: bool = False): # param short với định dạng boolean có giá trị mặc định là False
    item = {"item_id": item_id}
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```
- Trong trường hợp này

```http://127.0.0.1:8000/items/1?short=1```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Query_parameter_type_conversion_1.png" alt="" width="700">
</p>
<p align="center"><b>Query parameter type conversions 1 </b></p>

```http://127.0.0.1:8000/items/1?short=true```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Query_parameter_type_conversion_true.png" alt="" width="700">
</p>
<p align="center"><b>Query parameter type conversions true</b></p>

```http://127.0.0.1:8000/items/1?short=false```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Query_parameter_type_conversion_false.png" alt="" width="700">
</p>
<p align="center"><b>Query parameter type conversions - false</b></p>

### Multiple path and query parameters

- Với các đường dẫn lồng nhau, FastAPI biết param nào với param nào dựa trên tên param.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str):
    item = {"item_id": item_id, "owner_id": user_id}
    return item
```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Multiple_path_and_query_parameters.png" alt="" width="700">
</p>
<p align="center"><b>Multiple path and query parameters</b></p>

### Required query parameters

Đơn giản là bạn điền thiếu param trên đường dẫn sẽ báo lỗi

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
	item = {"item_id": item_id, "needy": needy}
	return item
```

- chỉ truyền vào giá trị của item_id còn giá trị của needy thì không nên sinh ra lỗi.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Required_query_parameters.png" alt="" width="700">
</p>
<p align="center"><b>Required query parameters</b></p>

```bash
$ uvicorn Required_query_parameters:app --host 0.0.0.0 --port 8000
INFO:     Started server process [194004]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:38720 - "GET /items/34 HTTP/1.1" 422 Unprocessable Entity
```
----

## Request Body

- Request body: người dùng gửi request từ browser đến API.
- Response body: dựa trên request, APi trả về response cho người dùng.
- Để khai báo format của request body, bạn cần sử dụng Pydantic models.
-  P/S: nhắc nhở khi send request cần sử dụng phương thức POST, nếu dùng phương thức GET thì bạn sẽ bị lộ thông tin trên URL => tính bảo mật không cao.

### Pydantic Models

**code**

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel #import class BaseModel của thư viện pydantic

class Item(BaseModel): #Kế thừa từ class BaseModel và khai báo các biến
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): #Khai báo dưới dạng parameter
	return item
```
#### Chạy bằng CLI

```bash
$ curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Book",
  "description": "A very interesting book",
  "price": 15.99,
  "tax": 1.99
}'
```
- Kết quả:
```bash
{"name":"Book","description":"A very interesting book","price":15.99,"tax":1.99}
```
#### Using Swagger UI

- Đi theo url sau:

```bash
http://127.0.0.1:8000/docs
```

- thêm vào như sau:

```json
{
  "name": "chu",
  "description": "hehe",
  "price": 10,
  "tax": 2
}
```
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Pydantic_Models_use_swagger_ui.png" alt="" width="700">
</p>
<p align="center"><b>Using Swagger UI</b></p>




<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Pydantic_Models_use_swagger_ui_responses.png" alt="" width="700">
</p>
<p align="center"><b>Using Swagger UI - Responses</b></p>

**Dựa trên việc import Pydantic module, FastAPI hỗ trợ:**

- Đọc request body dưới dạng Json.
- Chuyển đổi định dạng biến.
- Validate dữ liệu
- Khai báo format mặc định của request body, class Item trên là 1 ví dụ.
- Gen JSON Schema cho model của bạn
- Schema sẽ được gen thành UI của OpenAI doc.

### Use model

Trong hàm create_item, bạn có thể tùy biến các biến của class Item, đơn giản như việc tính phí chịu thuế bằng cách tính tổng item.price và item.tax như bên dưới.

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
	item_dict = item.dict()
	if item.tax:
		price_with_tax = item.price + item.tax
		item_dict.update({"price with tax": price_with_tax})
	return item_dict
```

- Thực hiện 1 request

  ```bash
  $ curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Book",
  "description": "A very interesting book",
  "price": 15.99,
  "tax": 1.99
}'

- Trả về response
  
```
{"name":"Book","description":"A very interesting book","price":15.99,"tax":1.99,"price with tax":17.98}
```

### Request body + path parameters

- FastAPI hỗ trợ khai báo tham số URL và request body cùng lúc, framework sẽ biết tham số nào truyền từ đường dẫn và tham số nào lấy từ request.

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
	return {"item_id": item_id, **item.dict()}
```

- Thực hiện request

```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/items/123' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Laptop",
  "description": "A powerful gaming laptop",
  "price": 1500.00,
  "tax": 150.00
}'
```

- Response
  
```bash
{"item_id":123,"name":"Laptop","description":"A powerful gaming laptop","price":1500.0,"tax":150.0}
```

- Hoặc có thể như thực hiện như sau:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Request_body_and_path_parameters.png" alt="" width="700">
</p>
<p align="center"><b>Request body + path parameters</b></p>

## Query Parameters and String Validations

- Ở phần trước chúng ta đã biết khái niệm của query parameter rồi, lạ 1 loại param có cũng được không có cũng không sao. Param này có attribute là Optional, nhưng độ dài bị giới hạn không vượt quá 50 ký tự. Nên FastAPI cung cấp class Query.

```python
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Chu"}, {"item_id": "miran"}]}
    if q:
        results.update({"q": q})
    return results
```

- Câu lệnh q: Optional[str] = Query(None) cũng tương tự q: Optional[str] = None nhưng Query cung cấp các param khác như max_lenght, min_lenght, regex, ... Bạn có thể tăng giới hạn ký tự thành 250 như thế này chỉ việc thay đổi giá trị tham số. (Mặc định của max_lenght là 50)

- Gửi request:

```bash
$ curl -X 'GET' "http://127.0.0.1:8000/items/hhhh?short=true"
{"item_id":"hhhh"}
```

```bash
$ curl -X 'GET' "http://127.0.0.1:8000/items/hhhh?short=false"
{"item_id":"hhhh","description":"This is an amazing item that has a long description"}
```

### Query parameter list / multiple values

Ngoài định dạng string và integer, FastAPI còn hỗ trợ type List.

```python
from typing import List, Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
```
q là 1 List có thể chứa nhiều giá trị.

Ví dụ: ```http://localhost:8000/items/?q=ha&q=he```

Response body mà API trả về:

```html
{
  "q": [
    "ha",
    "he"
  ]
}
```

API cũng được cập nhật theo.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Query_parameter_list_mutiple_value.png" alt="" width="700">
</p>
<p align="center"><b>Query parameter list / multiple values</b></p>


P/S: bạn cũng có thể thay List[str] thành list như thế này.

```python
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items
```

Query còn 1 vài param nữa nhưng không quá quan trọng, bạn có thể vào doc của FastAPI để tìm hiểu chi tiết.

Các param mà Query cung cấp:

- Metadata

  	- alias: tên khác của param
	- title: metadata đặt tên param
	- description: metadata giới thiệu param
	- deprecated: khi bạn chán param nào thì thêm vào để người dùng biết là bạn không còn sử dụng param đó nữa

- Validation cho string:

	- min_lenght
	- max_lenght
	- regex

 ## Path Parameters and Numeric Validations

- Query parameters có class Query để khai báo metadata và validations, Path parameters có class Pass với cơ chế tương tự.

- Thêm title metadata cho path param item_id:

```python
from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Path_Parameters_and_Numberic_Validations.png" alt="" width="700">
</p>
<p align="center"><b>Path Parameters and Numeric Validations</b></p>

### Number validations: greater than or equal

Tương tự với le=100, item_id bắt buộc phải là 1 số nhỏ hơn hoặc bằng 100.

```python
item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000)
```

P/S: Number validations không chỉ hỗ trợ type integer mà còn hỗ trợ cho type float.

```python
size: float = Query(..., gt=0, lt=10.5)
```

