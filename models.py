from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True, null=False)
    password = fields.CharField(max_length=255, unique=True, null=False)

    notes: fields.ReverseRelation["Note"]


class Note(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    body = fields.TextField()

    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="notes", on_delete=fields.CASCADE)
