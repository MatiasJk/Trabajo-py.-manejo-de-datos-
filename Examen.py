import datetime
import pandas as pd

def validar_empleado(lista_empleados, validar):
    try:
        if buscar_empleado(lista_empleados, validar)!= False:
            return True
        elif buscar_empleado_id(lista_empleados, validar) != False:
            return True
        else:
            return False
    except AttributeError:
        print('El empleado no existe')

def buscar_empleado(lista_empleados, buscando):
    for emp in lista_empleados:
        if emp.get('nombre').lower() == buscando.lower():
            return emp
    return False

def buscar_empleado_id(lista_empleados, buscando):
    for emp in lista_empleados:
        if emp.get('id') == buscando:
            return emp
    return False

def validar_fecha(fecha_str):
    try:
        datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def imprimir_empleado(emps, search):
    if search == int:
        emp = buscar_empleado_id(emps, search)
    else:
        emp = buscar_empleado(emps, search)
    dataf = pd.DataFrame([emp])
    print(dataf.T)


#**************************
#diccionario de muestra
#**************************
empleados = [{
    'nombre' : 'Matias',
    'id' : 0,
    'cargo' : 'Practica',
    'Departamento' : 'developers',
    'Salario' : 100000,
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
                Salario = float(salario)
            except ValueError:
                print("Debe ingresar un id y/o salario valido")
            #Validamos que nada este vacío
            if (nombre and N_identificacion and cargo and departamento
                    and salario and fecha and type(N_identificacion) == int
                    and type(salario) == int and validar_fecha(fecha)):
                #Se ingresan los inputs al diccionario y se agrega en el array empleados, salimos del bucle
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

    elif opcion == 2:
        buscar = input("Ingrese el nombre o id del empleado: ")
        #validamos si es que se busca por ID
        try:
            buscar_id = int(buscar)
            if buscar_id >= 0:
                imprimir_empleado(empleados, buscar_id)
            else:
                print("no puede ingresar id negativo")
        except ValueError:
            if  len(buscar) > 2:
                imprimir_empleado(empleados, buscar)
            else:
                print("El empleado ",buscar," no existe")
    elif opcion == 3:
        buscar = input("Ingrese el nombre o id del empleado: ")
    elif opcion == 4:

    elif opcion == 5:
        print("Bye Bye")
        programa = False
    else:
        print("opción no valida")



