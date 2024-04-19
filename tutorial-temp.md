# REQL tutorial

TODO:Write a REQL tutorial here.

# Motivation of using REQL and REmatch

Suppose you want to do a linguistic analysis focused on the relations that Chile has with its neighboring countries. A possible starting point would be to analyze the Wikipedia page corresponding to the History of Chile. The article (from English Wikipedia) is provided in plain text format at chile_wiki.txt.


Chile, officially the Republic of Chile, is a country in western South America. It is the southernmost country in the world and the closest to Antarctica, stretching along a narrow strip of land between the Andes Mountains and the Pacific Ocean. With an area of 756,102 square kilometers (291,933 sq mi) and a population of 17.5 million as of 2017, Chile shares borders with Peru to the north, Bolivia to the northeast, Argentina to the east, and the Drake Passage to the south. The country also controls several Pacific islands, including Juan Fernández, Isla Salas y Gómez, Desventuradas, and Easter Island, and claims about 1,250,000 square kilometers (480,000 sq mi) of Antarctica as the Chilean Antarctic Territory. The capital and largest city of Chile is Santiago, and the national language is Spanish.

Spain conquered and colonized the region in the mid-16th century, replacing Inca rule, but failed to conquer the independent Mapuche people who inhabited what is now south-central Chile. Chile emerged as a relatively stable authoritarian republic in the 1830s after their 1818 declaration of independence from Spain. During the 19th century, Chile experienced significant economic and territorial growth, putting an end to Mapuche resistance in the 1880s and gaining its current northern territory in the War of the Pacific (1879–83) by defeating Peru and Bolivia. In the 20th century, up until the 1970s, Chile underwent a process of democratization and experienced rapid population growth and urbanization, while relying increasingly on exports from copper mining to support its economy. During the 1960s and 1970s, the country was marked by severe left-right political polarization and turmoil, which culminated in the 1973 Chilean coup d'état that overthrew Salvador Allende's democratically elected left-wing government. This was followed by a 16-year right-wing military dictatorship under Augusto Pinochet, which resulted in more than 3,000 deaths or disappearances. The regime ended in 1990, following a referendum in 1988, and was succeeded by a center-left coalition, which ruled until 2010.

Chile has a high-income economy and is one of the most economically and socially stable nations in South America, leading Latin America in competitiveness, per capita income, globalization, peace, and economic freedom. Chile also performs well in the region in terms of sustainability of the state and democratic development, and boasts the second lowest homicide rate in the Americas, following only Canada. Chile is a founding member of the United Nations, the Community of Latin American and Caribbean States (CELAC), and the Pacific Alliance, and joined the OECD in 2010.


(^|[\n.])!sentence{[^.\n]*((!y{Chile} [^.\n]*!z{(Peru|Argentina|Bolivia)})|(!z{(Peru|Argentina|Bolivia)} [^.\n]*!y{Chile}))[^.\n]*\.}

######

[1]
0s
with open('chile_wiki.txt') as file:
    text = file.read()

Suponga ahora que usted desea extraer todas las oraciones del artículo de Wikipedia que mencionan primero a Chile y luego a alguno de sus países vecinos (Argentina, Bolivia o Perú). Entiéndase por una oración como un string que no posee ni saltos de línea ni puntos. Realizar esto en Python sin la ayuda de una librería puede resultar complicado. Un intento podría ser:

[ ]
count = 1
for line in text.split('\n'):
    for sentence in line.split('.'):
        x = sentence.find("Chile ")
        if x != -1:
            for pais in ["Peru", "Argentina", "Bolivia"]:
                y = sentence.find(pais, x)
                if y != -1:
                    print("{}. {}".format(count, sentence))
                    count += 1
                    break
Donde, por cada línea del documento, se hace uso de el método find de un string en Python para buscar las palabras relevantes.

Esta tarea no requiere mucho esfuerzo de su parte. Ahora, imagine que como experto en datos usted requiere hacer esta tarea multiples veces al dia, con distintos data sets (potencialmente con grandes volumenes de datos) y donde los requerimientos para la extracción es muy distinta. Si bien escribir y probar este código le puede tomar 10 minutos a 30 minutos en promedio, realizar esta tarea reiteradas veces puede ser un costo innecesario para su quehacer como experto en datos. Por último, lo más seguro es que su programa en Python no será muy eficiente y puede que tome varios minutos en terminar para documentos de gran tamaño.

