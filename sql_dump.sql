CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR,
    customer_address VARCHAR,
    total_amount INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_details (
    id SERIAL PRIMARY KEY,
    serial_number VARCHAR,
    product_name VARCHAR,
    quantity INTEGER,
    order_id INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(id)
);


INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Charlie White', '202 Elm St', 944, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Jane Smith', '456 Oak St', 100, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Jane Smith', '101 Maple Ave', 212, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Bob Brown', '456 Oak St', 551, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Alice Johnson', '101 Maple Ave', 997, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Charlie White', '101 Maple Ave', 810, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Alice Johnson', '101 Maple Ave', 941, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Charlie White', '123 Main St', 649, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Bob Brown', '456 Oak St', 894, '2024-09-08 10:50:01');

INSERT INTO orders (customer_name, customer_address, total_amount, created_at) 
VALUES ('Charlie White', '456 Oak St', 774, '2024-09-08 10:50:01');

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1021', 'Monitor', 6, 3);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1031', 'Laptop', 7, 3);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1008', 'Keyboard', 9, 3);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1029', 'Monitor', 1, 1);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1010', 'Monitor', 4, 4);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1004', 'Tablet', 5, 5);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1007', 'Keyboard', 4, 10);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1024', 'Smartphone', 3, 8);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1040', 'Smartphone', 1, 8);

INSERT INTO order_details (serial_number, product_name, quantity, order_id) 
VALUES ('SN1041', 'Keyboard', 2, 10);
