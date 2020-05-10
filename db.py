from aiogram import types
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence)
from sqlalchemy import sql

from config import db_pass, db_user, host

db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    username = Column(String(50))
    query: sql.Select

    def __repr__(self):
        return f"<User(id='{self.id}', fullname='{self.full_name}')>"


class Todolist(db.Model):
    __tablename__ = 'todolists'
    query: sql.Select

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    task = Column(String(50))
    photo = Column(String(250))

    def __repr__(self):
        return f"<Item(id='{self.id}', task='{self.task}')>"


class DBCommands:

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.full_name = user.full_name

        await new_user.create()
        return new_user

    async def show_todolists(self):
        todolists = await Todolist.query.gino.all()

        return todolists


async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{host}/postgresql')

    # Create tables
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()
