
import streamlit as st
import oracledb


# --- DATABASE SETUP ---
LIB_DIR = r"C:\Users\j5r24\Downloads\instantclient-basic-windows.x64-11.2.0.4.0\instantclient_11_2"
DB_USER = "RWATERMAN0451_SCHEMA_N0KUW"
DB_PASS = "2CSA8#YK62NSRgZHS6SDRFBN5TMLYI"
DB_DSN = "db.freesql.com:1521/23ai_34ui2"


# Initialize Oracle Client for Thick Mode
@st.cache_resource
def init_db():
    if LIB_DIR:
        try:
            oracledb.init_oracle_client(lib_dir=LIB_DIR)
        except Exception as e:
            st.error(f"Error initializing Oracle Client: {e}")


init_db()

conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
cursor = conn.cursor()

def run_query(query, params=None):
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    for row in cursor:
        print(row)

def menu():
    while True:
        print("\n==== MENU ====")
        print("1. View all products with suppliers")
        print("2. View products with pricing")
        print("3. Search product by name")
        print("4. View product reviews")
        print("5. Average rating per product")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            run_query("""
                SELECT p.prod_id, pi.prod_name, s.sup_name
                FROM product_ p
                JOIN product_info pi ON p.prod_info_id = pi.prod_info_id
                JOIN supplier s ON p.sup_id = s.sup_id
            """)

        elif choice == "2":
            run_query("""
                SELECT pi.prod_name, pr.normal_price, pr.discount_percentage
                FROM product_ p
                JOIN product_info pi ON p.prod_info_id = pi.prod_info_id
                JOIN price pr ON pi.price_id = pr.price_id
            """)

        elif choice == "3":
            keyword = input("Enter keyword: ")
            run_query("""
                SELECT prod_name, category
                FROM product_info
                WHERE LOWER(prod_name) LIKE LOWER(:kw)
            """, {"kw": f"%{keyword}%"})

        elif choice == "4":
            prod_id = input("Enter product ID: ")
            run_query("""
                SELECT c.cus_name, r.rating, r.rev_title, r.rev_body
                FROM review r
                JOIN customer c ON r.cus_id = c.cus_id
                WHERE r.prod_id = :pid
            """, {"pid": prod_id})

        elif choice == "5":
            run_query("""
                SELECT pi.prod_name, AVG(r.rating)
                FROM review r
                JOIN product_ p ON r.prod_id = p.prod_id
                JOIN product_info pi ON p.prod_info_id = pi.prod_info_id
                GROUP BY pi.prod_name
            """)

        elif choice == "6":
            break

menu()

cursor.close()
conn.close()
