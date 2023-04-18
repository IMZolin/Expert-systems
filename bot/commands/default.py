from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommand

from loader import _, bot, i18n


def get_default_commands() -> list[BotCommand]:
    commands = [
        BotCommand('/start', 'запустить бота'),
        BotCommand('/help', 'как бот работает?'),
        BotCommand('/change_name', 'поменять имя'),
    ]

    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())

    # for lang in i18n.available_locales:
    #     await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)


async def set_user_commands(user_id: int):
    
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeChat(user_id))