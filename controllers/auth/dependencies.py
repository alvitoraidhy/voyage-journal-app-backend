from fastapi import HTTPException, Header, Depends
from typing import Union

from models import User
from .instances import session


async def logged_in(authorization: str = Header(None)):
    user_session = session.read_session(authorization)

    if user_session is None:
        raise HTTPException(401, "invalid token")

    return user_session


async def active_user(user_session=Depends(logged_in)):
    user = await User.get_or_none(username=user_session["username"])

    if user is None:
        raise HTTPException(401, "invalid session")

    return user
