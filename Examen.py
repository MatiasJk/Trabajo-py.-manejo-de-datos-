import datetime
import pandas as pd

def validar_busqueda(emps, buscar_emp):
    try:
        buscar_emp = int(buscar_emp)
        if buscar_emp >= 0:
            buscando_emp = validar_empleado(emps, buscar_emp)
            return buscando_emp
        else:
            print("no puede ingresar id negativo")
            return False
    except ValueError:
        if len(buscar_emp) > 2:
            buscando_emp = validar_empleado(emps, buscar_emp)
            return buscando_emp
        else:
            print("El empleado ", buscar_emp, " no existe")
            return False

def validar_empleado(lista_empleados, validar):
    if isinstance(validar, int):
        return buscar_empleado_id(lista_empleados, validar)

    else:
        return buscar_empleado(lista_empleados, validar)

def buscar_empleado(lista_empleados, buscando):
    for emp_name in lista_empleados:
        if emp_name.get('nombre').lower() == buscando.lower():
            return emp_name
    return False

def buscar_empleado_id(lista_empleados, buscando):
    for emp_id in lista_empleados:
        if emp_id.get('id') == buscando:
            return emp_id
    return False

def validar_fecha(fecha_str):
    try:
        datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def imprimir_empleado(emps, search):
    if search == int:
        emp_id = buscar_empleado_id(emps, search)
        dataf = pd.DataFrame([emp_id])
    else:
        emp_name = buscar_empleado(emps, search)
        dataf = pd.DataFrame([emp_name])
    print(dataf.T)

#**************************
#diccionario de muestra
#**************************
empleados = [{
    'nombre' : 'Matias',
    'id' : 0,
    'cargo' : 'Practica',
    'departamento' : 'developers',
    'salario' : 100000,
    'fecha de contratación' : '02-09-2025'}

]
#**************************
#Inicio menu
#**************************
programa = True
while programa:
    #aseguramos que la elección sea solo numerica
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
    #*************************
    #Ingresar nuevo empleado
    #*************************
    if opcion == 1:
        #Diccionario en blanco para agregar posteriormente a "empleados"
        nuevo_empleado = {}
        in_datos = True
        #bucle de ingreso de datos
        while in_datos:
            nombre = input("Ingrese el nombre del empleado: ").strip()
            N_identificacion = input("Ingrese el id del empleado: ").strip()
            cargo = input("Ingrese el cargo del empleado: ").strip()
            departamento = input("Ingrese el departamento: ").strip()
            salario = input("Ingrese el salario: ").strip()
            fecha = input("Ingrese la fecha de contratación:").strip()
            #se valida si la id y el salario se ingresan como int
            try:
                N_identificacion = int(N_identificacion)
                salario_num = float(salario)
                if (nombre and N_identificacion and cargo and departamento
                        and salario and fecha and type(N_identificacion) == int
                        and type(salario_num) in (int, float) and validar_fecha(fecha)):
                    # Se ingresan los inputs al diccionario y se agrega en el array empleados, salimos del bucle
                    nuevo_empleado['nombre'] = nombre
                    nuevo_empleado['id'] = N_identificacion
                    nuevo_empleado['cargo'] = cargo
                    nuevo_empleado['departamento'] = departamento
                    nuevo_empleado['salario'] = salario
                    nuevo_empleado['fecha'] = fecha
                    empleados.append(nuevo_empleado)
                    in_datos = False
                else:
                    print("no debe dejar datos vacíos ni inválidos, intente de nuevo.")
            except ValueError:
                print("Debe ingresar un id y/o salario valido")
            #Validamos que nada este vacío

    #*************************
    #Mostrar empleado
    #*************************
    elif opcion == 2:
        buscar = input("Ingrese el nombre o id del empleado: ")
        #validamos si es que se busca por ID
        validar_busqueda(empleados, buscar)
    #********************************
    #Actualizar información empleado
    #********************************
    elif opcion == 3:
        buscar_act = input("Ingrese el nombre o id del empleado: ")
        emp = validar_busqueda(empleados, buscar_act)
        cambio = True
        if not emp:
            cambio = False
        while cambio:
            try:
                opcion = int(input(f"Editando empleado: {emp['nombre']} (ID: {emp['id']})\n"
                                   f"que desea cambiar?\n"
                                   '1. Salario\n'
                                   '2.Departamento\n'
                                   '3.cargo\n'
                                   '4.Salir'))

            except ValueError:
                print("Debes ingresar un número")
                continue
            if opcion == 1:
                try:
                    emp["salario"] = float(input("Ingrese el salario nuevo: "))
                except ValueError:
                    print("Salario no válido")
            elif opcion == 2:
                new_departamento = input("Ingrese el nuevo departamento: ").strip()
                if new_departamento:
                    emp["departamento"] = new_departamento
                else:
                    print("no puede dejar el campo vacío")
            elif opcion == 3:
                new_cargo = input("Ingrese el nuevo cargo: ").strip()
                if new_cargo:
                    emp["cargo"] = new_cargo
                else:
                    print("no puede dejar el campo vacío")
            elif opcion == 4:
                print("Saliendo del editor...")
                cambio = False

            else:
                print("Empleado inexistente")
    #************************
    #Eliminar empleado
    #************************
    elif opcion == 4:
        buscar_del = input("Ingrese el nombre o id del empleado a eliminar: ").strip()
        eliminado = validar_busqueda(empleados, buscar_del)
        if eliminado != False:
            try:
                buscar_del = int(buscar_del)
                for i in range(len(empleados)):
                    if empleados[i]['id'] == eliminado ['id']:
                        del empleados[i]
                        print("El empleado ",eliminado['nombre']," ya no existe")
            except ValueError:
                for i in range(len(empleados)):
                    if empleados[i]['nombre'] == eliminado ['nombre']:
                        del empleados[i]
                        print("El empleado ",eliminado['nombre']," ya no existe")

    #*******************
    #Salir del programa
    #*******************
    elif opcion == 5:
        print("Bye Bye")
        programa = False
    else:
        print("opción no valida")



