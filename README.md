# CalculadoraPresupuestoViajeSimple

Aqui puse en practica conocimientos que vimos el lunes 09/06/25 en clases (try/except), 
el truncar al decimal exacto y algunas validaciones de datos se que se pidieron datos de entrada int, float y str por separado,
pero queria darle mayor complejidad al codigo y practicar cosas nuevas, como por ejemplo:

- 1.- Realizar un comprobar para cada caso, para numeros de tipo "int" y "float":
        - a) Para que ambos casos solo validara que sea mayor que 0 y del tipo que se especifica.
        - b) Retornar el dato comprobado con su respectivo valor pedido inicialmente.

    - Y para el caso del tipo "str":
        - a) Validar que la cadena no sea vacia y mostrar los datos con cada inicial en mayuscula.
        - b) Validar que los datos fueron si o no explicito.

    - Además el uso de la variable "flag" es para identificar en que caso nos encontramos y realizar las acciones segun 
    corresponda el tipo de dato y condicion, utilicé "title()" para formatear el nombre y "strip()" para eliminar los espacios

- 2.- Pedir y almacenar datos en una funcion, además de llamar la funcion "comprobar"
    para validar los datos y retornar las variables
    y desempaquetarlas al llamar la funcion en el main.

- 3.- En vez de mostrar los datos en el main, cree una función para que haga los prints y luego llamarla en el main,
    - EXTRA en esta funcion, queria intentar probar esta comprobacion de muestra de datos "'Sí' if tour == 'si' else 'No'"
    ya que se puede usar en C desde la siguiente sintaxis: "(condicion) ? (caso 1) : (caso 2);" entonces queria ver si se aplicaba en Python.
    Para mostrar los numeros en el formato "123.123.123,12" utilicé el formateo de numeros ":,.(numero)f".