De hecho, la misma tarea anterior se puede hacer con las siguientes lineas de código, usando la librería REmatch.

Double-click (or enter) to edit

[ ]
import pyrematch as re

rgx = re.compile("(^|[\n.])!sentence{[^.\n]*Chile [^.\n]+(Peru|Argentina|Bolivia)[^.\n]*\.}")

for idx, match in enumerate(rgx.finditer(text)):
    print("{}. {sentence}".format(idx+1, **match.groupdict()))
La mayor parte de las lineas del código anterior son para llamar y ejecutar la librería REmatch. De hecho, toda la tarea se encuentra descrita en:

(^|[\n.])!sentence{[^.\n]*Chile [^.\n]+(Peru|Argentina|Bolivia)[^.\n]*\.}

el cuál es un patron que describe la tarea de extracción que debe hacer la librería. El lenguaje de este patrón se conoce como expresiones regulares (también llamados regex ó RE). Las expresiones regulares es un lenguaje de caracteres y operadores especiales que nos permiten describir grupos de secuencias en strings, que a uno le gustaría identificar, verificar, y extraer. Estas expresiones nos facilitarán la tarea de extracción de información de documentos, permitiendonos definir nuestra tarea y dejando que una librería como REmatch se encargue de ejecutar y optimizar la tarea de la mejor forma posible. Las expresiones regulares nos pueden servir para otras tareas como validación de formularios, búsqueda y reemplazo, transformación de texto, y procesamiento de registros.

En esta unidad usted aprenderá el lenguaje de expresiones regulares para verificar patrones sencillos en strings, para después aprovechar estos patrones para extraer información desde documentos con la librería REmatch.

Expresiones regulares
Patrones sencillos
La forma más sencilla de una expresión regular es un palabra. Una palabra como gmail define la secuencia 'gmail' y describe que solo los strings que contengan la palabra 'gmail' cumplirán con la propiedad. Por ejemplo, el siguiente código muestra un arreglo de strings, donde cada uno es un correo. Con la función find de la librería REmatch verificaremos si se encuentra la palabra 'gmail' en cada correo y, de ser así, la imprimiremos como output.

[ ]
# Importamos la librería REmatch
import pyrematch as re
[ ]
# Definimos un conjunto de correos que 
# necesitamos verificar si cumplen con un patrón.
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]

# El patrón que ocuparemos es 'gmail'
pattern = "gmail"

# Compilamos nuestro patrón en un objeto regex
regex = re.compile(pattern)

# Verificacamos si algun string cumple con la expresión regular
for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Como se puede ver en el ejemplo, la función find verifica que el patron gmail aparece en un string y retorna TRUE si aparece, y FALSE en caso contrario.

Muchas veces sabremos el patrón que queremos definir, pero existen ciertas posiciones del patrón que puede ser cualquier carácter. Para esto usaremos el patrón . que significa simplemente que queremos ver una letra. Por ejemplo, si queremos encontrar verificar correos que tienen la palabra 'gm?il' donde la tercera letra puede ser cualquier símbolo, entonces eso lo definimos con la expresión gm.il donde el . representa cualquier símbolo.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "gm.il"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Al ejecutar este código, tendremos los mismos resultados que para el patrón sencillo gmail pero con más resultados. En algunos casos, con el patrón queremos definir que en esa posición no irá cualquier símbolo, si no un símbolo de una clase en especial. En nuestro ejemplo de 'gm?il' nos gustaría decir que el tercer símbolo es una vocal. Para esto, usamos el operador [ ] que permite especificar clases de caracteres, donde dentro de los párentesis cuadrados enlistamos todos los símbolos que pueden aparecer. Por ejemplo, para definir la clase de vocales, usamos [aeiou], y para decir que queremos encontrar 'gm_il' donde el símbolo _ puede ser una vocal, usamos el patrón gm[aeiou]il.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "gm[aeiou]il"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
La lista de correos anterior ahora se redujo, porque solo queremos los que tienen una vocal en la tercer símbolo. Si queremos agregar más símbolos, podemos colocar todos los que queramos dentro de los [ ], como por ejemplo todas las letras minúsculas del abecedario (inglés):

[abcdefghijklmnopqrstuvwxyz]

