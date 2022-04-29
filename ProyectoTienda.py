import random
lista_compradores = []
lista_vendedores = []
lista_transportadores = []
lista_productos = []
lista_pedidos = []
lista_envios = []

class Comprador:
    def __init__(self,cedula_comprador, nombre_comprador,carrito_compras):
        self.cedula_comprador = cedula_comprador
        self.nombre_comprador = nombre_comprador
        self.carrito_compras = carrito_compras

    def MostrarDatos(self):
        print("Cedula: {} - Nombre: {}".format(self.cedula_comprador,self.nombre_comprador))

def crear_comprador():
    print("CREAR COMPRADOR")
    cedula_comprador = (int(input("Ingrese su cédula: ")))
    nombre_comprador = ((input("Ingrese su nombre: ")))
    carrito_compras = []
    obj_comprador = Comprador(cedula_comprador, nombre_comprador,carrito_compras)
    lista_compradores.append(obj_comprador)

def editar_comprador():
    cedula = (int(input("Ingrese la cedula para editar el comprador")))
    while True:
        print("\n")
        print("Seleccione una de las siguientes opciones:")
        print("1.- EDITAR CEDULA")
        print("2.- EDITAR NOMBRE")
        print("0.- SALIR\n")

        opcion = int(input("Opción: "))

        if opcion == 1:
            ced_editar = (int(input("Ingrese su cedula nueva")))
            for comprador in lista_compradores:
                if comprador.cedula_comprador == cedula:
                    comprador.cedula_comprador = ced_editar
                    print(f"Su cedula ha sido editada correctamente y ahora es {comprador.cedula_comprador}")
        elif opcion == 2:
            nombre_editar = input("Ingrese el nuevo nombre")
            for comprador in lista_compradores:
                if comprador.cedula_comprador == cedula:
                    comprador.nombre_comprador = nombre_editar
                    print(f"Su nombre ha sido editada correctamente y ahora es {comprador.nombre_comprador}")
        elif opcion == 0:
            break

def eliminar_comprador():
    cedula = (int(input("Ingrese la cedula del comprador que desea eliminar")))
    for comprador in lista_compradores:
        if comprador.cedula_comprador == cedula:
            lista_compradores.remove(comprador)

def mostar_compradores():
    print("Lista compradores registrados")
    for compradores in lista_compradores:
        compradores.MostrarDatos()

def car_cost(cedula):
    car_cost = 0
    for comprador in lista_compradores:
        if comprador.cedula_comprador == cedula:
            if len(comprador.carrito_compras) > 0:
                for producto in comprador.carrito_compras:
                    car_cost = car_cost + producto.precio
                    print("Codigo: {} - Producto: {} - Precio: {}".format(producto.codigo, producto.nombre,
                                                                          producto.precio))
        print(f"El coste del carrito es {car_cost}")

def gestionar_carrito():
    print("CATÁLOGO DE PRODUCTOS")
    cedula = int(input("INGRESE SU CEDULA PARA ACCEDER A SU CARRITO"))
    for vendedor in lista_vendedores:
        for producto in vendedor.catalogo_productos:
            print(f"VENDEDOR: {vendedor.nombre_vendedor}")
            print("Codigo: {} - Producto: {} - Existencias {}".format(producto.codigo,producto.nombre, producto.existencias))
    while True:
        print("\n")
        print("Seleccione una de las siguientes opciones:")
        print("1.- AGREGAR PRODUCTO AL CARRITO")
        print("2.- ELIMINAR PRODUCTO DEL CARRITO")
        print("3.- CALCULAR PRECIO DEL CARRITO")
        print("0.- SALIR\n")

        opcion = int(input("Opción: "))

        if opcion == 1:
            producto_comprar = (int(input("Ingrese el codigo del producto que desea comprar")))
            for vendedor in lista_vendedores:
                for producto in vendedor.catalogo_productos:
                    if producto.codigo == producto_comprar:
                        cantidad_comprar = int(input("Ingrese la cantidad que desea comprar"))
                        if producto.existencias >= cantidad_comprar:
                            producto.existencias = producto.existencias - cantidad_comprar
                            for comprador in lista_compradores:
                                if comprador.cedula_comprador == cedula:
                                    for _ in range(cantidad_comprar):
                                        comprador.carrito_compras.append(producto)
                                    print(f"Se han agregado {cantidad_comprar} productos al carrito")
                                else:
                                    print("Registrese antes para tener acceso a un carrito de compras")
                        else:
                            print("Producto sin existencias")
                    else:
                        print("El producto no existe")
        if opcion == 2:
            for comprador in lista_compradores:
                if comprador.cedula_comprador == cedula:
                    if len(comprador.carrito_compras) != 0:
                        producto_eliminar = int(input("Ingrese el codigo del producto que desea eliminar "))
                        for producto in comprador.carrito_compras:
                            if producto.codigo == producto_eliminar:
                                comprador.carrito_compras.remove(producto)
                                print("Producto eliminado con exito")
                    else:
                        print("Carrito vacío")
                        break
        if opcion == 3:
            car_cost(cedula)
        if opcion == 0:
            break

