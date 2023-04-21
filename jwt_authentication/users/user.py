from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT
from jwt_authentication.users import schemas, services
from database import get_db

import cloudinary
import cloudinary.uploader

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.put('/update_profile')
def update_profile(request: schemas.Profile = Depends(), file: UploadFile = File(...), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()

    profile_photo = cloudinary.uploader.upload(file.file)
    url = profile_photo.get("url")
    service_obj = services.UserProfile(request)
    return service_obj.update_profile(url, current_user)


@router.get('/show_user_profile', response_model=schemas.BaseProfile)
def user_profile(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()

    return services.user_profile(db, current_user)


@router.put('/change_password')
def change_my_password(request: schemas.ChangePassword, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()

    service_obj = services.UserProfile(request)
    return service_obj.change_my_password(current_user)