Obviamente, esto no se ve muy elegante a primera vista. Para simplificar las clases de caracteres, expresiones regulares permiten definir intervalos de caracteres. Si queremos definir todas las letras mínusculas podemos usar [a-z], que significa desde la a hasta la z (en códificación ASCII), o si queremos todas las letras mayusculas y mínusculas, podemos usar [a-zA-Z], que es lo mismo que [a-z] pero agregando el tramo de mayusculas desde la A hasta la Z. Por último, las clases de caracteres [ ] permite definir un clase de símbolos que excluye a todos los símbolos enlistados dentro los parentesis. Para esto, usamos el símbolo ^ al comienzo de la clase de caracteres. Así, si queremos decir cualquier símbolo menos las vocales, escribimos [^abcde].

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "gm[^aeiou]il"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Lo anterior describe todos los patrones sencillos para encontrar una secuencia de símbolos dentro de un string. Pero, ¿cómo podemos definir que queremos encontrar un punto .? Como el punto es parte de la síntaxis del lenguaje, debemos usar el símbolo de escape. Así, si queremos encontrar todos los correos del tipo 'gmail.com', debemos escribir el patrón como gmail\.com. Lo mismo debemos hacer para encontrar símbolos como [ y] que son parte de la sintaxis del lenguaje de expresiones regulares, cómo los símbolos de otros operadores que veremos a continuación.

Disyunción y opcionales
Si bien los patrones sencillos nos permite definir una secuencia de largo fijo que queremos encontrar en un string, no nos permite buscar la aparición de dos o más posibilidades a la vez. Por ejemplo, nos gustaría verificar la aparición de la palabra 'gmail' o la palabra 'uc', si cualquier de las dos aparece en el string. Para esto podemos usar el operador de disyunción | que nos permite decir gmail|uc que se lee como "queremos ver la aparición de gmail o uc en el string".

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "gmail|uc"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Este nuevo operador | lo podemos combinar con patrones sencillos, o también dentro de patrones sencillos. Por ejemplo, en vez de utilizar clase de caracteres para definir una vocal, podemos usar la disyunción y definir el patrón gm(a|e|i|o|u)il, donde los parentesis son parte de la sintaxis de expresiones regulares y nos permite agrupar las disyunciones. En otras palabras, la subexpresión (a|e|i|o|u) es equivalente a [aeiou], que define la clase de las vocales. En particular, podemos usar el operador | para listar distintas posibilidades en un patrón como gmail|uc|puc.

Otra forma de elegir entre alternativas en una expresión regular es usando el operador opcional ?, que es otra alternativa para usar disyunción. Un ejemplo del opcional es cuando utilizamos ing\.(uc|puc) para buscar la palabra 'ing.uc' o 'ing.puc' en un correo. Ambas palabras son muy parecidas y la única diferencia es que la 'p' puede o no aparecer en el correo. Para esto utilizamos el operador opcional ? y escribimos la expresión ing\.p?uc.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "ing\.p?uc"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Por último, es importante notar que podemos usar el opcional ? sobre un patron sencillo, o anidar este operador sobre otros operadores. Por ejemplo, si también queremos que el prefijo 'ing.' puede o no aparecer, entonces esto lo podemos definir como (ing\.)?p?uc donde los paréntesis ( ) nos ayudan para agrupar el subpatrón donde se aplicará el operador opcional.

Repeticiones
El último y uno de los operadores más importantes son las repeticiones. Nuestras expresiones regulares nos permiten identificar hasta ahora patrones dentro de un string, pero una cantidad acotada de posibilidades. Por ejemplo, una expresión como gmail|p?uc nos permite identificar la aparición de 'gmail', 'puc' o 'uc' en el string, pero esta es una cantidad acotada de posibilidades (tres).

