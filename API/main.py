from typing import List
from fastapi import FastAPI, HTTPException
import alumnat  # Import your database connection file
import alumne, aula    # Import your schema file for Alumne
from models import alumn
from models import tablaAlumne
from models import Aula
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Alumnat API"}

@app.get("/alumne/list", response_model=List[tablaAlumne])
def read_alumnes():
    return alumne.alumnes_schema(alumnat.read()) # Call to database function to read all alumnes
    # return alumne.alumne_schema(db_data)  
    
      # Convert the raw data to schema

@app.get("/alumne/{IdAlumne}", response_model=tablaAlumne)
def read_alumne_id(IdAlumne: int):
   # alumn = Alumnat.read_id(IdAlumne)
    if alumnat.read_id(IdAlumne) is not None:
        tablaAlumne =  alumne.alumne_schema(alumnat.read_id(IdAlumne))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return tablaAlumne

@app.post("/alumne/add", response_model=dict)
def add_alumne(alumne: alumn):
    # check if IdAula exists in Aula table
    if not alumnat.validate_id_aula(alumne.IdAula):
        raise HTTPException(status_code=400, detail="IdAula does not exist in Aula table")

    # Add the new alumne
    alumnat.add_alumne(alumne.IdAlumne, alumne.IdAula, alumne.NomAlumne, alumne.Cicle, 
        alumne.Curs, alumne.Grup)
    return {"message": "S'ha afegit correctament"}

@app.put("/alumne/update/{id}")
def update_alumne(id: int, alumne: alumn):
    # Check if the alumne exists
    existing_alumne = alumnat.read_id(id)
    if existing_alumne is None:
        raise HTTPException(status_code=404, detail="Alumne not found")
    
    # Validate IdAula if it's being updated
    if alumne.IdAula != existing_alumne[1]:
        if not alumnat.validate_id_aula(alumne.IdAula):
            raise HTTPException(status_code=400, detail="IdAula does not exist in Aula table")

    # Update the alumne in the database
    alumnat.update_alumne(
        id,
        alumne.IdAlumne,
        alumne.IdAula,
        alumne.NomAlumne,
        alumne.Cicle,
        alumne.Curs,
        alumne.Grup
    )
    return {"message": "S'ha modificat correctament"}

#to get aules
@app.get("/aules", response_model=List[dict])
def read_aules():
    db_data = aula.read_aules()
    return aula.aulas_schema(db_data)