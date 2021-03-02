## Installation

**Các bước**  
1. Tạo virtual env và cài các package cần thiết, rồi activate env đó
> <code>python3 -m venv venv</code> 
> <code>\Python27\Scripts\virtualenv.exe venv</code>  
> <code>venv\Scripts\activate</code>  
> <code>pip install -r requirements.txt</code>  
2. Migration và Migrate Database
> <code>python</code>  
> <code>>> from main import db</code>  
> <code>>> db.create_all()</code>  
> <code>>> exit()</code>  
3. Runserver
> <code>python main.py</code>  