Para definir patrones que puede tener 1-o-más o 0-o-más caracteres, utilizamos los operadores de repeticiones + y *. Por ejemplo, si queremos identificar correos que contengan '@ing.uc.cl' o '@mail.uc.cl', donde lo que esta entre '@' y el siguiente punto no nos interesa, entonces usamos la expresión regular @[a-zA-Z]+\.uc\.cl. En esta última expresión, el [a-zA-Z]+ significa que queremos ver una letra (mayuscula o mínuscula, esto es, [a-zA-Z]) una o más veces. En cambio, si queremos permitir correos como '@.uc.cl', entonces podemos usar el operador * y escribir la expresión @[a-zA-Z]*\.uc\.cl donde ahora el [a-zA-Z]* significa que deseamos ver una letra cero o más veces.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "@[a-zA-Z]+\.uc\.cl"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
La expresión regular [a-zA-Z]+ nos permite encontrar uno o más letras en un correo, pero no tiene limite del largo de la palabra. De hecho, la expresión @[a-zA-Z]+\.uc\.cl calzará con el correo '@a.uc.cl' o con el correo '@aaaaaaaaaaaaaaaaaaaaa.uc.cl' (20 letras o más) o con cualquier largo entre @ y el primer punto. Muchas veces no queremos una cantidad arbitraria de repeticiones de un patrón, si no que una cantidad de repeticiones que esta entre un rango. Para esto, uno puede utilizar el operador de repeticiones con rango {n,m} que significa que el patrón se repetira de n a m veces. Volviendo a nuestro ejemplo, si queremos que la palabra del dominio este entre 2 a 5 caracteres, entonces usamos @[a-zA-Z]{2,5}\.uc\.cl.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "@[a-zA-Z]{2,5}\.uc\.cl"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Anclas y abreviaciones
Hasta ahora hemos usado nuestros ejemplos pidiendo que la aparición de cada patrón sea en cualquier parte del string. Si bien esto ocurre en la mayoría de los casos, otras veces nos gustará referirnos al comienzo o fin del string, también conocidos como anclas. Para esto usaremos el operador ^ para referirse al inicio del string y $ para referirse al termino del string. Para ejemplificar el uso de ambos operadores, podemos definir una expresión regular que nos permita verificar que el string completo es un correo electrónico usando la siguiente expresión:

^[a-zA-Z.]+@[a-zA-Z.]+\.[a-zA-Z]{2,3}$

Aquí el ^ al comienzo de la expresión nos dice que la aparición del patrón tiene que ser desde el comienzo del string y, en cambio, el $ al final nos dice que el patrón debe terminar justo al final del string.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]{2,3}$"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Los símbolos ^ y $ nos sirven como caracteres especiales para referirnos al comienzo y el fin. Existen también otros símbolos que nos permiten referirnos a clases de símbolos especiales. Por ejemplo, en vez de usar la clase de caracteres [a-zA-Z] para referirnos a una letra, las expresiones regulares nos permiten utilizar abreviaciones y usar \w para decir cualquier caracter alfa numérico (especificamente, equivalente a [a-zA-Z0-9]. Así, si nuestra expresión anterior para correos permitiendo digitos en el correo se vería de la siguiente forma: ^\w+@\w+\.\w+\.\w{2,3}$.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "^\w+@\w+\.\w+\.\w{2,3}$"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Existen abreviaciones prestablecidas para ciertas clases de caracteres. Las soportadas por la librería REmatch son las siguientes:

\d: equivale a [0-9];
\D: es equivalente a [^0-9], donde se compara con cualquier caracter que no sea dígito;
\s: equivale a hacer [\t\n\r\f\v], compara cualquier tipo de espacio en blanco;
\S: equivale a escribir la clase [^\t\n\r\f\v], que compara con cualquier caracter distinto a los espacios en blanco;
\w: es equivalente a la clase [a-zA-Z0-9\_], donde se compara con cualquier caracter alfa numérico;
\W: equivale a [^a-zA-Z0-9\_], que contempla que no haya ningún caracter alfa numérico.
Para finalizar, definiremos la expresión regular que nos permite detectar correos cómo aparecen en el mundo real; quiere decir, los correos de tipo cristian.perez52@ing.puc.cl, dónde la primera parte pude tener una o dos palabras alfa numericas separadas por un punto ., seguido por el símbolo @, seguido por el dominio que consta de dos o tres partes, la última siendo de largo 2 o 3.

La expresión regular que nos permite definir un correo así ocupa las ideas vista en los ejemplos anteriores, cómo las anclas, las abreviaciones, las repeticiones, y opcionales, y se puede escribir de siguiente manera: ^(\w+\.)?\w+@(\w+\.)?\w+.\w{2,3}$. Aquí la parte opcional (\w+\.)? en el inicio de la expresión nos permite tener el usuario del correo compuesto de dos palabras, o de una, y después del símbolo @ permite tener la definición del dominio más compleja.

El siguiente código permite verificar que la expresión funciona como deseamos.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "^(\w+\.)?\w+@(\w+\.)?\w+.\w{2,3}$"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")
Funciones de libreria REmatch
Ya contamos con todos los operadores más importantes para definir nuestras expresiones regulares. Existen varias otros operadores o extensiones que nos pueden permitir simplificar nuestras expresiones, pero las vistas anteriormente son las principales, y con ellas podemos hacer la mayoría de las tareas.

