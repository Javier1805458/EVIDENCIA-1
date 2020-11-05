global ListaDeAlumnos
ListaDeAlumnos = list()

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
    Archivo = open("ArchivoAlumnos.txt", "w")
    Archivo.write(f'Matricula: {Alumno.Matricula}  -  Alumno: {Alumno.NombreCompleto}  -  Promedio final: {Alumno.Promedio} ')
    Archivo.close()
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
        print('5- Salir del sistema')
        
        Opcion = input('\nElige una opcion: ')
        
        if Opcion == '1':
            AgregarAlumno()
        elif Opcion == '2':
            ListarAlumnos()
        elif Opcion == '3':
            BuscarAlumno()
        elif Opcion == '4':
            ModificarAlumno()
        else:
            i = 1

Menu()
            
            