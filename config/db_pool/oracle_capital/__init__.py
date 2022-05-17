import cx_Oracle
from flask import current_app


def get_connect():
    cx_Oracle.init_oracle_client(lib_dir=current_app.config.get("ORACLE_CAPITAL_DIR"))
    return cx_Oracle.connect(user=current_app.config.get("WALLET_USER"),
                             password=current_app.config.get("WALLET_PASSWD"),
                             dsn=current_app.config.get("WALLET_DSN"),
                             encoding="UTF-8")


def get_cur():
    return get_connect().cursor()
