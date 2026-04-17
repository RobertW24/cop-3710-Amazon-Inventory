import oracledb

# Address of instantclient
oracledb.init_oracle_client(lib_dir=r"C:\Users\mtkg8\OneDrive\Desktop\instantclient_23_0")

#Database system login stuff
conn = oracledb.connect(
    user="system",
    password="123abc",
    dsn=oracledb.makedsn("localhost", 1521, sid="xe")
)

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
