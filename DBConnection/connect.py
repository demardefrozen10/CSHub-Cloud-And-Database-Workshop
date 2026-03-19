import os

import oracledb


def get_connection() -> oracledb.Connection:
    return oracledb.connect(
        user=os.getenv("ORACLE_USER", ""),
        password=os.getenv("ORACLE_PASSWORD", ""),
        host=os.getenv("ORACLE_HOST", ""),
        port=int(os.getenv("ORACLE_PORT", "")),
        service_name=os.getenv("ORACLE_SERVICE", ""),
    )


'''
if __name__ == "__main__":
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT table_name FROM user_tables ORDER BY table_name")
            print(cur.fetchone())
'''