from typing import NoReturn

from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import engine
from .facke_data import data_categories, data_products
from .models import Category, Product


def create_category(session: Session, name: str):
    category: Category = Category(name=name)
    session.add(category)
    session.commit()


def create_product(session: Session, name: str, price: int):
    product: Product = Product(name=name, price=price)
    session.add(product)
    session.commit()


def add_categories(session: Session, categories: list) -> NoReturn:
    """
    Добавление категорийю
    :param session: Session
    :param categories: list
    :return: NoReturn
    """
    for cat in categories:
        create_category(session=session, name=cat)
    session.commit()


def add_products(session: Session, products: dict[str, dict]) -> NoReturn:
    """
    Добавление продуктов.
    :param session: Session
    :param products: dict[str, dict]
    :return:
    """
    for prod, v in products.items():
        create_product(session=session, name=prod, price=v.get('price'))
    session.commit()


def fetch_category_by_id(session: Session, id_: int) -> Category:
    stmt = select(Category).where(Category.id == id_)
    cat: Category = session.execute(stmt).scalar_one_or_none()
    return cat


def fetch_product_by_name(session: Session, name: str) -> Product:
    stmt = select(Product).where(Product.name == name)
    product: Product = session.execute(stmt).scalar_one_or_none()
    return product


def add_product_category(session: Session,
                         products: dict[str, dict]) -> NoReturn:
    """
    Добавление категорий к продуктам
    :param session: Session
    :param products: dict[str, dict]
    :return: NoReturn
    """
    for p, v in products.items():
        if v.get('cats'):
            prod = fetch_product_by_name(session, p)
            prod.category = [
                fetch_category_by_id(session, c) for c in v['cats']
            ]
            session.commit()


def insert_categories():
    with Session(engine) as session:
        add_categories(session=session, categories=data_categories)


def insert_products():
    with Session(engine) as session:
        add_products(session=session, products=data_products)


def insert_products_categories():
    with Session(engine) as session:
        add_product_category(session=session, products=data_products)


def main():
    insert_categories()
    insert_products()
    insert_products_categories()