def generar_pedido():
    cedula_comprador = int(input("Ingrese su cedula para generar un pedido"))
    for comprador in lista_compradores:
        if comprador.cedula_comprador == cedula_comprador:
            if len(comprador.carrito_compras) == 0:
                print("El carrito está vacío")
            else:
                car_cost(cedula_comprador)
        while True:
            print("DESEA CONFIRMAR LA COMPRA?")
            print("Presione la opción 1 para confirmar")
            print("Presione la opción 2 para rechazar")

            opcion = int(input("Opción: "))

            if opcion == 1:
                crear_pedido(cedula_comprador)
                if crear_pedido(cedula_comprador):
                    print("Su pedido se ha generado con exito")
            if opcion == 2:
                break

class Vendedor:
    def __init__(self,cedula_vendedor, nombre_vendedor,catalogo_productos):
        self.cedula_vendedor = cedula_vendedor
        self.nombre_vendedor = nombre_vendedor
        self.catalogo_productos = catalogo_productos

    def MostrarDatos(self):
        print("Cedula: {} - Nombre: {} ".format(self.cedula_vendedor,self.nombre_vendedor))

def crear_vendedor():
    print("CREAR VENDEDOR")
    cedula_vendedor = (int(input("Ingrese su cédula: ")))
    nombre_vendedor = input("Ingrese su nombre: ")
    catalogo_productos = []
    obj_vendedor = Vendedor(cedula_vendedor, nombre_vendedor,catalogo_productos)
    lista_vendedores.append(obj_vendedor)

def editar_vendedor():
    cedula = (int(input("Ingrese la cedula para editar el vendedor")))
    while True:
        print("\n")
        print("Seleccione una de las siguientes opciones:")
        print("1.- EDITAR CEDULA")
        print("2.- EDITAR NOMBRE")
        print("0.- SALIR\n")

        opcion = int(input("Opción: "))

        if opcion == 1:
            ced_editar = (int(input("Ingrese su cedula nueva")))
            for vendedor in lista_vendedores:
                if vendedor.lista_vendedores == cedula:
                    vendedor.cedula_vendedor = ced_editar
                    print(f"Su cedula ha sido editada correctamente y ahora es {vendedor.cedula_vendedor}")
        elif opcion == 2:
            nombre_editar = input("Ingrese el nuevo nombre")
            for vendedor in lista_vendedores:
                if vendedor.cedula_vendedor == cedula:
                    vendedor.nombre_vendedor = nombre_editar
                    print(f"Su nombre ha sido editada correctamente y ahora es {vendedor.nombre_vendedor}")
        elif opcion == 0:
            break

def eliminar_vendedor():
    cedula = (int(input("Ingrese la cedula del comprador que desea eliminar")))
    for vendedor in lista_vendedores:
        if vendedor.cedula_vendedor == cedula:
            lista_vendedores.remove(vendedor)

def mostrar_vendedores():
    print("Lista vendedores registrados")
    for vendedor in lista_vendedores:
        vendedor.MostrarDatos()

def mostrar_catalogo():
    print("CATÁLOGO DE PRODUCTOS")
    for vendedor in lista_vendedores:
        for producto in vendedor.catalogo_productos:
            print(f"VENDEDOR: {vendedor.nombre_vendedor}")
            print("Codigo: {} - Producto: {} - Existencias {}".format(producto.codigo,producto.nombre, producto.existencias))

def buscar_producto_categoria():
    caracteristica_buscar = input("Ingrese la categoría a buscar")
    for vendedor in lista_vendedores:
        for producto in vendedor.catalogo_productos:
            if producto.caracteristicas == caracteristica_buscar:
                print("El producto se encuentra disponible")
                print("Los productos son distribuidos por: El vendedor {}".format(vendedor.nombre_vendedor))
                print("Productos disponibles con esta caracteristica: {} - Existencias {}".format(producto.nombre,producto.existencias))

class Transportador:
    def __init__(self,cod_transportador, cedula_transportador, nombre_transportador):
        self.codigo_transportador = cod_transportador
        self.cedula_transportador = cedula_transportador
        self.nombre_transportador = nombre_transportador

    def MostrarDatos(self):
        print("Codigo del transportador: {} - Cedula: {} - Nombre: {}".format(self.codigo_transportador,
        self.cedula_transportador, self.nombre_transportador))

