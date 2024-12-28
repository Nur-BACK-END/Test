CREATE_TABLE_products = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    size text,
    category text,
    price text,
    product_id text,
    photo text
    )
"""

INSERT_products_QUERY = """
    INSERT INTO products (name,size, category, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""



CREATE_TABLE_client = """
    CREATE TABLE IF NOT EXISTS client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id text,
    size text,
    quantity text,
    number text
    )
"""

INSERT_client_QUERY = """
    INSERT INTO client (product_id, size, quantity, number) 
    values (?, ?, ?, ?)
"""