Ahora veremos como utilizar expresiones regulares para, no solo verificar si se cumple un patrón o no, si no también para extraer las partes del documento que cumplen con este patrón. Para esto, usaremos expresiones regulares y las extenderemos con variables que almacenarán las partes del string o documento que cumplen con el patrón.

Variables y captura
Para entender como usar expresiones regulares y extraer partes de nuestro strings, veamos un ejemplo. Considere nuestra expresión sencilla para verificar un correo, solo que ahora le agregaremos variables para especificar las partes que queremos extraer:

^!x{(\w+\.)?\w+}@!y{(\w+\.)?\w+\.\w{2,3}}$

Nuestra nueva expresion regular cuenta con dos variables. La primera variable, escrita como !x{...} nos permitirá obtener el identificador del correo, mientras que la segunda variable, escrita como !y{...} nos permitirá obtener el dominio del correo. De hecho, el identificador x e y son los nombres de estas variables, y nos permitirá referirnos por un nombre a cada captura. Estos nombres son arbitrarios, y podríamos haber ocupado identificadores más sugerentes como a continuación:

^!id{(\w+\.)?\w+}@!domain{(\w+\.)?\w+\.\w{2,3}}$

donde id y domain son los nuevos identificadores para x e y, respectivamente.

Ahora que tenemos nuestras variables para capturar contenido, necesitaremos ver como utilizar la librería REmatch para extraer el contenido. Para esto, veamos un ejemplo en ejecución.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "^!id{(\w+\.)?\w+}@!domain{(\w+\.)?\w+\.\w{2,3}}$"
regex = re.compile(pattern)

for s in seq:
    match = regex.find(s)
    if match:
        print("El correo " + s + 
              " tiene id " + match.group('id') + 
              " y dominio " + match.group('domain'))
Como se puede observar de este ejemplo, la función find del objeto regex nos devuelve un objeto match cuando obtiene un resultado. Este objeto match tiene la captura con el contenido de id y de domain. Para acceder el string capturado por estas variables, usamos la función group con el nombre de la variable.

Extracción en documentos
Suponga ahora que en vez de un solo string, usted cuenta con un documento que es una lista de string separados por comas, donde algunos de estos strings pueden ser correos y otros no. Por ejemplo, un posible documento con estas caracteristicas sería el siguiente:

Carlos Perez,cperez@gmail.com,Juan Soto,soto@uc.cl,Sebastian del Campo,sdelcampo@gmail.com

Usted desea extraer los strings que son correos, junto con su identificador y dominio. Si extendemos ligeramente nuestra expresión regular podremos identificar si un campo en los datos (esto es, un string separado por comas) es un correo y, utilizando las variables, podremos obtener el identificador el dominio. En otras palabras, considere la siguiente expresión regular:

(^|,)!id{(\w+\.)?\w+}@!domain{(\w+\.)?\w+\.\w{2,3}}($|,)

Lo que hicimos fue modificar el comienzo con (^|,) que nos permite partir desde el comienzo del string o desde una coma, y también modificar el fin con ($|,) que nos permite terminar desde el fin del string o desde una coma. Esta expresión regular busca un correo en el documento y, de encontrarlo, obtiene el identificador y dominio del correo.

Volviendo a nuestro objetivo, nosotros queremos obtener todos los correos en esta lista y no solo saber si hay un correo o no. Para esto, al evaluar nuestra nueva expresión la función finditer de REmatch buscará todos los posibles matches de nuestro patrón en el documento, permitiendo recorrerlos uno a uno. Veamos un ejemplo de como funciona finditer.

[ ]
document = 'Carlos Perez,cperez@gmail.com,Juan Soto,soto@uc.cl,Sebastian del Campo,sdelcampo@gmail.com'
pattern = "(^|,)!id{(\w+\.)?\w+}@!domain{(\w+\.)?\w+\.\w{2,3}}($|,)"
regex = re.compile(pattern)

for match in regex.finditer(document):
    print("El correo " + s + 
          " tiene id " + match.group('id') + 
          " y dominio " + match.group('domain'))
Superposición de resultados
Es importante notar que REmatch buscará todas las ocurrencias de nuestro patrón en el documento, posiblemente con contenidos repetidos en el documento. Para entender esto, tratemos ahora de buscar todos los campos que estan entre comas con la expresión regular:

(^|,)!text{.+}($|,)