def crear_transportador():
    print("CREAR TRANSPORTADOR")
    cedula_transportador = (int(input("Ingrese su cédula: ")))
    nombre_transportador = (input("Ingrese su nombre: "))
    cod_transportador = (random.randrange(10000,99999))
    obj_transportador = Transportador(cod_transportador, cedula_transportador, nombre_transportador)
    lista_transportadores.append(obj_transportador)

def editar_transportador():
    cedula = (int(input("Ingrese la cedula para editar el transportador")))
    while True:
        print("\n")
        print("Seleccione una de las siguientes opciones:")
        print("1.- EDITAR CODIGO")
        print("2.- EDITAR CEDULA")
        print("3.- EDITAR NOMBRE")
        print("0.- SALIR\n")

        opcion = int(input("Opción: "))

        if opcion == 1:
            cod_editar = int(input("Ingrese su nuevo código (5 dígitos)"))
            for transportador in lista_transportadores:
                if transportador.lista_transportadores == cedula:
                    transportador.codigo_transportador = cod_editar
                    print(f"Su código ha sido editada correctamente y ahora es {transportador.codigo_transportador}")

        elif opcion == 2:
            ced_editar = (int(input("Ingrese su cedula nueva")))
            for transportador in lista_transportadores:
                if transportador.lista_transportadores == cedula:
                    transportador.cedula_transportador = ced_editar
                    print(f"Su cedula ha sido editada correctamente y ahora es {transportador.cedula_transportador}")

        elif opcion == 3:
            nombre_editar = input("Ingrese el nuevo nombre")
            for transportador in lista_transportadores:
                if transportador.cedula_transportador == cedula:
                    transportador.nombre_transportador = nombre_editar
                    print(f"Su nombre ha sido editada correctamente y ahora es {transportador.nombre_transportador}")

        elif opcion == 0:
            break

def eliminar_transportador():
    cedula = (int(input("Ingrese la cedula del transportador que desea eliminar")))
    for transportador in lista_transportadores:
        if transportador.cedula_vendedor == cedula:
            lista_transportadores.remove(transportador)

def mostrar_transportadores():
    print("Lista transportadores registrados")
    for transportador in lista_transportadores:
        transportador.MostrarDatos()

