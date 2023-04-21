from fastapi import FastAPI
from jwt_authentication import constants
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from jwt_authentication import exceptions
import config

@AuthJWT.load_config
def get_config():
    return config.Settings()


def create_app():
    app = FastAPI(
        title='FastAPI jwt-auth Authentication Routes',
        description=constants.DESCRIPTION,
        version='1.0.0',
        exception_handlers={AuthJWTException: exceptions.authjwt_exception_handler},
    )

    from jwt_authentication.authentication import authentication
    from jwt_authentication.users import user

    app.include_router(authentication.router)
    app.include_router(user.router)

    return app
