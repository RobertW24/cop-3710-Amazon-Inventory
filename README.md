# cop-3710-Amazon-Inventory

Application Domain:
- Database for Amazon product data and analytics like reviews and ratings.

High-Level Goals:
  - Product metadata analyzer
  - Review/rating analyzer
  - Supplier information analyzer

Users:
  - Amazon
  - Companies selling products on Amazon
  - Amazon's competitiors

Data Sources:
  - https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset
  - https://amazon-reviews-2023.github.io/
  - https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews

Databse Design:

- [link](database_er.md)


Creating the Schema:

- Use the sql script named "create_db.sql" to generate the schema for the ER design.

- [link](create_db.sql)


Data:

- Use the CSV files in the "data" folder as the data files.

- [link](data)

Loading the Data:
- Use the file named "dataload.py" to load all the CSV files into the database tables.
- [link](dataload.py)


Database Application:
- I will use oracle as a database and my applications will be developed in python.
