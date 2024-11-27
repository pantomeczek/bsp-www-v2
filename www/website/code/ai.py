from .postgresql_connection import PostgresConn


QUERY = """
select analysis_date, analysis_content
  from ai_analysis
 where analysis_type = '##ANALYSISTYPE##'
   and analysis_date = (select max(analysis_date) from ai_analysis where analysis_type = '##ANALYSISTYPE##');
"""


def get_ai_summary(analysis_type):

    cn = PostgresConn()
    try:
        session = cn.get_cursor_to_pg()       
        session.execute(QUERY.replace('##ANALYSISTYPE##', analysis_type))
        result = session.fetchone()

        cn.close_connection()

        if result is not None:
            return {"date": result[0], "content": result[1]}
        else:
            return None
    except:
        return None
