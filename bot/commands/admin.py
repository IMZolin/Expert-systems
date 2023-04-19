from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommand

from loader import bot
from .default import get_default_commands


def get_admin_commands() -> list[BotCommand]:
    commands = get_default_commands()

    commands.extend([
        BotCommand('/export_users', 'экспорт пользователей в csv'),
        BotCommand('/count_users', 'подсчитать пользователей, которые связались с ботом'),
        BotCommand('/count_active_users', 'подсчет активных пользователей (которые не заблокировали бота)'),
    ])

    return commands


async def set_admin_commands(user_id: int):
    await bot.set_my_commands(get_admin_commands(), scope=BotCommandScopeChat(user_id))