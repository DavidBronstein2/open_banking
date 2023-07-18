from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('postgresql://davidbron:Mdavid2003@localhost:5432/davidbron')

# test the connection by executing a simple query
with engine.connect() as conn:
    stmt = text("SELECT 1")
    result =  conn.execute(stmt)
    print(result.fetchone()) 