Este expresión buscara el comienzo del documento o una coma, seguido de uno o más caracteres, y terminado en el fin del documento o una coma. Por último la secuencia de uno o más caracteres será almacenado en la variable text. Comprobemos ahora como funciona este patrón en REmatch y que será lo que entregará la función finditer.

[ ]
document = 'Carlos Perez,cperez@gmail.com,Juan Soto,soto@uc.cl,Sebastian del Campo,sdelcampo@gmail.com'
pattern = "(^|,)!text{.+}($|,)"
regex = re.compile(pattern)

for match in regex.finditer(document):
    print("El texto encontrado fue " + match.group('text'))
Puede ver que REmatch encontro todos los campos entre comas, pero tambien campos que cruzan entre una o más comas. Recuerde que .+ buscará calzar con "uno o más" caracteres y como la coma es un carácter, también cumple con lo especificado. Si queremos encontrar todos los campos, entonces tenemos que decirle a REmatch que encuentre uno o más caracteres que no sea una coma. Esto ya lo sabemos hacer con la clase [^,], por lo cual, el patrón que necesitamos será el siguiente:

(^|,)!text{[^,]+}($|,)

Si probamos este patrón en el documento anterior, podremos ver que ahora si encotraremos solo los campos entre dos comas consecutivas.

[ ]
document = 'Carlos Perez,cperez@gmail.com,Juan Soto,soto@uc.cl,Sebastian del Campo,sdelcampo@gmail.com'
pattern = "(^|,)!text{[^,]+}($|,)"
regex = re.compile(pattern)

for match in regex.finditer(document):
    print('El campo encontrado fue "{0}"'.format(match.group('text')))
Groups versus spans
Hasta ahora hemos extraido el contenido de cada captura. Muchas veces también nos interesa saber la posición donde aparece ese contenido, más que el contenido mismo. La posición del contenido en el documento viene dado por lo que se conoce como un span, que es un par (i, j) con i menor que j. Este span (i,j) define un intervalo del string, o sea, define el contenido desde el carácter i hasta el carácter j. Si volvemos a nuestro ejemplo anterior de campos de un documento, podemos extraer las posiciones de donde aparce cada campo text, utilizando el método span de un match.

[ ]
document = 'Carlos Perez,cperez@gmail.com,Juan Soto,soto@uc.cl,Sebastian del Campo,sdelcampo@gmail.com'
pattern = "(^|,)!text{[^,]+}($|,)"
regex = re.compile(pattern)
for match in regex.finditer(document):
    print('El campo encontrado fue "{0}" en la posición {1}'.format(match.group('text'), match.span('text')))
Es importante notar que el span de un match nos dice el contexto donde aparece el contenido, y esto nos puede ayudar para saber si este aparece al comienzo del documento, al final, etc. Para manejo de spans y groups, el objeto match cuenta con las siguientes funcionalidades:

start(id-variable): entrega la posición inicial del span de la variable con nombre id-variable.
end(id-variable): entrega la posición final del span de la variable con nombre id-variable.
groups(): entrega todos los contenidos de las variables en orden arbitrario.
groupdict(): entrega un diccionario (id-variable, contenido) de todas las variables.
¿Por qué utilizamos la librería REmatch?
REmatch es una librería para extracción de información desarrollada por investigadores y alumnos del Departamento de Ciencia de la Computación de la Escuela de Ingeniería. Esta librería cuenta con varias ventajas con respesto a otras librerías.

REmatch es una librería orientada a extraer información desde archivos de texto grandes, y no solo a la búsqueda de un patron adentro del texto. En este contexto, REmatch permite extraer todos los matches, y no solo encontrar el primer match. Con todos los matches nos referimos que REmatch también puede detectar matches solapados, que es algo fuera del alcance de otras librerías, y muy útil en varios contextos, cómo, por ejemplo, en el análisis de secuencias de ADN, procesamiento de logs, texto natural, etc.

Adicionalmente, REmatch es orientado a procesar documentos grandes de manera muy rápida, y extraer información de manera muy eficiente. Por lo tanto, REmatch evita las debilidades de varias otras librerías de expresiones regulares, y no permite ataques de estilo ReDos (ver https://en.wikipedia.org/wiki/ReDoS), a los cuales padecen muchas librerías clasicas de expresiones regulares.

Para aprender más sobre la librería REmatch, te invitamos visitar nuestra página web https://rematch.cl, o bajar, compilar, y ocupar el código de la librería desde nuestro github https://github.com/REmatchChile/REmatch/, dónde puedes encontrar la versión de la librería en C++, Python, y javaScript.

