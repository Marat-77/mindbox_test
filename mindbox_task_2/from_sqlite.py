import sqlite3
from sqlite3 import Cursor


def get_list_tuples_from_db(cursor: Cursor,
                            table: str) -> dict[str, list | list[str]]:
    """
    Чтение данных из БД sqlite3 в словарь {columns: data}
    :param cursor: Cursor
    :param table: str
    :return: dict[str, list | list[str]]
    """
    cursor.execute(f'SELECT * FROM {table}')
    columns = [description[0] for description in cursor.description]
    data = cursor.fetchall()
    res = [tuple(columns)]
    res.extend(cursor.fetchall())
    return {'columns': columns, 'data': data}


def read_db() -> tuple[dict[str, list], dict[str, list], dict[str, list]]:
    """
    Чтение данных из БД sqlite3
    :return: tuple[dict[str, list], dict[str, list], dict[str, list]]
    """
    db_file = 'sqlite.db'
    with sqlite3.connect(db_file) as conn:
        cursor: Cursor = conn.cursor()
        categories = get_list_tuples_from_db(cursor, 'category')

        products = get_list_tuples_from_db(cursor, 'product')

        products_categories = get_list_tuples_from_db(cursor,
                                                      'product_category')
    return categories, products, products_categories
