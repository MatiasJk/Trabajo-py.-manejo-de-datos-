import datetime


def validar_empleado(empleados,buscando):
    for empleado in empleados:
        if empleado.get('nombre') == buscando.lower() or empleado.get('id') == buscando.lower():
            return True
    return False

def validar_fecha(fecha_str):
    try:
        datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

empleados = [{
    'nombre' : 'Matias',
    'id' : 0,
    'cargo' : 'Practica',
    'Departamento' : 'developers',
    'Salario' : 100000,
    'fecha de contratación' : '02-09-2025'}

]
programa = True
while programa:
    try:
        opcion=int(input("bienvenido al programa, Que desea hacer hoy \n"
                         "1. Registrar empleado nuevo\n"
                         "2. Mostrar empleado\n"
                         "3. Actualizar información de empleado\n"
                         "4. Eliminar empleado\n"
                         "5. Salir"))

    except ValueError:
        print("Debes ingresar un número")
        continue

    if opcion == 1:
        nuevo_empleado = {}
        in_datos = True
        while in_datos:
            nombre = input("Ingrese el nombre del empleado: ").strip()
            N_identificacion = input("Ingrese el id del empleado: ").strip()
            cargo = input("Ingrese el cargo del empleado: ").strip()
            departamento = input("Ingrese el departamento: ").strip()
            salario = input("Ingrese el salario: ").strip()
            fecha = input("Ingrese la fecha de contratación:").strip()
            if (nombre and N_identificacion and cargo and departamento
                    and salario and fecha and type(N_identificacion) == int
                    and type(salario) == int and validar_fecha(fecha)):
                nuevo_empleado['nombre'] = nombre
                nuevo_empleado['id'] = N_identificacion
                nuevo_empleado['cargo'] = cargo
                nuevo_empleado['departamento'] = departamento
                nuevo_empleado['salario'] = salario
                nuevo_empleado['fecha'] = fecha
                empleados.append(nuevo_empleado)
                in_datos = False
            else:
                print("no debe dejar datos vacios ni invalidos, intente de nuevo.")

    elif opcion == 2:

    elif opcion == 3:
    elif opcion == 4:
    elif opcion == 5:
    else:
        print("opcion no valida")



