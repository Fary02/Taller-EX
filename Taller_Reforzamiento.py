# Se inician las Variables de Array y de objetos;

Productos = []; 

# Creacion de functions;

def menu ():
  
  # Menu;
  
  print("\n*****MENU PRINCIPAL*****"); 
  print("1. Agregar producto"); 
  print("2. Buscar producto"); 
  print("3. Eliminar producto"); 
  print("4. Actualizar disponibilidad"); 
  print("5. Mostrar productos"); 
  print("6. Salir"); 
  
def opcion_Elegida ():
  
  # Solicitud de opcion;
  
  opcion = int(input("\nPor favor, digita una opcion: ")); 

  print(f"\n¡Usted a seleccionado la opcion: {opcion}!"); 
    
  return opcion; 

# Function validacion nombre;  

def validacion_Nombre():

  # Solicitud de datos;
  
  nombre_Validacion = str(input("\n¡Por favor, digite el nombre del producto: ")); 

  # Filtros len y strip;
  
  nombreFiltro = len(nombre_Validacion); 

  nombreFiltroStrip = nombre_Validacion.strip(); 

  # Si se cumple la condicion imprime el mensaje de aviso;
  
  if nombreFiltro >= 1 and isinstance(nombre_Validacion, str) and nombre_Validacion.isdigit() == False and nombreFiltroStrip:
    
    print(f"\n¡Nombre de producto: {nombre_Validacion}!"); 

    # Retorna el nombre filtrado;
    
    return nombre_Validacion; 

  # De lo contrario;

  else:

    print("\n¡ERROR!, el nombre no es valido."); 
    
    return None; 

# Function validacion de datos;

def validacion_Stock():

  # Intenta;

  try:

    # Solicitud de datos;

    stock_Validacion = int(input("\n¡Por favor, digite el stock: ")); 
 
    # Si se cumple la condicion imprime el mensaje con el stock;

    if stock_Validacion >= 0:

      print(f"\n¡Stock disponible: {stock_Validacion}!"); 

      # Retorna el stock filtrado;
      
      return stock_Validacion; 
  
    # De lo contrario; 

    else:

      print("\n¡ERROR!, el stock no es valido."); 
      
      return None; 

    # Manejo de errores dentro de la validacion de stock;

  except ValueError:

    print("\n¡ERROR!, ingrese una cifra valida."); 
    
    return None; 

# Function validacion de precio;

def validacion_Precio():

  # Intenta;

  try:

    precio_Validacion = float(input("\n¡Por favor, digite el precio: ")); 

    # Si se cumple la condicion imprime el mensaje con el precio;

    if precio_Validacion > 0:

      print(f"\n¡Precio: {precio_Validacion}!"); 

      # Retorna el precio filtrado;
      
      return precio_Validacion; 

    # De lo contrario; 

    else:

      print("\n¡ERROR!, el precio no es valido."); 
      
      return None; 

      # Manejo de errores dentro de la validacion de precio;

  except ValueError:

    print("\n¡ERROR!, ingrese un precio valido."); 
    
    return None; 

# Function de disponibilidad por defecto;

def validacion_Disponibilidad ():

  disponibilidad_Inicial = bool(False); 

  print(f"\n¡Disponible: {disponibilidad_Inicial}!"); 
  
  return disponibilidad_Inicial; 

# Function agregar producto; 

def agregar_Producto ():

  # Contiene los datos usados en la opcion;

  nombre_Resultado = validacion_Nombre(); 
  
  stock_Resultado = validacion_Stock(); 
  
  precio_Resultado = validacion_Precio(); 
  
  disponible_Resultado = validacion_Disponibilidad(); 
  
  # Valida que todos los datos sean correctos antes de guardar;
  
  if nombre_Resultado is None or stock_Resultado is None or precio_Resultado is None:
    
    print("\nNo se pudo agregar el producto. Revise los datos ingresados."); 
    
    return; 

  producto = {

  "Nombre": nombre_Resultado,

  "Stock": stock_Resultado,

  "Precio": precio_Resultado,

  "Disponible": disponible_Resultado

  }

  Productos.append(producto); 

  # Mensaje resumen de el producto agregado;
    
  print(f"\n¡Producto agregado correctamente! Datos guardados: Nombre: {nombre_Resultado}, Stock: {stock_Resultado}, Precio: {precio_Resultado}, Disponible: {disponible_Resultado}"); 

# Se crea function que muestre los productos;

def mostrar_Productos ():

  # Si no hay productos imprime el mensaje informativo;

  if len(Productos) == 0:
    
    print("\nNo hay productos registrados."); 
  
  # De lo contrario;
  
  else:

    # Muestra el array con los detalles del producto en formato objeto;

    print("\nProductos registrados:"); 

    for producto in Productos:
      
      print(producto); 

# Function salir;
  
def salir():

  # Retorna mensaje de despedida;

  return print("\nGracias por usar el sistema. ¡Vuelva Pronto!"); 
  
# Inicio de Bucle; 

while True:
  
  menu(); 
  
  # Intenta;
  
  try:

    opcion = opcion_Elegida()

    # Si opcion 1;
    
    if opcion == 1:

      # Devuelve lo siguiente;

      agregar_Producto(); 
    
    # Si la opcion 1 no se cumple;

    elif opcion == 5:

      # Devuelve lo siguiente;

      mostrar_Productos(); 
  
    elif opcion == 6:

      # Devuelve lo siguiente;

      salir()

      # Cierre de ciclo; 

      break; 
    
    # Para avisar al usuario que las siguientes opciones estaran proximamente;
    
    elif opcion == 2 or 3 or 4:

      print("\n¡Se añadiran mas opciones PROXIMAMENTE!"); 


    # De lo contrario;

    else:

      print("\n¡ERROR!, digite una opcion valida."); 
  
    # Manejo de errores;
    
  except ValueError:
    
    print("\n¡ERROR!, ingrese una opcion valida."); 