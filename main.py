# Estefanía Ruiz Cuartas
# Lenguaje de programación: Python
# Tema: Programación orientada a objetos. Atributos de clase e instancias. Métodos de clase
# Fuentes de consulta: https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/#poo-atributos-clase-instancia           https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings https://towardsdatascience.com/understand-o-o-p-in-python-with-one-article-bfa76f3ba48chttps://pythondiario.com/2018/07/metodos-de-clase-estaticos-y.html

# Atributos de clase e instancia: 
# Los atributos de clase son atributos compartidos por todas las instancias de esa clase. Los atributos de instancia, son únicos para cada uno de los objetos pertenecientes a dicha clase.
print("Atributos de clase e instancia\n")

# Ejercicio 1: Class Patinaje_artistico
print("\n- Ejercicio 1: Class Patinaje_artistico\n")

# Creación de la clase Patinaje_artistico, donde incluiremos algunos elementos fundamentales para un deportista que lo practique. Para esto usamos la palabra clave 'class' y la acompañamos con el nombre elegido 'Patinaje_artistico'.
class Patinaje_artistico():
  """
    Clase usada para representar elementos básicos de un deportista de patinaje artistico

    ...

    Atributos
    ------------------
    patines : int (atributo de clase)
        indica la cantidad de patines que necesita un patinador artistico (por defecto 2)
    ruedas_por_patin : int (atributo de clase)
        indica la cantidad de ruedas por patin que necesita un patinador artistico (por defecto 4)
    trusa : int (atributo de clase)
        indica la cantidad de trusas que necesita un patinador artistico para una rutina (por defecto 1)
    coreografia : int (atributo de clase)
        indica la cantidad de coreografias que realiza un patinador artistico (por defecto 1)
    deportista : str (atributos de instancia)
        indica el nombre del deportista
    color : str (atributo de instancia)
        indica el color de la trusa del deportista
    musica : str (atributo de instancia)
        indica la música que utiliza el deportista en su coreografía

    Métodos
    ------------------
    __init__(self,deportista,color,musica)
        inicializa los artibutos del objeto
  """
  patines = 2
  ruedas_por_patin = 4
  trusa = 1
  coreografia = 1

  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: deportista,color,musica 
  def __init__(self,deportista,color,musica):
    '''Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
    ...
    
    Parametros
    -------------------
    deportista : str 
        indica el nombre del deportista
    color : str 
        indica el color de la trusa del deportista
    musica : str 
        indica la música que utiliza el deportista en su coreografía
    '''
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.deportista = deportista
    self.color = color
    self.musica = musica

# Instancia 1, crearemos el objeto a mostrar
# Objeto 1: La deportista Valeria utiliza una trusa color turquesa e innterpreta una canción clásica
deportista1 = Patinaje_artistico("Valeria","turquesa","clasica")

# Mostrar los atributos del objeto 1. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver. En este están incluidos, tanto atributos de clase como atributos de instancia 
print("\nCantidad de ruedas por cada patin:",deportista1.ruedas_por_patin)
print("\nColor de la trusa de la deportista:",deportista1.color)
print("\nNombre del deportista:",deportista1.deportista)
print("\nCoreografías que presenta:",deportista1.coreografia)

# Ejercicio 2: Class Patinaje_artistico
print("\n","\n- Ejercicio 2: Class Patinaje_artistico\n")

# Instancia 2, crearemos el objeto a mostrar
# Objeto 2: La deportista Daniela interpretará en su coreografia una canción de jazz y vestirá una trusa color beige
deportista2 = Patinaje_artistico("Daniela","beige","jazz")

# Mostrar los atributos del objeto 2. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver. En este están incluidos, tanto atributos de clase como atributos de instancia 
print("\nCantidad de trusas de la deportista:",deportista2.trusa)
print("\nMúsica que utiliza la deportista:",deportista2.musica)
print("\nCantidad de patines:",deportista2.patines)
print("\nNombre del deportista:",deportista2.deportista,"\n")

print("\n","---------"*7,"\n")

# Los métodos de clase son aquellos que están ligados directamente con los atributos definidos en la clase que los contiene. Para definirlo, se utiliza el decorador @classmethod y por convención se utiliza cls como argumento inicial en lugar de self
print("\nMétodo de clase\n")

# Ejercicio 1: Class Rectangulo
print("\n- Ejercicio 1: Class Rectangulo\n")

# Creación de la clase Rectangulo, obtener el perimetro de un rectangulo. Para esto usamos la palabra clave 'class' y la acompañamos con el nombre elegido 'Rectangulo'.

class Rectangulo():
   '''
    Clase usada para representar el perimetro de un rectangulo. Tiene incluidas tres funciones,la constructura, la que calcula el perimetro y la del método de clase (permite crear un cuadrado con el parametro 'lado')

    ...

    Atributos
    ------------------
    base : int 
        indica el valor de la base del rectángulo
    altura : int 
        indica el valor de la altura del rectángulo
  
    Métodos
    ------------------
    __init__(self,base,altura)
        inicializa los artibutos del objeto

    perimetro(self)
        retorna el perimetro: resultado de multiplicar la base por 2 y sumarle la altura multplicada por 2

    @classmethod
    cuadrado(cls, lado)
         con este método de clase buscamos crear un cuadrado con el parametro lado
  '''
   def __init__(self,base,altura):
    '''Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
    ...
    
    Parametros
    -------------------
    base : int 
        indica el valor de la base del rectángulo
    altura : int 
        indica el valor de la altura del rectángulo
    ''' 
    self.base = base
    self.altura = altura
        
   def perimetro(self):
     '''
        retorna el perimetro: resultado de multiplicar la base por 2 y sumarle la altura multplicada por 2
         ...
    
    Parametros
    -------------------
    base : int 
        indica el valor de la base del rectángulo
    altura : int 
        indica el valor de la altura del rectángulo
     '''   
     return (self.base*2 + self.altura*2)
  
    
   @classmethod
   def cuadrado(cls, lado):
     '''
       con este método de clase buscamos crear un cuadrado con el parametro lado
      ...
    
    Parametros
    -------------------
    lado : int 
        indica el valor de un lado del cuadrado
     '''
     return cls(lado,lado)


# Instancia 1, crearemos el objeto a mostrar
# Objeto 1: creación de un rectángulo de base 5 y altura 3 y le hallaremos su perimetro con el método de la función de perimetro
rectangulo = Rectangulo(5,3)

# Mostrar el perimetro del rectángulo, objeto creado en el paso anterior
print("Perimetro de un rectángulo de base 5 y altura 3:",rectangulo.perimetro(),"\n")

# Ejercicio 2: Class Rectangulo
print("\n- Ejercicio 2: Class Rectangulo\n")

# Instancia 2, crearemos el objeto a mostrar
# Objeto 2: creación de un cuadrado de lado 7, y le hallaremos su perimetro con el método de la función de perimetro
cuadrado = Rectangulo.cuadrado(7)

# Mostrar el perimetro del cuadrado, objeto creado en el paso anterior
print("Perimetro de un cuadrado de lado 7:",cuadrado.perimetro(),"\n")
