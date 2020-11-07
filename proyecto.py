global ListaDeAlumnos
global ListaDePromedios

ListaDeAlumnos = list()
ListaDePromedios = list()


class Sistema:
    Matricula = ""
    Nombre = ""
    ApellidoP = ""
    ApellidoM = ""
    NombreCompleto = ""
    Nota1 = 0
    Nota2 = 0
    Nota3 = 0
    
def AgregarAlumno():
    
    Alumno = Sistema()
    print('REGISTRO DE ALUMNO')
    
    Alumno.Matricula = input('Matricula: ')
    Alumno.Nombre = input('Nombre: ')
    Alumno.ApellidoP = input('Apellido paterno: ')
    Alumno.ApellidoM = input('Apellido materno: ')
    Alumno.NombreCompleto = (('{} {} {}').format(Alumno.ApellidoP, Alumno.ApellidoM, Alumno.Nombre)).upper()
        
    Alumno.Nota1 = float(input('Calificacion de Programacion: '))
    Alumno.Nota2 = float(input('Calificacion de Matematicas: '))
    Alumno.Nota3 = float(input('Calificacion de Liderazgo: '))
    Alumno.Prom = (Alumno.Nota1 + Alumno.Nota2 + Alumno.Nota3)/3
    Alumno.Promedio = round(Alumno.Prom,1)
    
    ListaDeAlumnos.append(Alumno)
    Archivo = open("ArchivoAlumnos.txt", "a")
    Archivo.write(f'Matricula: {Alumno.Matricula}  -  Alumno: {Alumno.NombreCompleto}  -  Promedio final: {Alumno.Promedio} \n')
    Archivo.close()
    
    import shutil
    
    shutil.copy('ArchivoAlumnos.txt','archivos')
    
    
    
def ListarAlumnos():
    print('LISTA DE ALUMNOS')
    
    for Alumno in ListaDeAlumnos:
        print(f'Matricula: {Alumno.Matricula}  -  Alumno: {Alumno.NombreCompleto}  -  Promedio final: {Alumno.Promedio} ')
    
def  BuscarAlumno():
    print('BUSQUEDA DE ALUMNO')
    MatriculaABuscar = input('Introduce la matricula del alumno a buscar: ')
    
    for Alumno in ListaDeAlumnos:
        Encontrado = False
        if MatriculaABuscar == Alumno.Matricula:
             print(f'Matricula: {Alumno.Matricula}  -  Alumno: {Alumno.NombreCompleto}  -  Promedio final: {Alumno.Promedio} ')
             Encontrado = True
    if Encontrado == False:
        print('La matricula ingresada no pertenece a ningun alumno.')
    
def ModificarAlumno():
    print('Modificar ALUMNO')
    MatriculaABuscar = input('Introduce la matricula del alumno a modificar: ')
    
    for Alumno in ListaDeAlumnos:
        
        if MatriculaABuscar == Alumno.Matricula:             
             Alumno.Nota1 = float(input('Calificacion de Programacion: '))
             Alumno.Nota2 = float(input('Calificacion de Matematicas: '))
             Alumno.Nota3 = float(input('Calificacion de Liderazgo: '))
             Alumno.Prom = (Alumno.Nota1 + Alumno.Nota2 + Alumno.Nota3)/3
             Alumno.Promedio = round(Alumno.Prom,1)
    
             print('Modificacion exitosa')
             break
            
def MejorPromedio():
    import sys
    
    TuplaDePromedios = tuple(ListaDeAlumnos)
    
    for Alumno in ListaDeAlumnos:      
        ListaDePromedios.append(Alumno.Promedio)
        
    MejorProm = max(ListaDePromedios)
    
    for Alumno in ListaDeAlumnos:
        if MejorProm == Alumno.Promedio:
            Name = Alumno.NombreCompleto
        
    print(f'El mejor Promedio es: {MejorProm} que le pertenece a {Name}\n')
    
    print(type(TuplaDePromedios))
    print(f'El tamaño de la tupla de promedios es: {sys.getsizeof("TuplaDePromedios")} bytes')
    
    print(type(ListaDePromedios))
    print(f'El tamaño de la Lista de promedios es: {sys.getsizeof("ListaDePromedios")} bytes')
    
    
      

def Menu():
    i = 0
    
    while i < 1:
        print('----------------------')
        print("Menú del sistema")
        print('----------------------')
        
        print('1- Agregar Alumno')
        print('2- Lista de Alumnos')
        print('3- Buscar Alumnos')
        print('4- Modificar  Alumno')
        print('5- Mejor promedio')
        print('6- Borrar la lista')
        print('7- Salir del sistema')
        
        Opcion = input('\nElige una opcion: ')
        
        if Opcion == '1':
            AgregarAlumno()
            tecla = input('\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENÚ\n')
            
        elif Opcion == '2':
            ListarAlumnos()
            tecla = input('\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENÚ\n')
            
        elif Opcion == '3':
            BuscarAlumno()
            tecla = input('\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENÚ\n')
            
        elif Opcion == '4':
            ModificarAlumno()
            tecla = input('\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENÚ\n')
            
        elif Opcion == '5':
            MejorPromedio()     
            tecla = input('\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENÚ\n')
            
        elif Opcion == '6':
            import os
            
            os.unlink('ArchivoAlumnos.txt')
            ListaDeAlumnos = list()
            print("Lista eliminada, hay una copia de seguridad en la carpeta de archivos")
            tecla = input('\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENÚ\n')
            
        elif Opcion =='7':
            import os
            directorio_actual = os.getcwd()
            print(f'El directorio actual es: {directorio_actual}')
            i = 1
            

        else:
            print('Escriba un numero valido')
            tecla = input('\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENÚ\n')

Menu()
            
            