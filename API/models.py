from pydantic import BaseModel

class alumn(BaseModel):  
    IdAlumne: int
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    CreatedAt: str
    UpdatedAt: str
    
class tablaAlumne(BaseModel): #changed from Alumne to tablaAlumne
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    DescAula: str
   

class Aula(BaseModel):
    IdAula: int
    DescAula: str
    Edifici: str
    Pis: str
