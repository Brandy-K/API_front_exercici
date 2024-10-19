from client import db_client
from fastapi import HTTPException

def read():
    conn = db_client()
    if isinstance(conn, dict) and conn.get("status") == -1:
        return conn  # Return the error from db_client

    try:
        cur = conn.cursor()
        # Only select the required fields
        cur.execute(
            "SELECT NomAlumne, Cicle, Curs, Grup, DescAula "
            "FROM alumne JOIN aula ON alumne.IdAula = aula.IdAula"
        )
        alumnes = cur.fetchall()
    except Exception as e:
        return {"status": -1, "message": f"Query error: {e}"}
    finally:
        if conn:
            conn.close()

    return alumnes



def read_id(IdAlumne):
    conn = db_client()

    # Check if the connection returned an error
    if isinstance(conn, dict) and conn.get("status") == -1:
        return conn  # Return the error from db_client

    try:
        with conn.cursor() as cur:
            query = (
                "SELECT NomAlumne, Cicle, Curs, Grup, DescAula "
                "FROM alumne JOIN aula ON alumne.IdAula = aula.IdAula "
                "WHERE IdAlumne = %s"
            )
            value = (IdAlumne,)
            cur.execute(query, value)
            alumn = cur.fetchone()
    except Exception as e:
        return {"status": -1, "message": f"Query error: {e}"}
    finally:
        if conn:
            conn.close()

    return alumn


def add_alumne(IdAlumne: int, IdAula: int, NomAlumne: str, Cicle: str, Curs: str, Grup: str):
    conn = db_client()

    # Check if the connection returned an error
    if isinstance(conn, dict) and conn.get("status") == -1:
        raise HTTPException(status_code=400, detail=f"Connection error: {conn.get('message')}")

    try:
        cur = conn.cursor()
        query = """
            INSERT INTO alumne (IdAlumne, IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt)
            VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())
        """
        values = (IdAlumne, IdAula, NomAlumne, Cicle, Curs, Grup)
        cur.execute(query, values)
        conn.commit()
        alumna_id = cur.lastrowid
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding alumne: {e}")
    finally:
        if conn:
            conn.close()

    return alumna_id
