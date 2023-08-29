import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from handlers import delivery_handlers, client_handlers, common_handlers


async def main():
    config: Config = load_config()
    dp = Dispatcher()
    bot = Bot(token=config.tg_bot.token)
    #admin_tg_ids: list[int] = config.tg_bot.admin_ids

    dp.include_routers(common_handlers.router, delivery_handlers.router,
                       client_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
