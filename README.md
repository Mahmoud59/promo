Promo System

To run project:

1 - Clone project from github 
    ( git clone https://github.com/Mahmoud59/promo.git ).

2 - In project directory beside requirements' directory, 
    create virtual environment by ( virtualenv venv ) command
    and active it by (source venv/bin/activate).

3 - Install packages in virtual environment by 
    (pip install -r requirements/requirements.txt - 
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

8 - After run project, open swagger docs in a main link 
    (http://127.0.0.1:8000)

9 - For login in (127.0.0.1:8000/api/token/)
    username: 'admin'
    password: '###'

10 - For create users (127.0.0.1:8000/api/users/)

11 - For create promo (127.0.0.1:8000/api/promos/)

12 - For modify promo (127.0.0.1:8000/api/promos/'promo_id'/)

13 - For delete promo (127.0.0.1:8000/api/promos/'promo_id'/)

14 - For list all promo for an admin (127.0.0.1:8000/api/promos/)

15 - For list all promo for user (127.0.0.1:8000/api/promos/)

16 - For show remaining of user promo (127.0.0.1:8000/api/promos/'promo_id'/)

17 - For use promo by user (127.0.0.1:8000/api/promo/'promo_id'/)

18 - For run unit test, run 'pytest' in apps directory beside users and promos.

19 - You can run flake8 --statistics for characters limited in one line.
