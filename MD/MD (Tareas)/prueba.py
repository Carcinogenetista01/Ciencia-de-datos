import requests
from bs4 import BeautifulSoup

def obtener_cartelera(dia):
    url_base = 'https://www.cinetecanacional.net/sedes/cartelera.php?cinemaId=003&dia='
    url = url_base + dia
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        peliculas = []

        peliculas_contenedor = soup.find_all('div', class_='col-12 col-md-6 col-lg-4 float-left')

        for pelicula in peliculas_contenedor:
            try:
                titulo = pelicula.find('p', class_='font-weight-bold text-uppercase text-decoration-none text-black').get_text(strip=True)
                print(f"Procesando película: {titulo}")

                # Obtener todos los horarios de la película
                horarios = []
                horarios_divs = pelicula.find_all('p', class_='pb-1 small')
                for horarios_div in horarios_divs:
                    print("Contenedor de horarios encontrado")
                    a_tags = horarios_div.find_all('a')
                    for a in a_tags:
                        horario = a.get_text(strip=True)
                        print(f"Horario encontrado: {horario}")
                        if ':' in horario:  # Verifica que el horario tiene formato de hora
                            horarios.append(horario)

                # Obtener información de la película
                info_pelicula = pelicula.find('div', class_='small').get_text(strip=True)
                duracion_str = info_pelicula.split("Dur.:")[-1].split("mins")[0].strip()
                duracion = int(duracion_str)

                # Agregar todos los horarios a la lista de películas
                for horario in horarios:
                    peliculas.append({
                        'titulo': titulo,
                        'horario_inicio': horario,
                        'duracion': duracion
                    })

            except Exception as e:
                print(f"Error al procesar película: {e}")
                continue

        return peliculas
    else:
        print(f"Error al acceder a la página, código de estado: {response.status_code}")
        return []

# Ejemplo de uso
dia = '2024-09-12'
cartelera = obtener_cartelera(dia)
for pelicula in cartelera:
    print(pelicula)
