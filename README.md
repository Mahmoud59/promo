Promo System

To run project:

1 - Clone project from github 
    ( git clone https://github.com/Mahmoud59/promo.git ).

2 - In project directory beside requirements directory, 
    create virtual environment by ( virtualenv venv ) command.

3 - Install packages in virtual environment by 
    (pip install -r requirements/requirements.txt
     pip install -r requirements/test-requirements.txt) commands.

4 - Create postgresql 'promo_system' database.

5 - Migrate apps migrations (./manage.py migrate)

6 - In main app directory Create super user 'Admin' by 
    ( ./manage.py createsuperuser )
    username: 'admin'
    email: 'admin@promo.com'
    password: '####'

7 - Run fixtures for admin profile
    (./manage.py loaddata fixtures/*.json)

8 - Open swagger docs in main link (http://127.0.0.1:8000)

9 - For login in (127.0.0.1:8000/api/api/token/)
    username: 'admin'
    password: '###'

10 - For create promo (127.0.0.1:8000/api/promos/)

11 - For modify promo (127.0.0.1:8000/api/promos/'promo_id'/)

12 - For delete promo (127.0.0.1:8000/api/promos/'promo_id'/)

13 - For list all promo for admin (127.0.0.1:8000/api/promos/)

12 - For list all promo for user (127.0.0.1:8000/api/promos/)

13 - For show remaining of user promo (127.0.0.1:8000/api/promos/'promo_id'/)

14 - For use promo by user (127.0.0.1:8000/api/promo/'promo_id'/)
