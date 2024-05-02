sql commands : 


- create DATABASE shopclassy;
- create user shopclassy with ENCRYPTED PASSWORD '*******';
- GRANT all privileges on database shopclassy to shopclassy;
- CREATE TABLE Authentication (username VARCHAR(255) PRIMARY KEY,password VARCHAR(255) NOT NULL,
    isadmin INT NOT NULL);
- INSERT INTO authentication (username, password, isadmin)VALUES ('boopesh', 'boo', 1);
- GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE authentication TO shopclassy;
- CREATE TABLE products (product_id VARCHAR(255),product_name VARCHAR(255),
    price VARCHAR(20),quantity INT);
- INSERT INTO products (product_id, product_name, price, quantity)VALUES ('1001', 'Iphone 13 pro Max', 1400.99, 10);
- GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE products TO shopclassy;
- CREATE TABLE cart (cart_id SERIAL PRIMARY KEY,product_id INTEGER NOT NULL,quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (product_id));
- GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE cart TO shopclassy;
- GRANT USAGE, SELECT ON SEQUENCE cart_cart_id_seq TO shopclassy; - IN CASE OF serial sequence isnt working


Docker commands :

- docker run -d --name postgresCont -p 5432:5432 -e POSTGRES_PASSWORD=pass013 postgres
- docker exec -it mypostgres psql -U postgres - to connect to the bash of logged on to the psql
   
