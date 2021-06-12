# Project running into local machine
```ssh
    $ git clone https://github.com/SreekanthTeja/IntellectArena.git
    $ virtualenv env
    $ source env/bin/activate 
    $ pip install -r requirements.txt 
    $ cd <project_name>
    $ python manage.py runserver
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver
```


<h4 align='center'>Postman Testing </h4>

> export date into database
```
[GET]
$ localhost:8000/accounts/date 
At first request data is dumped into database
if we hit the request you find certain exception error
```
> to achieve login functionality do this in your browser for good reason
```
$ http://127.0.0.1:8000/accounts/login
```
> To make appointments
```
> firstly we need to have token.So give valid credentials 
Type POST,headers = Content-Type application/json
$ localhost:8000/auth/jwt/create/
At this point you will get tokens in the names of refresh,access
> Take new tab paste below urlendpoint select type POST 
$ http://127.0.0.1:8000/accounts/appointment
So we have the access token to access certain view. Now Apply token in the Authorization JWT <your tokken> in 
Now in headers = Content-Type: application/json,
                Authorization: JWT <access token>
for testing purpose give data in the given format:
{
	"appointment_date":"2021-06-10 05:00:01",
	"time_slot":1,
	"organizer":14
}
and finally hit the request
if you see token expiry
repeat the procedure
```
