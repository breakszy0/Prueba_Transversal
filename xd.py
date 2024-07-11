import random
import statistics
import csv

# Lista de nombres de empleados
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para generar sueldos aleatorios para los empleados
def asignar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

# Función para clasificar los sueldos
def clasificar_sueldos(sueldos):
    sueldo_menor = []
    sueldo_intermedio = []
    sueldo_mayor = []
    
    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        if sueldo < 800000:
            sueldo_menor.append((nombre, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            sueldo_intermedio.append((nombre, sueldo))
        else:
            sueldo_mayor.append((nombre, sueldo))
    
    # Imprimir clasificación
    print("Sueldos menores a $800.000\nTOTAL:", len(sueldo_menor))
    for nombre, sueldo in sueldo_menor:
        print(f"{nombre} ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000\nTOTAL:", len(sueldo_intermedio))
    for nombre, sueldo in sueldo_intermedio:
        print(f"{nombre} ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000\nTOTAL:", len(sueldo_mayor))
    for nombre, sueldo in sueldo_mayor:
        print(f"{nombre} ${sueldo}")
    
    # Calcular y mostrar total de sueldos
    total_sueldos = sum(sueldo for _, sueldo in sueldos)
    print("\nTOTAL SUELDOS: $", total_sueldos)

# Función para mostrar estadísticas de sueldos
def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio_sueldos = statistics.mean(sueldos)
    media_geom = statistics.geometric_mean(sueldos)
    
    print("\nEstadísticas de Sueldos:")
    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica: ${media_geom:.2f}")

# Función para generar reporte de sueldos
def reporte_sueldos(sueldos):
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        
        for i, sueldo in enumerate(sueldos):
            nombre = trabajadores[i]
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([nombre, sueldo, descuento_salud, descuento_afp, sueldo_liquido])

# Función principal que ejecuta el programa
def main():
    sueldos = []
    
    while True:
        print("\n----- Menú Principal -----")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sueldos = asignar_sueldos_aleatorios()
            print("Sueldos asignados aleatoriamente.")
        
        elif opcion == '2':
            if sueldos:
                clasificacion = clasificar_sueldos(sueldos)
                for categoria, empleados in clasificacion.items():
                    print(f"{categoria} TOTAL: {len(empleados)}")
                    for empleados, sueldo in empleados:
                        print(f"{empleados} ${sueldo}")
            else:
                print("Primero debe asignar los sueldos aleatorios.")
        
        elif opcion == '3':
            if sueldos:
                ver_estadisticas(sueldos)
            else:
                print("Primero debe asignar los sueldos aleatorios.")
        
        elif opcion == '4':
            if sueldos:
                reporte_sueldos(sueldos)
                print("Reporte de sueldos generado en 'reporte_sueldos.csv'")
            else:
                print("Primero debe asignar los sueldos aleatorios.")
        
        elif opcion == '5':
            print("Saliendo del programa...  Desarrollado por Alfredo Ibaceta RUT 21.532.161-4")
            break
        
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()
