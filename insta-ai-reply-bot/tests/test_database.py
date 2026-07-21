from sqlalchemy import text
from memory.database import get_session


db = get_session()

result = db.execute(
    text("SELECT now();")
)

print(result.fetchone())

db.close()