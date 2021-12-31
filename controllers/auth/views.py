from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi import APIRouter, Header, Depends

from models import User
from .dependencies import active_user
from .helpers import hash_password
from .instances import session
from .requests import LoginIn, RegisterIn
from .responses import TokenOut, UserOut

router = APIRouter()


# Routes


@router.post("/login", response_model=TokenOut)
async def login(form: LoginIn):
    user = await User.get_or_none(username=form.username, password=hash_password(form.password))

    if user is None:
        raise HTTPException(400, "wrong username or password")
    
    token = session.create_session({ "username": user.username })

    return JSONResponse({"token": token}, 200)


@router.get("/logout")
async def logout(authorization: str = Header(None)):
    session.delete_session(authorization)

    return Response(status_code=204)


@router.post("/register", response_model=TokenOut)
async def register(form: RegisterIn):
    if await User.get_or_none(username=form.username, password=hash_password(form.password)):
        raise HTTPException(409, "a user with the same username already exists")

    user = User(username=form.username, password=hash_password(form.password))

    await user.save()
    
    token = session.create_session({ "username": user.username })

    return JSONResponse({"token": token}, 200)


@router.get("/current", response_model=UserOut)
async def get_current_user(current_user: User = Depends(active_user)):
    response = {
        "username": current_user.username
    }

    return JSONResponse(response, 200)
