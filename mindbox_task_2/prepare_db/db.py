from sqlalchemy import create_engine, Engine

engine: Engine = create_engine("sqlite:///sqlite.db", echo=False)
