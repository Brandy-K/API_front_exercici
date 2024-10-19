from typing import List

# Schema for a single alumne (student)
def alumne_schema(fetchAlumnes) -> dict:
    return {
        "NomAlumne": fetchAlumnes[0],
        "Cicle": fetchAlumnes[1],
        "Curs": fetchAlumnes[2],
        "Grup": fetchAlumnes[3],
        "DescAula": fetchAlumnes[4],  # Ensure this field exists in the fetchAlumnes result
    }

# Schema for a list of alumne (students)
def alumnes_schema(fetchAlumnes) -> List[dict]:
    return [alumne_schema(alum) for alum in fetchAlumnes]  # Process each alum in the result

# Schema for a single aula (classroom)
def aula_schema(aula) -> dict:
    return {
        "IdAula": aula[0],
        "DescAula": aula[1],
        "Edifici": aula[2],
        "Pis": aula[3],
    }

# Schema for a list of aula (classrooms)
def aulas_schema(fetchAules) -> List[dict]:
    return [aula_schema(aula) for aula in fetchAules]  # Process each aula in the result
