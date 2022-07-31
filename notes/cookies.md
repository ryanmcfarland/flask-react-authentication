## JWT or JWE for a rememeber_me

This doesn't matter - if a user has access to your cookies then he can provide both for access and get the same result. JWE just encrypts the payload so that the client cannot see the value.

## useful links

SO - https://stackoverflow.com/questions/23603801/handling-expiry-remember-me-functionality-with-jwt

## My Solution

- Remember_me token - lasts one year
- On page react refresh - generate a token that lasts 1 day and use this for subsequent page queries
- enables api access from other means by requesting a token.

## Flask Login

code
1. https://github.com/maxcountryman/flask-login/blob/main/src/flask_login/login_manager.py
2. https://github.com/maxcountryman/flask-login/blob/main/src/flask_login/utils.py

uses hmac - encode_cookie - payload & encrypted payload to verify using secret key on the backend

# React Redux Flask

1. https://github.com/dternyak/React-Redux-Flask/blob/master/application/app.py

## Flask & g & sessions

To get the username for any request, you need to get the username from the payload and assign it to the flask gloval parameter g
this is because each request is completely seperate within flask and all user data is contained within the cookie / jwt