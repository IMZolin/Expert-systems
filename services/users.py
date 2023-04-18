from typing import Optional
from peewee import fn

from models import User
from utils.misc.logging import logger


def count_users() -> int:
    query = User.select(fn.COUNT(User.id))
    return query.scalar()


def get_users() -> list[User]:
    query = User.select()

    return list(query)


def get_user(id: int) -> User:
    return User.get_or_none(User.id == id)


def update_username(user: User, name: str, username: str = None) -> User:
    user.name = name
    user.username = username
    user.save()

    return user


async def update_user(id: int, name: Optional[str] = None, scores: Optional[int] = None, current_step: Optional[int] = None, task_1_best: Optional[int] = None, mark: Optional[int] = None) -> bool: 
    user = get_user(id)
    if user is None:
        return False
    else:
        if name is not None:
            user.name = name
        if scores is not None:
            user.scores = scores
        if current_step is not None:
            user.current_step = current_step
        if task_1_best is not None:
            user.task_1_best = task_1_best
        if mark is not None:
            user.mark = mark
        user.save()
        return True


def edit_user_language(id: int, language: str):
    query = User.update(language=language).where(User.id == id)
    query.execute()


def create_user(id: int, name: str, username: str = None) -> User:
    new_user = User.create(id=id, name=name, username=username)

    new_user.is_admin = False
    new_user.save()

    logger.info(f'New user {new_user}')

    return new_user


def get_or_create_user(id: int, name: str, username: str = None) -> User:
    user = get_user(id)

    if user:
        user = update_username(user, name, username)

        return user

    return create_user(id, name, username)


def get_user_info(user: User) -> str:
    result = ""
    result += f"<b>" + user.name + "</b>\n"
    result += f"<b>" + str(user.scores) + "$</b>"
    result += f"<b>" + str(user.mark) + "$</b>"
    return result
