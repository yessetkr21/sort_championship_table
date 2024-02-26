class Equipo:
  def __init__(self, nombre, puntos, goles_marcados, goles_en_contra):
      self.nombre = nombre
      self.puntos = puntos
      self.goles_marcados = goles_marcados
      self.goles_en_contra = goles_en_contra

  def diferencia_goles(self):
      return self.goles_marcados - self.goles_en_contra

def ordenar_tabla_burbuja(tabla):
  n = len(tabla)

  for i in range(n):
      for j in range(0, n-i-1):
          # Compare puntos, diferencia de goles y goles marcados
          if (tabla[j].puntos, tabla[j].diferencia_goles(), tabla[j].goles_marcados) < (tabla[j+1].puntos, tabla[j+1].diferencia_goles(), tabla[j+1].goles_marcados):
              tabla[j], tabla[j+1] = tabla[j+1], tabla[j]

  return tabla

def imprimir_tabla(tabla):
  print("{:<10} {:<7} {:<15} {:<15} {:<15}".format("Equipo", "Puntos", "Dif. de Goles", "Goles Marcados", "Goles en Contra"))
  for i, equipo in enumerate(tabla, start=1):
      print("{:<10} {:<7} {:<15} {:<15} {:<15}".format(equipo.nombre, equipo.puntos, equipo.diferencia_goles(), equipo.goles_marcados, equipo.goles_en_contra))

def main():
  equipos = []
  num_equipos = int(input("Ingrese el número de equipos: "))
  for _ in range(num_equipos):
      nombre = input("Nombre del equipo: ")
      puntos = int(input("Puntos: "))
      goles_marcados = int(input("Goles marcados: "))
      goles_en_contra = int(input("Goles en contra: "))
      equipos.append(Equipo(nombre, puntos, goles_marcados, goles_en_contra))

  # Utilice el algoritmo de ordenamiento burbuja
  tabla_ordenada = ordenar_tabla_burbuja(equipos)

  print("\nTabla de Posiciones:")
  imprimir_tabla(tabla_ordenada)

if __name__ == "__main__":
  main()
