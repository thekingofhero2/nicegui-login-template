from tortoise import Tortoise

async def init_db() -> None:
    await Tortoise.init(db_url='sqlite://db2.sqlite3', modules={'models': ['Models']})
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()