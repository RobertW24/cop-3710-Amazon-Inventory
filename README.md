# cop-3710-Amazon-Inventory

# **Amazon Product Metadata, Reviews, & Supplier Database**

Problem Statement:
  - A database with an application that can retrieve certain products, certain product metadata/reviews, and products with specific metadata/ratings will be created.


Roles:
  - Solution Architect
  - Database Designer
  - Database Administrator

Partner's Role (Mathew King):
  - Application Developer


Application Domain:
  - Database for Amazon product data, analytics like reviews and ratings, & supplier information.

Database Application:
  - Oracle will be used as a database and an application will be developed in python.

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


Summary:
  - First, based on a scenario, an ER diagram is designed for a database with the following tables: product, product_info, price, supplier, review, and customer.
  - Next, a database schema is created to generate a corresponding database.
  - Then, csv files are created manually using data from any sources provided.
  - Then, a dataload python code is written to insert data from corresponding csv files into the previously-created database.
  - Finally, an application python code is written and 5 features are implemented.


Application Features:
  - 1. View all products with suppliers
  - 2. View products with pricing
  - 3. Search product by name
  - 4. View product reviews
  - 5. Average rating per product

Database Design:
  - [database_er.md](database_er.md)


# **HOW TO USE THIS REPO:**

- Step 1:
  - Creating the Schema:
    - Use the SQL script named "create_db.sql" to generate the schema for the ER design.
      - [create_db.sql](create_db.sql)

- Step 2:
  - Loading the Data:
    - Use the file named "dataload.py" to load all the CSV files into the database tables.
      - [dataload.py](dataload.py)
      - Use the CSV files in the "data" folder as the data files.
        - [data](data)
    - In dataload.py, swap out the instant client path, username, password, and dsn for the user's own.
    - Make sure the correct file address is chosen and run the dataload with "python dataload.py".

- Step 3:
  - Running the Application:
    - Use the file named "app.py" in the "Part_E" folder to run the application and use the features.
      - [Part_E](Part_E)
    - In app.py, swap out the instant client path, username, password, and dsn for the user's own.
    - If streamlit is not installed, enter this into the terminal "pip install streamlit".
    - Make sure the correct file address is chosen and run the application with "Python -m streamlit run app.py".

<img width="532" height="322" alt="image" src="https://github.com/user-attachments/assets/9a9545d1-9311-476e-8901-b3c95e85b968" />


