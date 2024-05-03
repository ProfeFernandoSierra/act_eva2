# act_eva2
ENUNCIADO
El instituto DOUK desea implementar un sistema informático para la gestión de sus alumnos, y
para ello, te solicitan que desarrolles lo especificado a continuación:
Se te solicita crear un menú en el cual se puedan registrar los datos de un alumno. Los
atributos que debe tener la ficha son los siguientes:
Rut (sin dígito verificador ni puntos).
Nombre
Dirección
Correo electrónico
Edad
NEM
FORMA: A
El menú debe tener las siguientes opciones:
Sistema de Gestión de Alumnos
1) Registrar Alumno
2) Consultar Datos de Alumno
3) Salir
Donde:
Registrar Alumno: Solicita todos los datos de un alumno para hacer el registro de una nueva
ficha. Cada uno de los atributos debe cumplir con lo solicitado mediante validación.
Nombre: no puede venir vacio
Direccion: no puede venir vacio
Rut: debe ser un número entero que se encuentre dentro del rango de 500000 y 39999999.
Edad: debe ser un número entero que se encuentre en el rango de 17 a 90.
Correo electrónico: debe ser una cadena de caracteres que contenga al menos un carácter
"@".
NEM: debe manipularse como si fuese un decimal.
Consultar Datos de Alumno:
Muestra por pantalla todos los atributos del alumno que coincida con el Rut ingresado.
Los datos se deben mostrar de forma ordenada, utilizando herramientas de tabulación
y/o saltos de línea según lo aprendido en clases (ver reglas de negocio más abajo).
Salir:
Sale del ciclo del menú y muestra un mensaje "Ha salido del sistema…".
Reglas de negocio:
Debe crear un usuario y una contraseña para el administrador, solo este usuario tiene
permisos de poder visualizar la opción 2
EJ: user: admin
pass: admin
En el resumen (opción 2) deberá desplegarse toda la información del alumno y si tiene un
NEM inferior a 5.2 el sistema deberá indicar
'alumno no cumple con requisitos’, caso contrario, 'alumno cumple con requisitos'