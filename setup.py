from setuptools import setup

setup(
    name='event-manager',
    version='1.0.0',
    packages=[
        'blinker==1.7.0',
        'click==8.1.7',
        'colorama==0.4.6',
        'dynaconf==3.2.4',
        'Flask==2.1.3',
        'Flask-JWT-Extended==4.5.3',
        'Flask-RESTful==0.3.10',
        'Flask-SQLAlchemy==2.5.1',
        'greenlet==3.0.1',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.3',
        'marshmallow==3.20.1',
        'packaging==23.2',
        'psycopg2==2.9.9',
        'PyJWT==2.8.0',
        'pytz==2023.3.post1',
        'six==1.16.0',
        'SQLAlchemy==1.4.50',
        'typing_extensions==4.8.0',
        'Werkzeug==2.2.2'
    ],
    url='https://github.com/omribarouch/EventHandler.git',
    license='',
    author='Omri Barouch',
    author_email='omby8888@gmail.com',
    description='AlfaBet Backend Exercise'
)
