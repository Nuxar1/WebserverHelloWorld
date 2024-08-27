from fastapi import FastAPI
import psycopg

conn = psycopg.connect(host="db", user="postgres", password="postgres")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/db_test")
def read_db_test():
    # Missing
    with conn.cursor() as cur:
        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test")

        # Make the changes to the database persistent
        conn.commit()

        return cur.fetchall()

@app.get("/key_login")
async def key_login(key: str):
    if not key.isalnum():
        return {"error": "Invalid key"}
    
    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM keys WHERE key = %s", (key,))

        if cur.rowcount == 0:
            return {"error": "Invalid key"}
        
        return {"success": "Logged in!"}