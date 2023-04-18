from datetime import datetime

from peewee import BigIntegerField, CharField, BooleanField, DateTimeField, IntegerField

from .base import BaseModel


class User(BaseModel):
    id = BigIntegerField(primary_key=True)
    name = CharField(default=None)
    username = CharField(default=None, null=True)
    current_step = IntegerField(default=0, null=True)
    task_1_best = IntegerField(default=0, null=True)
    scores = IntegerField(default=0, null=True)
    mark = IntegerField(default=0, null=True)

    is_admin = BooleanField(default=False)

    created_at = DateTimeField(default=lambda: datetime.utcnow())

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    class Meta:
        table_name = 'users'