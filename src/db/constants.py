from urllib.parse import quote_plus

password = quote_plus("%0.}7Y1h-;R*@O")
SQLALCHEMY_DATABASE_URL = f"postgresql://gen_user:{password}@147.45.237.134:5432/orders"