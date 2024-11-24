from .postgresql_connection import PostgresConn

def get_last_blocks(last_n = 7):
    cn = PostgresConn() 
    session = cn.get_cursor_to_pg()

    session.execute(f"select block_id, block_hash, block_time, block_difficulty, fee_total, transactions_count, avg_fee_per_trx, row_number() over(order by block_id desc) as rn from processed_blocks order by block_id desc limit {str(last_n)}")
    blocks = session.fetchall()

    return blocks