Features
 -

FastAPI extension that provides JWT Auth support (secure, easy to use and lightweight), if you were familiar with flask-jwt-extended this extension suitable for you, cause this extension inspired by flask-jwt-extended grinning

 - Access tokens and refresh tokens
 - Freshness Tokens
 - Revoking Tokens
 - Support for WebSocket authorization
 - Support for adding custom claims to JSON Web Tokens
 - Storing tokens in cookies and CSRF protection

How to run fastapi-jwt-auth requests:
 - 
 - pip install flit
 - Create README.md file 
 - Create pyproject.toml file in the same root directory. Copy the code from below URL.
   - https://github.com/IndominusByte/fastapi-jwt-auth/blob/master/pyproject.toml
 - Create a folder with name **fastapi_jwt_auth** and add files from below git URL.
   - https://github.com/IndominusByte/fastapi-jwt-auth/tree/master/fastapi_jwt_auth
 - Run the following command
   - flit install --deps develop --symlink
 - Run the code with fastapi server command.
   - uvicorn main:app --reload

Helpful Documentation URLs:
 -
 - https://pypi.org/project/fastapi-jwt-auth/
 - https://indominusbyte.github.io/fastapi-jwt-auth/contributing/
 - https://github.com/fastapi-users/fastapi-users/issues/820
 - https://github.com/IndominusByte/fastapi-jwt-auth#
