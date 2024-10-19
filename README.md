##Explicacio

##main.py
És el punt d'entrada de l'aplicació fastapi.
Conté el CORS middleware i defineix els endpoints.
##alumnat.py
Conté funcions que interactuen amb la base de dades per obtenir dades dels estudiants.
`read()`: estableix una connexió de base de dades, recupera les dades de l'estudiant de la base de dades i les retorna com a llista d'instàncies de `tablaAlumne`.
##alumne.py
Defineix esquemes per a les dades dels estudiants.
Alumne_schema converteix les dades dels estudiants de tuple en un diccionari.
Alumnes_schema()`: processa una llista de dades de l'estudiant en una llista de diccionaris.
Aula_schema()` i `aulas_schema()`: (S'assumeix que es defineixen de manera similar per a les dades de l'aula si s'utilitzen).
##models.py
Conte els Pydantic que defineixen l-estrucutura de dates dels almunes i aula.

