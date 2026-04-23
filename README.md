# cop-3710-Amazon-Inventory

Application Domain:
- Database for Amazon product data and analytics like reviews and ratings.

Database Application:
- I will use oracle as a database and my applications will be developed in python.

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

Database Design:
- [database_er.md](database_er.md)


**HOW TO USE THIS REPO:**

  Step 1:
  - Creating the Schema:
    - Use the SQL script named "create_db.sql" to generate the schema for the ER design.
      - [create_db.sql](create_db.sql)

  Step 2:
  - Loading the Data:
    - Use the file named "dataload.py" to load all the CSV files into the database tables.
      - [dataload.py](dataload.py)
    - Use the CSV files in the "data" folder as the data files.
      - [data](data)
    - In dataload.py, swap out the instant client path, username, password, and dsn for your own.

  Step 3:
  - Running the Application:
    - Use the file named "app.py" in the "Part_E" folder to run the application and use the features.
      - [Part_E](Part_E)
    - In app.py, swap out the instant client path, username, password, and dsn for your own.
    - If you do not have streamlit installed, enter this into the terminal "pip install streamlit"
    - Run the application with "Python -m streamlit run app.py"

