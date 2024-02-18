from aiogram import Router, types
from aiogram.filters import Command

from sqlalchemy.orm import sessionmaker
from model import Note, engine

Session = sessionmaker(bind=engine)
session = Session()

user_router = Router()


@user_router.message(Command("start"))
async def starting(message: types.Message):
    await message.answer("Welcome, I'm ready to write your notes!")


@user_router.message(Command("add"))
async def add_note(message: types.Message):
    txt = message.text.strip('/add')
    note = Note(text=txt)
    session.add(note)
    session.commit()
    await message.answer("Note successfully added.")


@user_router.message(Command("getall"))
async def show_notes(message: types.Message):
    await message.answer("Your notes:")
    notes = session.query(Note).all()
    for note in notes:
        await message.answer(f"\n{note.text}")
