# Assignment 7: Django REST API Project

## Module 16: Implementing REST API Using Django

This project demonstrates the implementation of a REST API using **Django REST Framework (DRF)**.  
It includes models, serializers, views, filters, and permissions to build a fully functional blog-style API.

---

## Project Structure
- **manage.py** – Django project management file  
- **blog/** – Main Django project configuration  
- **helloworld/** – Django app containing models, serializers, filters, permissions, and views  
- **db.sqlite3** – Database file  
- **screenshots/** – Screenshots of API implementation  

---

## Features
- ✅ Basic REST API implementation using Django REST Framework  
- ✅ CRUD operations for blog posts  
- ✅ Filtering and ordering of API responses  
- ✅ Pagination support  
- ✅ Permissions and authentication  
- ✅ Admin integration for managing posts  

---

## Requirements
Install the dependencies before running the project:

```bash
pip install django djangorestframework django-filter==2.4.0
```

---

## Running the Project

1. Navigate to the project folder:
   ```bash
   cd blog
   ```
2. Apply migrations:
   ```bash
   python manage.py migrate
   ```
3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the API at:  
   - API Root: `http://127.0.0.1:8000/`  
   - Admin Panel: `http://127.0.0.1:8000/admin/`  

---

## Screenshots

### 1. Hello World using REST API
![Hello World](screenshots/Hello_world_using_REST_API.jpg)

### 2. Creating Model in Admin
![Admin Model](screenshots/creating_model_in_admin.jpg)

### 3. Posting API
![Posting API](screenshots/posting_API.jpg)

### 4. Adding User Name to the Post
![User Name](screenshots/adding_user_name_to_the_post.jpg)

### 5. Search and Ordering Filters
![Filters](screenshots/search_and_ordering_filters.jpg)

### 6. Segregating into Pages (Pagination)
![Pagination](screenshots/segregating_into_pages.jpg)


