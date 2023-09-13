"""
Создание и заполнение БД SQLite3 (sqlite.db)
"""
from mindbox_task_2.prepare_db import insert_data
from mindbox_task_2.prepare_db.db import engine
from mindbox_task_2.prepare_db.models import Base

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    insert_data.main()
