from .postgresql_connection import PostgresConn
from datetime import timedelta, datetime

def get_last_blocks(last_n = 7):
    cn = PostgresConn() 
    session = cn.get_cursor_to_pg()

    session.execute(f"select block_id, block_hash, block_time, block_difficulty, fee_total, transactions_count, avg_fee_per_trx, row_number() over(order by block_id desc) as rn from processed_blocks order by block_id desc limit {str(last_n)}")
    blocks = session.fetchall()

    processed_blocks = []

    for i in blocks:
        minutes = (datetime.utcnow() - i[2]).total_seconds() / 60

        diff_val = 0
        diff_unit = ""

        if minutes < 60:
            diff_val = int(minutes)
            diff_unit = "minutes"
        else:
            diff_val = int(minutes/60)
            diff_unit = "hour" if diff_val == 1 else "hours"

        processed_blocks.append(
            {
                "block_id": i[0],
                "block_hash": i[1],
                "block_time": i[2],
                "block_time_full": i[2].strftime("%B %d, %Y %I:%M %p (UTC)"),
                "block_time_diff": f"{diff_val} {diff_unit} ago",
                "block_difficulty": i[3],
                "fee_total": i[4],
                "transactions_count": i[5],
                "avg_fee_per_trx": i[6],
                "rn": i[7],
            }
            
        )

    

    return processed_blocks