class Producto:
    def __init__(self,codigo, nombre, caracteristicas, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.caracteristicas = caracteristicas
        self.precio = precio
        self.existencias = existencias

def crear_productos():
    print("CREAR PRODUCTO")
    cedula_vendedor = int(input("Ingrese la cedula del vendedor al que desea gestionarle el catalogo"))
    while True:
        print("\n")
        print("Seleccione una de las siguientes opciones:")
        print("1.- INGRESAR PRODUCTO")
        print("2.- ELIMINAR PRODUCTO")
        print("0.- SALIR\n")

        opcion = int(input("Opción: "))

        if opcion == 1:
            codigo_producto = (int(input("INGRESE EL CODIGO DEL PRODUCTO: ")))
            nombre_producto = input("INGRESE EL NOMBRE DEL PRODUCTO")
            caracteristicas_producto = (input("INGRESE LAS CARACTERISTICAS DEL PRODUCTO: "))
            precio = (int(input("INGRESE EL PRECIO DEL PRODUCTO")))
            existencias = (int(input("INGRESE LAS EXISTENCIAS DEL PRODUCTO")))
            obj_producto = Producto(codigo_producto, nombre_producto, caracteristicas_producto, precio,
                                    existencias)
            for vendedor in lista_vendedores:
                if vendedor.cedula_vendedor == cedula_vendedor:
                    vendedor.catalogo_productos.append(obj_producto)
                    print("Producto registrado con exito")
        elif opcion == 2:
            for vendedor in lista_vendedores:
                if len(vendedor.catalogo_productos) == 0:
                    print("El vendedor no tiene productos en su catalogo")
                else:
                    for _ in vendedor.catalogo_productos:
                        vendedor.catalogo_productos.pop()
                        print("Producto eliminado con exito")
        elif opcion == 0:
            break

class Pedido:
    def __init__(self,codigo,comprador,transportador):
        self.codigo = codigo
        self.comprador = comprador
        self.transportador = transportador
    def MostrarDatos(self):
        print("Codigo del pedido: {} - Comprador: {} - Transportador: {}".format(self.codigo,
        self.comprador, self.transportador))

def guardar_comprador(cedula):
    for comprador in lista_compradores:
        if comprador.cedula_comprador == cedula:
            comprador_pedido = comprador.nombre_comprador
            return comprador_pedido

def crear_pedido(cedula):
    codigo = (random.randrange(10000,99999))
    comprador = guardar_comprador(cedula)
    a = random.choice(lista_transportadores)
    c = a.nombre_transportador
    obj_pedido = Pedido(codigo, comprador, c)
    lista_pedidos.append(obj_pedido)

def consultar_pedidos():
    for pedido in lista_pedidos:
        pedido.MostrarDatos()

def realizar_envio():
    pedido_enviado = lista_pedidos.pop()
    codigo_pedido = pedido_enviado.codigo
    print(f"El pedido {codigo_pedido} ha sido enviado")
    lista_envios.append(pedido_enviado)

def Quit():
    print("Fue un gusto, vuelva pronto!...")
    exit()

def main():
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:")
        print("1.- GESTIONAR COMPRADORES")
        print("2.- GESTIONAR VENDEDORES")
        print("3.- GESTIONAR TRANSPORTADORES")
        print("4.- MOSTRAR LISTADO DE USUARIOS REGISTRADOS")
        print("5.- CREAR PRODUCTOS")
        print("6.- MOSTRAR CATALOGO DE PRODUCTOS")
        print("7.- BUSCAR PRODUCTO POR SU CATEGORÍA")
        print("8.- GESTIONAR CARRITO DE COMPRAS")
        print("9.- GENERAR PEDIDO")
        print("10.- CONSULTAR PEDIDOS")
        print("11.- REALIZAR UN ENVIO")
        print("0.- SALIR\n")

        opcion = int(input("Opción: "))
        #GESTION COMPRADORES
        if opcion == 1:
            while True:
                print("1.- REGISTRAR COMPRADOR")
                print("2.- EDITAR COMPRADOR")
                print("3.- ELIMINAR COMPRADOR")
                print("0.- VOLVER AL MENU PRINCIPAL")

                opcion = int(input("Opción: "))
                if opcion == 1:
                    crear_comprador()
                if opcion == 2:
                    editar_comprador()
                if opcion == 3:
                    eliminar_comprador()
                if opcion == 0:
                    break
        #GESTION VENDEDORES
        elif opcion == 2:
            while True:
                print("1.- REGISTRAR VENDEDOR")
                print("2.- EDITAR VENDEDOR")
                print("3.- ELIMINAR VENDEDOR")
                print("0.- VOLVER AL MENU PRINCIPAL")

                opcion = int(input("Opción: "))
                if opcion == 1:
                    crear_vendedor()
                if opcion == 2:
                    editar_vendedor()
                if opcion == 3:
                    eliminar_vendedor()
                if opcion == 0:
                    break
        #GESTION TRANSPORTADORES
        elif opcion == 3:
            while True:
                print("1.- REGISTRAR TRANSPORTADOR")
                print("2.- EDITAR TRANSPORTADOR")
                print("3.- ELIMINAR TRANSPORTADOR")
                print("0.- VOLVER AL MENU PRINCIPAL")

                opcion = int(input("Opción: "))
                if opcion == 1:
                    crear_transportador()
                if opcion == 2:
                    editar_transportador()
                if opcion == 3:
                    eliminar_transportador()
                if opcion == 0:
                    break
        #MOSTRAR LISTADO DE USUARIOS REGISTRADOS
        elif opcion == 4:
            while True:
                print("1.- MOSTRAR LISTADO COMPRADORES")
                print("2.- MOSTRAR LISTADO VENDEDORES")
                print("3.- MOSTRAR LISTADO TRANSPORTADORES")
                print("0.- VOLVER AL MENU PRINCIPAL")

                opcion = int(input("Opción: "))
                if opcion == 1:
                    mostar_compradores()
                if opcion == 2:
                    mostrar_vendedores()
                if opcion == 3:
                    mostrar_transportadores()
                if opcion == 0:
                    break
        #CREAR PRODUCTOS
        elif opcion == 5:
            crear_productos()
        #MOSTRAR CATALOGO DE PRODUCTOS
        elif opcion == 6:
            mostrar_catalogo()
        #BUSCAR PRODUCTO EN CATALOGO
        elif opcion == 7:
            buscar_producto_categoria()
        #GESTIONAR CARRITO
        elif opcion == 8:
            gestionar_carrito()
        #GENERAR PEDIDO
        elif opcion == 9:
            generar_pedido()
        #CONSULTAR PEDIDOS
        elif opcion == 10:
            consultar_pedidos()
        #REALIZAR ENVIO
        elif opcion == 11:
            realizar_envio()
        #SALIR
        elif opcion == 12:
            Quit()


if __name__ == '__main__':
    main()