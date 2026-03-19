import os

import oracledb


def get_connection() -> oracledb.Connection:
    return oracledb.connect(
        user=os.getenv("ORACLE_USER", "chud"),
        password=os.getenv("ORACLE_PASSWORD", "test123"),
        host=os.getenv("ORACLE_HOST", "172.202.113.49"),
        port=int(os.getenv("ORACLE_PORT", "1521")),
        service_name=os.getenv("ORACLE_SERVICE", "MYPDB"),
    )


'''
if __name__ == "__main__":
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT table_name FROM user_tables ORDER BY table_name")
            print(cur.fetchone())
'''