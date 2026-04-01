BEGIN
  FOR c IN (SELECT table_name FROM user_tables) LOOP
    EXECUTE IMMEDIATE ('DROP TABLE "' || c.table_name || '" CASCADE CONSTRAINTS');
  END LOOP;
END;
/

CREATE TABLE supplier (
sup_id NUMBER PRIMARY KEY NOT NULL,
sup_name VARCHAR2(20) NOT NULL,
supply_price NUMBER(12,2) NOT NULL, 
lead_time VARCHAR2(10) NOT NULL
);

CREATE TABLE price (
price_id NUMBER PRIMARY KEY NOT NULL,
normal_price FLOAT NOT NULL,
discount_percentage FLOAT NOT NULL,
discounted_price FLOAT NOT NULL
);

CREATE TABLE product_info (
prod_info_id NUMBER PRIMARY KEY NOT NULL,
price_id NUMBER NOT NULL,
prod_name VARCHAR2(500) NOT NULL,
category VARCHAR2(200) NOT NULL,
descript VARCHAR2(3000) NOT NULL
);

CREATE TABLE product_ (
prod_id VARCHAR2(20) PRIMARY KEY NOT NULL,
prod_info_id NUMBER NOT NULL,
sup_id NUMBER NOT NULL,
img_link VARCHAR2(300) NOT NULL,
prod_link VARCHAR2(300) NOT NULL,
rev_count NUMBER NOT NULL,
avg_rating FLOAT NOT NULL
);

CREATE TABLE customer (
cus_id VARCHAR2(300) PRIMARY KEY NOT NULL,
cus_name VARCHAR2(200) NOT NULL
);

CREATE TABLE review (
prod_id VARCHAR2(20) NOT NULL,
cus_id VARCHAR2(1000) NOT NULL,
rev_title VARCHAR2(1000) NOT NULL,
rev_body VARCHAR2(4000) NOT NULL,
rating NUMBER NOT NULL,

PRIMARY KEY (prod_id, cus_id)
);




ALTER TABLE product_
ADD CONSTRAINT fk_product_product_info
FOREIGN KEY (prod_info_id)
REFERENCES product_info (prod_info_id);

ALTER TABLE product_
ADD CONSTRAINT fk_product_supplier
FOREIGN KEY (sup_id)
REFERENCES supplier (sup_id);

ALTER TABLE product_info
ADD CONSTRAINT fk_product_info_price
FOREIGN KEY (price_id)
REFERENCES price (price_id);

ALTER TABLE review
ADD CONSTRAINT fk_review_product_
FOREIGN KEY (prod_id)
REFERENCES product_ (prod_id);

ALTER TABLE review
ADD CONSTRAINT fk_review_customer
FOREIGN KEY (cus_id)
REFERENCES customer (cus_id);

