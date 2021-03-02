## Installation

### Chuẩn bị dev-env backend
**Yêu cầu**  
Có cài đặt pipenv

**Các bước**  
1. Dùng pipenv tạo virtual env và cài các package cần thiết, rồi activate env đó
> <code>python3 -m venv venv</code> 
> <code>\Python27\Scripts\virtualenv.exe venv</code>  
> <code>venv\Scripts\activate</code>  
> <code>pip install -r requirements.txt</code>  
2. Migration và Migrate Database
> <code>python manage.py makemigrations</code>  
> <code>python manage.py migrate</code>  
3. Runserver
> <code>python manage.py runserver</code>  

