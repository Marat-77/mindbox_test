# Продукты и категории.
from sqlalchemy import String, Integer, Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# промежуточная таблица product_category
association_table = Table(
    'product_category',
    Base.metadata,
    Column('product_id',
           ForeignKey('product.id'),
           primary_key=True),
    Column('category_id',
           ForeignKey('category.id'),
           primary_key=True)
)


# Product
class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(55), nullable=False, unique=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    category = relationship(
        'Category',
        secondary=association_table,
        back_populates='product',
        cascade='all, delete'
    )

    def __repr__(self) -> str:
        return (f'Product(id:{self.id!r}, name:{self.name!r},'
                f' price:{self.price!r})')

    def __str__(self) -> str:
        return repr(self)


# Category
class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(55), nullable=False, unique=True)
    product = relationship(
        'Product',
        secondary=association_table,
        back_populates='category',
        cascade='all, delete'
    )

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"

