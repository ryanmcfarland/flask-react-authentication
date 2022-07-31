# Flask & React Login + JWT Cookies Demo

Based heavily on this repo: https://github.com/ahnaf-zamil/flask-react-session-authenticaton-tutorial/

## Purpose

A demo app to show how to use authenticantion using JWT and Flask to provide and authenticate using generated JWT tokens that are stored within a httpOnly cookie within the browser.

The cookie only contains the following payload for security reasons:

```
{ exp:10000, username:"username_provided" }
```

## Set-up - Flask & React

### Flask

Create the flask backend - create the user table and start the backend app. This acts as our way to deliver the httpOnly cookie and provide revelant user information to the frontend

```bash
cd backend
flask db init
flask db update
flask run
```

### React

Either run / build the react frontend. Nothing fancy involved here.

```bash
cd frontend
npm install
npm start
```
