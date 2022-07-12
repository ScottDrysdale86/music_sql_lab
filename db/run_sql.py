import psycopg2 as pg2
import psycopg2.extras as ext


def run_sql(sql, values=None):
    conn = None
    results = []
    try:
        conn = pg2.connect("dbname='music_app'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, pg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results