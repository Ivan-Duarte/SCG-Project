import os

class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "scg_user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "SCG_Db_2024safe")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "scg_inventory_db")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

settings = Settings()


