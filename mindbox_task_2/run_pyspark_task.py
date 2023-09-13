"""
Есть 2 датафрейма (pyspark.sql.DataFrame) - с продуктами и категориями.
Одному продукту может соответствовать много категорий,
в одной категории может быть много продуктов.
Напишите метод с помощью PySpark,
который вернет датафрейм с набором всех пар «Имя продукта – Имя категории».
В результирующем датафрейме должны также присутствовать продукты,
у которых нет категорий.
"""

from pyspark.sql import SparkSession

from from_sqlite import read_db

df1, df2, df3 = read_db()
categories, products, products_categories = read_db()

# создание SparkSession
spark = SparkSession.builder.appName('product_category_app').getOrCreate()

# создание category DataFrame
category_df = spark.createDataFrame(
    data=categories.get('data'),
    schema=categories.get('columns')
)

# print(type(category_df))
# # <class 'pyspark.sql.dataframe.DataFrame'>

category_df.show()
# +---+------+
# | id|  name|
# +---+------+
# |  1|cat_01|
# |  2|cat_02|
# |  3|cat_03|
# |  4|cat_04|
# +---+------+

# создание product DataFrame
product_df = spark.createDataFrame(
    data=products.get('data'),
    schema=products.get('columns')
)
product_df.show()
# +---+----------+-----+
# | id|      name|price|
# +---+----------+-----+
# |  1|product_01| 1200|
# |  2|product_02|  356|
# |  3|product_03| 1048|
# |  4|product_04| 1674|
# |  5|product_05| 1899|
# |  6|product_06| 1925|
# +---+----------+-----+

# создание product_category DataFrame
product_category_df = spark.createDataFrame(
    data=products_categories.get('data'),
    schema=products_categories.get('columns')
)
product_category_df.show()
# +----------+-----------+
# |product_id|category_id|
# +----------+-----------+
# |         1|          3|
# |         1|          1|
# |         2|          4|
# |         2|          3|
# |         4|          1|
# |         5|          4|
# |         5|          3|
# |         5|          1|
# |         6|          4|
# +----------+-----------+

category_df.createOrReplaceTempView("category")
product_df.createOrReplaceTempView("product")
product_category_df.createOrReplaceTempView("product_category")

sql_query = '''
SELECT p.name product_name, c.name category_name
FROM category c 
LEFT JOIN product_category pc ON c.id == pc.category_id
LEFT JOIN product p ON p.id == pc.product_id
  UNION
SELECT p.name product_name, c.name category_name
FROM category c 
LEFT JOIN product_category pc ON c.id == pc.category_id
RIGHT JOIN product p ON p.id == pc.product_id;
'''

spark.sql(sql_query).show()
# +------------+-------------+
# |product_name|category_name|
# +------------+-------------+
# |  product_02|       cat_03|
# |  product_01|       cat_03|
# |        null|       cat_02|
# |  product_06|       cat_04|
# |  product_05|       cat_04|
# |  product_02|       cat_04|
# |  product_05|       cat_01|
# |  product_05|       cat_03|
# |  product_04|       cat_01|
# |  product_01|       cat_01|
# |  product_03|         null|
# +------------+-------------+
