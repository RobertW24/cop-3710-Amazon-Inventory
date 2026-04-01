import oracledb
import csv

# --- SETUP ---
LIB_DIR = r"C:\Users\j5r24\Downloads\instantclient-basic-windows.x64-11.2.0.4.0\instantclient_11_2"  # Your Instant Client Path
DB_USER = "RWATERMAN0451_SCHEMA_N0KUW"
DB_PASS = "2CSA8#YK62NSRgZHS6SDRFBN5TMLYI"
DB_DSN = "db.freesql.com:1521/23ai_34ui2"

# Initialize Thick Mode (Required for FreeSQL/Cloud)
oracledb.init_oracle_client(lib_dir=LIB_DIR)


def data_load_csv(file_path, sql):
    try:
        # 1. Connect
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()

        # 2. Read CSV Data into a List
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            data_to_insert = [row for row in reader]

        # 4. Execute Batch
        print(f"Starting bulk load of {len(data_to_insert)} rows...")
        cursor.executemany(sql, data_to_insert)

        # 5. Commit Changes
        conn.commit()
        print(f"Successfully loaded {cursor.rowcount} rows into the database.")

    except Exception as e:
        print(f"Error during bulk load: {e}")
        if 'conn' in locals():
            conn.rollback()  # Undo changes if an error occurs

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()


# Run the function

sql_ = "INSERT INTO supplier (sup_id, sup_name, supply_price, lead_time) VALUES (:1, :2, :3, :4)"

data_load_csv('supplier.csv', sql_)

sql_ = "INSERT INTO price (price_id, normal_price, discount_percentage, discounted_price) VALUES (:1, :2, :3, :4)"

data_load_csv('price.csv', sql_)

sql_ = "INSERT INTO product_info (prod_info_id, price_id, prod_name, category, descript) VALUES (:1, :2, :3, :4, :5)"

data_load_csv('product_info.csv', sql_)

sql_ = "INSERT INTO product_ (prod_id, prod_info_id, sup_id, img_link, prod_link, rev_count, avg_rating) VALUES (:1, :2, :3, :4, :5, :6, :7)"

data_load_csv('product_.csv', sql_)

sql_ = "INSERT INTO customer (cus_id, cus_name) VALUES (:1, :2)"

data_load_csv('customer.csv', sql_)

sql_ = "INSERT INTO review (prod_id, cus_id, rev_title, rev_body, rating) VALUES (:1, :2, :3, :4, :5)"

data_load_csv('review.csv', sql_)



