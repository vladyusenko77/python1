import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def dbpostgress():
    conn = psycopg2.connect(database="test", user="vlad",
                            password="root", host="127.0.0.1", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = conn.cursor()
    sql = "CREATE DATABASE test"
    sql = "CREATE TABLE IF NOT EXISTS account(cardnumber serial PRIMARY KEY,name VARCHAR(50) NOT NULL,surname VARCHAR(50) NOT NULL,amount FLOAT(10) NOT NULL,currancy VARCHAR (10) NOT NULL)"
    cursor.execute(sql)
    conn.commit()
    print("Working")
    return conn


def add_card(cardnumber, name, surname, amount, currancy):
    db = dbpostgress()
    cursor = db.cursor()
    sql = "INSERT INTO account (cardnumber,name, surname, amount, currancy ) VALUES (%s,%s,%s,%s,%s)"
    val = (cardnumber, name, surname, amount, currancy)
    cursor.execute(sql, val)
    db.commit()
    db.close()
    print(cursor.rowcount, "CARD added")
