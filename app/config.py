import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://admin:KJXkT4wBUL84SvZuJeoBis71ARzEnzfR@dpg-cr2bdb5svqrc73cmec3g-a.oregon-postgres.render.com/task1_4a8q")

settings = Settings()
