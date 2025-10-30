from db import get_connection

def check_health():
    try:
        conn = get_connection()
        conn.close()
        return {"status": "healthy", "message": "MSSQL connection successful!"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
