from .manager import BaseManager

DB_SETTINGS = {
    "host": "127.0.0.1",
    "port": "5432",
    "database": "ormify",
    "user": "Elias",
    "password": "EliasORM",
}

BaseManager.database_settings = DB_SETTINGS
