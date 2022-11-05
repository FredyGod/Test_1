import psycopg2
from config import host, user, password, db_name

try:
    con = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    con.autocommit = True
    with con.cursor() as cur:
        cur.execute(
            '''SELECT title, COUNT(brand_idd) FROM notebooks_notebook GROUP BY title ORDER BY COUNT(brand_id) DESC''',
        )
        cur.execute(
            '''SELECT brand_id, COUNT(diagonal) FROM notebooks_notebook WHERE diagonal >= 14 GROUP BY bran_id ORDER BY COUNT(width) DESC''',
        )
        r = cur.fetchall()
        print(r)

except Exception as ex:
    print('Error working with PostgreSQL', ex)
finally:
    if con:
        con.close()
        print('PostgreSQL connection closed')
