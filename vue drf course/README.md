ori repo [link](https://github.com/pymike00/The-Complete-Guide-To-DRF-and-VueJS)

This project is developed using PyCharm



Project Setup
---
- install pillow 
    - python -m pip install --upgrade pip
    - python -m pip install --upgrade pillow

- command set:
  
    - django-admin startproject onlinestore
    
    - if new changes made in models.py , run these two commands

            ® python manage.py makemigrations
            ® python manage.py migrate
    - python manage.py createsuperuser
            
    - run django server
        - python manage.py runserver



Errors that may come across
---
- 针对django2.2报错：UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 9737: 
    
    - solution: [link](https://www.cnblogs.com/loveprogramme/p/10726712.html) 

Users and account
---
- username/pwd: standard/Ebook.objects.all
- random/auth/user/add/
