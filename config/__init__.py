import os
from dotenv import load_dotenv
from core.odoorpc import OdooRPC

load_dotenv()

# Odoo server setup
ODOO_URL = os.getenv("ODOO_URL")
ODOO_DB = os.getenv("ODOO_DB")
ODOO_USERNAME = os.getenv("ODOO_USERNAME")
ODOO_PASSWORD = os.getenv("ODOO_PASSWORD")

# Odoo RPC Client
odoo = OdooRPC(
    ODOO_URL,
    ODOO_DB,
    ODOO_USERNAME,
    ODOO_PASSWORD,
)
