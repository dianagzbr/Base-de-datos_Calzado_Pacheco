from tkinter import *
from tkinter import ttk, messagebox
import ttkbootstrap as tb
import psycopg2 as ps

class Ventana(tb.Window):
    def __init__(self):
        super().__init__()
        self.ventana_login()

    def ventana_login(self):

        self.frame_login=Frame(self)
        self.frame_login.pack()

        self.lblframe_login=LabelFrame(self.frame_login, text='Acceso')
        self.lblframe_login.pack(padx=10, pady=10)

        lbltitulo=Label(self.lblframe_login, text='Inicio de sesión', font=('Arial', 18))
        lbltitulo.pack(padx=10, pady=35)

        self.txt_usuario=ttk.Entry(self.lblframe_login, width=40, justify=CENTER)
        self.txt_usuario.pack(padx=10, pady=10) 
        self.txt_clave=ttk.Entry(self.lblframe_login, width=40, justify=CENTER)
        self.txt_clave.pack(padx=10, pady=10)
        self.txt_clave.configure(show='*')
        btn_acceso=ttk.Button(self.lblframe_login, text='Log in', width=38, command=self.logueo)
        btn_acceso.pack(padx=10, pady=10)
    def ventana_menu(self):
        self.frame_left=Frame(self, width=200)
        self.frame_left.grid(row=0, column=0, sticky=NSEW)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)
        self.frame_right=Frame(self, width=400)
        self.frame_right.grid(row=0, column=2, sticky=NSEW)

        btn_productos=ttk.Button(self.frame_left, text='Usuarios', width=15, command=self.ventana_lista_usuarios)
        btn_productos.grid(row=0, column=0, padx=10, pady=10)
        btn_productos=ttk.Button(self.frame_left, text='Productos', width=15, command=self.ventana_lista_productos)
        btn_productos.grid(row=1, column=0, padx=10, pady=10)
        btn_clientes=ttk.Button(self.frame_left, text='Clientes', width=15)
        btn_clientes.grid(row=2, column=0, padx=10, pady=10)
        btn_ventas=ttk.Button(self.frame_left, text='Ventas', width=15)
        btn_ventas.grid(row=3, column=0, padx=10, pady=10)
        btn_apartado=ttk.Button(self.frame_left, text='Apartados', width=15)
        btn_apartado.grid(row=4, column=0, padx=10, pady=10)
        btn_detalleVenta=ttk.Button(self.frame_left, text='Detalle venta', width=15)
        btn_detalleVenta.grid(row=5, column=0, padx=10, pady=10)
        btn_proveedor=ttk.Button(self.frame_left, text='Proveedores', width=15)
        btn_proveedor.grid(row=6, column=0, padx=10, pady=10)
        btn_facturaCompra=ttk.Button(self.frame_left, text='Factura Compras', width=15)
        btn_facturaCompra.grid(row=7, column=0, padx=10, pady=10)
        btn_detalleCompra=ttk.Button(self.frame_left, text='Detalle Compras', width=15)
        btn_detalleCompra.grid(row=8, column=0, padx=10, pady=10)
        btn_backup=ttk.Button(self.frame_left, text='Backup', width=15)
        btn_backup.grid(row=9, column=0, padx=10, pady=10)
        btn_restaurarDB=ttk.Button(self.frame_left, text='Restaurar DB', width=15)
        btn_restaurarDB.grid(row=10, column=0, padx=10, pady=10)
        

        lbl1=Label(self.frame_center, text='Aqui pondremos las ventanas')
        lbl1.grid(row=0, column=0, padx=10, pady=10)

        lbl1=Label(self.frame_right, text='Aqui pondremos las busquedas')
        lbl1.grid(row=0, column=0, padx=10, pady=10)
    def logueo(self):
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()
            
            nombre_usuario = self.txt_usuario.get()
            clave_usuario = self.txt_clave.get()

            #Ejecutar la consulta para obtener las credenciales
            cur.execute("SELECT * FROM usuarios WHERE nombre=%s AND clave=%s", (nombre_usuario, clave_usuario))
            # Obtener los resultados
            datos_logueo = cur.fetchall()
            if datos_logueo:
                nom_usu, cod_usu, cla_usu, rol_usu = datos_logueo[0] 
                if (nom_usu == nombre_usuario and cla_usu == clave_usuario):
                    self.frame_login.pack_forget()
                    self.ventana_menu()
            else:
                messagebox.showerror("Acceso", "El usuario o la clave son incorrectos")
        
            #Cerrar el cursor y la conexión
            conn.commit()
            conn.close()

        except Exception as e:#Captura excepciones específicas para depuración
            print("Error:", e)
            messagebox.showerror("Acceso","Ocurrió un error al intentar iniciar sesión")      
    
    #============================USUARIOS========================================
    def ventana_lista_usuarios(self):
        self.frame_lista_usuarios=Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_listusuarios=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listusuarios.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nuevo_usuario=tb.Button(self.lblframe_botones_listusuarios, text='Nuevo', width=15, bootstyle="success", command=self.ventana_nuevo_usuario)
        btn_nuevo_usuario.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_usuario=tb.Button(self.lblframe_botones_listusuarios, text='Modificar', width=15, bootstyle="warning")
        btn_modificar_usuario.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_usuario=tb.Button(self.lblframe_botones_listusuarios, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_usuario.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_botones_listusuarios=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listusuarios.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        self.txt_busqueda_usuarios=ttk.Entry(self.lblframe_botones_listusuarios, width=100)
        self.txt_busqueda_usuarios.grid(row=0, column=0, padx=5, pady=5)
        
        #====================================TreeView==========================================

        self.lblframe_tree_listusuarios=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listusuarios.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)

        columnas=("nombre","codigo", "clave", "rol")

        self.tree_lista_usuarios=tb.Treeview(self.lblframe_tree_listusuarios, columns=columnas, height=17, show='headings', bootstyle='dark')
        self.tree_lista_usuarios.grid(row=0, column=0)

        self.tree_lista_usuarios.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_usuarios.heading("codigo", text="Código", anchor=W)
        self.tree_lista_usuarios.heading("clave", text="Clave", anchor=W)
        self.tree_lista_usuarios.heading("rol", text="Rol", anchor=W)
        self.tree_lista_usuarios['displaycolumns']=("nombre", "codigo", "rol")

        #scrolbar
        tree_scroll_listusuarios=tb.Scrollbar(self.frame_lista_usuarios, bootstyle='round-succes')
        tree_scroll_listusuarios.grid(row=2, column=1)
        #configuracion
        tree_scroll_listusuarios.config(command=self.tree_lista_usuarios.yview)
        
        self.mostrar_usuarios()
    def mostrar_usuarios(self):
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()
            #Limpiar los datos existentes en el Treeview
            registros=self.tree_lista_usuarios.get_children()
            #Recorrer cada registro
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)

            #Ejecutar la consulta para obtener los productos
            cur.execute("SELECT * FROM usuarios")
            # Obtener los resultados
            datos = cur.fetchall()

            # Recorrer cada fila
            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))

            # Cerrar el cursor y la conexión
            conn.commit()
            conn.close()

        except:
            messagebox.showerror("Lista de Usuarios","Ocurrio un error al mostrar la lita de usuarios")
    def ventana_nuevo_usuario(self):
        self.frame_nuevo_usuario=Toplevel(self)
        self.frame_nuevo_usuario.title('Nuevo Usuario')
        self.centrar_ventana_nuevo_usuario(380, 250)
        self.frame_nuevo_usuario.resizable(0,0)
        self.frame_nuevo_usuario.grab_set()

        lblframe_nuevo_usuario=LabelFrame(self.frame_nuevo_usuario)
        lblframe_nuevo_usuario.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

        lbl_nombre_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Nombre')
        lbl_nombre_nuevo_usuario.grid(row=1, column=0, padx=10, pady=10)
        self.txt_nombre_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_nombre_nuevo_usuario.grid(row=1, column=1, padx=10, pady=10)

        lbl_codigo_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Código')
        lbl_codigo_nuevo_usuario.grid(row=2, column=0, padx=10, pady=10)
        self.txt_codigo_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_codigo_nuevo_usuario.grid(row=2, column=1, padx=10, pady=10)
        
        lbl_clave_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Clave')
        lbl_clave_nuevo_usuario.grid(row=3, column=0, padx=10, pady=10)
        self.txt_clave_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_clave_nuevo_usuario.grid(row=3, column=1, padx=10, pady=10)
        
        lbl_rol_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Rol')
        lbl_rol_nuevo_usuario.grid(row=4, column=0, padx=10, pady=10)
        self.txt_rol_nuevo_usuario=ttk.Combobox(lblframe_nuevo_usuario, values=('Administrador','Bodega', 'Vendedor'), width=36, state='readonly')
        self.txt_rol_nuevo_usuario.grid(row=4, column=1, padx=10, pady=10)
        self.txt_rol_nuevo_usuario.current(0)

        btn_guardar_nuevo_usuario=ttk.Button(lblframe_nuevo_usuario, text='Guardar',width=38, command=self.guardar_usuario)
        btn_guardar_nuevo_usuario.grid(row=9, column=1, padx=10, pady=10)
    def guardar_usuario(self):
        #Validación
        if (self.txt_nombre_nuevo_usuario.get()=="" 
            or self.txt_codigo_nuevo_usuario.get()=="" 
            or self.txt_clave_nuevo_usuario.get()=="" 
            or self.txt_rol_nuevo_usuario.get()==""
            ):
           messagebox.showwarning("Guardando usuario", "Algún campo no es valido. Intente nuevamente") 
           return 
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()

            datos_guardar_usuario = (
            self.txt_nombre_nuevo_usuario.get(),
            self.txt_codigo_nuevo_usuario.get(),
            self.txt_clave_nuevo_usuario.get(),
            self.txt_rol_nuevo_usuario.get()
            )

            # Ejecutar la consulta para insertar el usuario
            cur.execute("INSERT INTO usuarios VALUES (%s, %s, %s, %s)", datos_guardar_usuario)
            messagebox.showinfo("Guardando Usuarios", "Usuario guardado correctamente")
            # Cerrar el cursor y la conexión
            conn.commit()
            self.frame_nuevo_usuario.destroy()
            self.ventana_lista_usuarios()
            conn.close()

        except:
            messagebox.showerror("Guardando Usuarios","Ocurrio un error al Guardar Usuario")
    def centrar_ventana_nuevo_usuario(self, ancho, alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.frame_right.winfo_screenwidth()
        pantalla_alto=self.frame_right.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_nuevo_usuario.geometry("{}x{}+{}+{}".format(ventana_ancho, ventana_alto, coordenadas_x, coordenadas_y))
    def buscar_usuario(self, event):
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()
            #Limpiar los datos existentes en el Treeview
            registros=self.tree_lista_usuarios.get_children()
            #Recorrer cada registro
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)

            #Ejecutar la consulta para obtener los usuarios
            busqueda = self.txt_busqueda_usuarios.get() + '%'
            cur.execute("SELECT * FROM usuarios WHERE nombre LIKE %s", (busqueda,))
            # Obtener los resultados
            datos = cur.fetchall()

            # Recorrer cada fila
            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))

            # Cerrar el cursor y la conexión
            conn.commit()
            conn.close()

        except:
            messagebox.showerror("Búsqueda de Usuarios","Ocurrio un error al buscar el usuario")
    
    #============================PRODUCTOS========================================
    def ventana_lista_productos(self):
        self.frame_lista_productos=Frame(self.frame_center)
        self.frame_lista_productos.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_listproductos=LabelFrame(self.frame_lista_productos)
        self.lblframe_botones_listproductos.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nuevo_producto=tb.Button(self.lblframe_botones_listproductos, text='Nuevo', width=15, bootstyle="success", command=self.ventana_nuevo_producto)
        btn_nuevo_producto.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_producto=tb.Button(self.lblframe_botones_listproductos, text='Modificar', width=15, bootstyle="warning", command=self.ventana_modificar_producto)
        btn_modificar_producto.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_producto=tb.Button(self.lblframe_botones_listproductos, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_producto.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_botones_listproductos=LabelFrame(self.frame_lista_productos)
        self.lblframe_botones_listproductos.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        self.txt_busqueda_productos=ttk.Entry(self.lblframe_botones_listproductos, width=100)
        self.txt_busqueda_productos.grid(row=0, column=0, padx=5, pady=5)
        self.txt_busqueda_productos.bind('<Key>', self.buscar_producto)
        
        #====================================TreeView==========================================

        self.lblframe_tree_listproductos=LabelFrame(self.frame_lista_productos)
        self.lblframe_tree_listproductos.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)

        columnas=("id_producto","existencia", "color", "tipo_zapato", "talla", "modelo", "precio_may", "precio_men")

        self.tree_lista_productos=tb.Treeview(self.lblframe_tree_listproductos, columns=columnas, height=17, show='headings', bootstyle='dark')
        self.tree_lista_productos.grid(row=0, column=0)

        self.tree_lista_productos.column("id_producto", width=50)
        self.tree_lista_productos.column("existencia", width=80)
        self.tree_lista_productos.column("color", width=80)
        self.tree_lista_productos.column("tipo_zapato", width=80)
        self.tree_lista_productos.column("talla", width=50)
        self.tree_lista_productos.column("modelo", width=100)
        self.tree_lista_productos.column("precio_may", width=100)
        self.tree_lista_productos.column("precio_men", width=100)


        self.tree_lista_productos.heading("id_producto", text="ID", anchor=W)
        self.tree_lista_productos.heading("existencia", text="Existencia", anchor=W)
        self.tree_lista_productos.heading("color", text="Color", anchor=W)
        self.tree_lista_productos.heading("tipo_zapato", text="Estilo", anchor=W)
        self.tree_lista_productos.heading("talla", text="Talla", anchor=W)
        self.tree_lista_productos.heading("modelo", text="Modelo", anchor=W)
        self.tree_lista_productos.heading("precio_may", text="Precio mayoreo", anchor=W)
        self.tree_lista_productos.heading("precio_men", text="Precio menudeo", anchor=W)


        #scrolbar
        tree_scroll_listproductos=tb.Scrollbar(self.frame_lista_productos, bootstyle='round-succes')
        tree_scroll_listproductos.grid(row=2, column=1)
        #configuracion
        tree_scroll_listproductos.config(command=self.tree_lista_productos.yview)
        
        self.mostrar_productos()
    def mostrar_productos(self):
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()
            #Limpiar los datos existentes en el Treeview
            registros=self.tree_lista_productos.get_children()
            #Recorrer cada registro
            for elementos in registros:
                self.tree_lista_productos.delete(elementos)

            #Ejecutar la consulta para obtener los productos
            cur.execute("SELECT * FROM producto")
            # Obtener los resultados
            datos = cur.fetchall()

            # Recorrer cada fila
            for row in datos:
                self.tree_lista_productos.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

           # Consulta para obtener la suma de precios de mayoreo
            cur.execute("SELECT SUM(precio_mayoreo) FROM producto")
            sum_precio_may = cur.fetchone()[0]

            # Consulta para obtener el promedio de precios de menudeo
            cur.execute("SELECT AVG(precio_menudeo) FROM producto")
            avg_precio_men = cur.fetchone()[0]

            # Consulta para obtener el precio máximo de mayoreo
            cur.execute("SELECT MAX(precio_mayoreo) FROM producto")
            max_precio_may = cur.fetchone()[0]

            # Consulta para obtener el precio mínimo de menudeo
            cur.execute("SELECT MIN(precio_menudeo) FROM producto")
            min_precio_men = cur.fetchone()[0]

            # Cerrar el cursor y la conexión
            conn.commit()
            conn.close()

            # Mostrar los resultados en un messagebox
            info_message = f"Suma de precios de mayoreo: {sum_precio_may}\n"
            info_message += f"Promedio de precios de menudeo: {avg_precio_men}\n"
            info_message += f"Precio máximo de mayoreo: {max_precio_may}\n"
            info_message += f"Precio mínimo de menudeo: {min_precio_men}\n"

            messagebox.showinfo("Resultados", info_message)

        
        except ps.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Ocurrió un error al acceder a la base de datos: {e}")
    def ventana_nuevo_producto(self):
        self.frame_nuevo_producto=Toplevel(self)
        self.frame_nuevo_producto.title('Nuevo Producto')
        self.centrar_ventana_nuevo_producto(400, 400)
        self.frame_nuevo_producto.resizable(0,0)
        self.frame_nuevo_producto.grab_set()

        lblframe_nuevo_producto=LabelFrame(self.frame_nuevo_producto)
        lblframe_nuevo_producto.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

        lbl_id_nuevo_producto=Label(lblframe_nuevo_producto, text='ID')
        lbl_id_nuevo_producto.grid(row=1, column=0, padx=10, pady=10)
        self.txt_id_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_id_nuevo_producto.grid(row=1, column=1, padx=10, pady=10)

        lbl_existencia_nuevo_producto=Label(lblframe_nuevo_producto, text='Existencia')
        lbl_existencia_nuevo_producto.grid(row=2, column=0, padx=10, pady=10)
        self.txt_existencia_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_existencia_nuevo_producto.grid(row=2, column=1, padx=10, pady=10)
        
        lbl_color_nuevo_producto=Label(lblframe_nuevo_producto, text='Color')
        lbl_color_nuevo_producto.grid(row=3, column=0, padx=10, pady=10)
        self.txt_color_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_color_nuevo_producto.grid(row=3, column=1, padx=10, pady=10)
        
        lbl_tipo_nuevo_producto=Label(lblframe_nuevo_producto, text='Estilo')
        lbl_tipo_nuevo_producto.grid(row=4, column=0, padx=10, pady=10)
        self.txt_tipo_nuevo_producto=ttk.Combobox(lblframe_nuevo_producto, values=('Tacón','Valerina', 'Escolar','Deportivos','Mocasines','Sandalias','Zapatillas','Botas','Otro'), width=36, state='readonly')
        self.txt_tipo_nuevo_producto.grid(row=4, column=1, padx=10, pady=10)
        self.txt_tipo_nuevo_producto.current(0)
        
        lbl_talla_nuevo_producto=Label(lblframe_nuevo_producto, text='Talla')
        lbl_talla_nuevo_producto.grid(row=5, column=0, padx=10, pady=10)
        self.txt_talla_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_talla_nuevo_producto.grid(row=5, column=1, padx=10, pady=10)
        
        lbl_modelo_nuevo_producto=Label(lblframe_nuevo_producto, text='Modelo')
        lbl_modelo_nuevo_producto.grid(row=6, column=0, padx=10, pady=10)
        self.txt_modelo_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_modelo_nuevo_producto.grid(row=6, column=1, padx=10, pady=10)
        
        lbl_precioMay_nuevo_producto=Label(lblframe_nuevo_producto, text='Precio Mayoreo')
        lbl_precioMay_nuevo_producto.grid(row=7, column=0, padx=10, pady=10)
        self.txt_precioMay_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_precioMay_nuevo_producto.grid(row=7, column=1, padx=10, pady=10)
        
        lbl_precioMen_nuevo_producto=Label(lblframe_nuevo_producto, text='Precio Menudeo')
        lbl_precioMen_nuevo_producto.grid(row=8, column=0, padx=10, pady=10)
        self.txt_precioMen_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_precioMen_nuevo_producto.grid(row=8, column=1, padx=10, pady=10)

        btn_guardar_nuevo_producto=ttk.Button(lblframe_nuevo_producto, text='Guardar',width=38, command=self.guardar_producto)
        btn_guardar_nuevo_producto.grid(row=9, column=1, padx=10, pady=10)
    def guardar_producto(self):
        #Validación
        if (self.txt_id_nuevo_producto.get()=="" 
            or self.txt_existencia_nuevo_producto.get()=="" 
            or self.txt_color_nuevo_producto.get()=="" 
            or self.txt_tipo_nuevo_producto.get()==""
            or self.txt_talla_nuevo_producto.get()==""
            or self.txt_modelo_nuevo_producto.get()==""
            or self.txt_precioMay_nuevo_producto.get()==""
            or self.txt_precioMen_nuevo_producto.get()==""
        ):
           messagebox.showwarning("Guardando producto", "Algún campo no es valido. Intente nuevamente") 
           return 
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()

            datos_guardar_producto = (
            self.txt_id_nuevo_producto.get(),
            self.txt_existencia_nuevo_producto.get(),
            self.txt_color_nuevo_producto.get(),
            self.txt_tipo_nuevo_producto.get(),
            self.txt_talla_nuevo_producto.get(),
            self.txt_modelo_nuevo_producto.get(),
            self.txt_precioMay_nuevo_producto.get(),
            self.txt_precioMen_nuevo_producto.get()
            )

            # Ejecutar la consulta para insertar el producto
            cur.execute("INSERT INTO producto VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", datos_guardar_producto)
            messagebox.showinfo("Guardando Productos", "Producto guardado correctamente")
            # Cerrar el cursor y la conexión
            conn.commit()
            self.frame_nuevo_producto.destroy()
            self.ventana_lista_productos()
            conn.close()

        except:
            messagebox.showerror("Guardando Productos","Ocurrio un error al Guardar Producto")
    def centrar_ventana_nuevo_producto(self, ancho, alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.frame_right.winfo_screenwidth()
        pantalla_alto=self.frame_right.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_nuevo_producto.geometry("{}x{}+{}+{}".format(ventana_ancho, ventana_alto, coordenadas_x, coordenadas_y))
    def buscar_producto(self, event):
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()
            #Limpiar los datos existentes en el Treeview
            registros=self.tree_lista_productos.get_children()
            #Recorrer cada registro
            for elementos in registros:
                self.tree_lista_productos.delete(elementos)

            #Ejecutar la consulta para obtener los productos
            busqueda = self.txt_busqueda_productos.get() + '%'
            cur.execute("SELECT * FROM producto WHERE modelo LIKE %s", (busqueda,))
            # Obtener los resultados
            datos = cur.fetchall()

            # Recorrer cada fila
            for row in datos:
                self.tree_lista_productos.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

            # Cerrar el cursor y la conexión
            conn.commit()
            conn.close()

        except:
            messagebox.showerror("Búsqueda de Productos","Ocurrio un error al buscar el producto")
    def ventana_modificar_producto(self):
        self.producto_seleccionado=self.tree_lista_productos.focus()

        self.val_mod_prod=self.tree_lista_productos.item(self.producto_seleccionado, 'values')

        if self.val_mod_prod!='':
            self.frame_modificar_producto=Toplevel(self)
            self.frame_modificar_producto.title('Modificar Producto')
            self.frame_modificar_producto.geometry('500x400')
            #self.centrar_ventana_modificar_producto(400, 400)
            self.frame_modificar_producto.resizable(0,0)
            self.frame_modificar_producto.grab_set()

            lblframe_modificar_producto=LabelFrame(self.frame_modificar_producto)
            lblframe_modificar_producto.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

            lbl_id_modificar_producto=Label(lblframe_modificar_producto, text='ID')
            lbl_id_modificar_producto.grid(row=1, column=0, padx=10, pady=10)
            self.txt_id_modificar_producto=Entry(lblframe_modificar_producto, width=40)
            self.txt_id_modificar_producto.grid(row=1, column=1, padx=10, pady=10)

            lbl_existencia_modificar_producto=Label(lblframe_modificar_producto, text='Existencia')
            lbl_existencia_modificar_producto.grid(row=2, column=0, padx=10, pady=10)
            self.txt_existencia_modificar_producto=Entry(lblframe_modificar_producto, width=40)
            self.txt_existencia_modificar_producto.grid(row=2, column=1, padx=10, pady=10)
            
            lbl_color_modificar_producto=Label(lblframe_modificar_producto, text='Color')
            lbl_color_modificar_producto.grid(row=3, column=0, padx=10, pady=10)
            self.txt_color_modificar_producto=Entry(lblframe_modificar_producto, width=40)
            self.txt_color_modificar_producto.grid(row=3, column=1, padx=10, pady=10)
            
            lbl_tipo_modificar_producto=Label(lblframe_modificar_producto, text='Estilo')
            lbl_tipo_modificar_producto.grid(row=4, column=0, padx=10, pady=10)
            self.txt_tipo_modificar_producto=ttk.Combobox(lblframe_modificar_producto, values=('Tacón','Valerina', 'Escolar','Deportivos','Mocasines','Sandalias','Zapatillas','Botas','Otro'), width=36)
            self.txt_tipo_modificar_producto.grid(row=4, column=1, padx=10, pady=10)
            
            lbl_talla_modificar_producto=Label(lblframe_modificar_producto, text='Talla')
            lbl_talla_modificar_producto.grid(row=5, column=0, padx=10, pady=10)
            self.txt_talla_modificar_producto=Entry(lblframe_modificar_producto, width=40)
            self.txt_talla_modificar_producto.grid(row=5, column=1, padx=10, pady=10)
            
            lbl_modelo_modificar_producto=Label(lblframe_modificar_producto, text='Modelo')
            lbl_modelo_modificar_producto.grid(row=6, column=0, padx=10, pady=10)
            self.txt_modelo_modificar_producto=Entry(lblframe_modificar_producto, width=40)
            self.txt_modelo_modificar_producto.grid(row=6, column=1, padx=10, pady=10)
            
            lbl_precioMay_modificar_producto=Label(lblframe_modificar_producto, text='Precio Mayoreo')
            lbl_precioMay_modificar_producto.grid(row=7, column=0, padx=10, pady=10)
            self.txt_precioMay_modificar_producto=Entry(lblframe_modificar_producto, width=40)
            self.txt_precioMay_modificar_producto.grid(row=7, column=1, padx=10, pady=10)
            
            lbl_precioMen_modificar_producto=Label(lblframe_modificar_producto, text='Precio Menudeo')
            lbl_precioMen_modificar_producto.grid(row=8, column=0, padx=10, pady=10)
            self.txt_precioMen_modificar_producto=Entry(lblframe_modificar_producto, width=40)
            self.txt_precioMen_modificar_producto.grid(row=8, column=1, padx=10, pady=10)

            btn_guardar_modificar_producto=ttk.Button(lblframe_modificar_producto, text='Modificar',width=38, bootstyle='warning', command=self.modificar_producto)
            btn_guardar_modificar_producto.grid(row=9, column=1, padx=10, pady=10)
            self.llenar_entrys_modificar_producto()
            self.txt_id_modificar_producto.focus()
    def llenar_entrys_modificar_producto(self):
        #limpiar entrys
        self.txt_id_modificar_producto.delete(0, END)
        self.txt_existencia_modificar_producto.delete(0, END)
        self.txt_color_modificar_producto.delete(0, END)
        self.txt_tipo_modificar_producto.delete(0, END)
        self.txt_talla_modificar_producto.delete(0, END)
        self.txt_modelo_modificar_producto.delete(0, END)
        self.txt_precioMay_modificar_producto.delete(0, END)
        self.txt_precioMen_modificar_producto.delete(0, END)
        #llenar entrys
        self.txt_id_modificar_producto.insert(0, self.val_mod_prod[0])
        self.txt_id_modificar_producto.config(state='readonly')
        self.txt_existencia_modificar_producto.insert(0, self.val_mod_prod[1])
        self.txt_color_modificar_producto.insert(0, self.val_mod_prod[2])
        self.txt_tipo_modificar_producto.insert(0, self.val_mod_prod[3])
        self.txt_talla_modificar_producto.insert(0, self.val_mod_prod[4])
        self.txt_modelo_modificar_producto.insert(0, self.val_mod_prod[5])
        self.txt_precioMay_modificar_producto.insert(0, self.val_mod_prod[6])
        self.txt_precioMen_modificar_producto.insert(0, self.val_mod_prod[7])
    def modificar_producto(self):
        #Validación
        if (self.txt_id_modificar_producto.get()==""
            or self.txt_existencia_modificar_producto.get()==""
            or self.txt_color_modificar_producto.get()==""
            or self.txt_tipo_modificar_producto.get()==""
            or self.txt_talla_modificar_producto.get()==""
            or self.txt_modelo_modificar_producto.get()==""
            or self.txt_precioMay_modificar_producto.get()==""
            or self.txt_precioMen_modificar_producto.get()==""
        ):
           messagebox.showwarning("Modificar producto", "Algún campo no es valido. Intente nuevamente") 
           return 
        try:
            #Conectarse a la base de datos
            conn = ps.connect(
                dbname="proyecto",
                user="postgres",
                password="Yeika123",
                host="localhost",
                port="5432"
            )

            #Crear un cursor
            cur = conn.cursor()

            datos_modifcar_producto = (
                self.txt_existencia_modificar_producto.get(),
                self.txt_color_modificar_producto.get(),
                self.txt_tipo_modificar_producto.get(),
                self.txt_talla_modificar_producto.get(),
                self.txt_modelo_modificar_producto.get(),
                self.txt_precioMay_modificar_producto.get(),
                self.txt_precioMen_modificar_producto.get(),
                self.txt_id_modificar_producto.get()
                )

            # Ejecutar la consulta para modificar el producto
            cur.execute("""
            UPDATE producto 
            SET existencia = %s, color = %s, tipo_zapato = %s, talla = %s, modelo = %s, precio_mayoreo = %s, precio_menudeo = %s 
            WHERE id_producto = %s
            """, datos_modifcar_producto)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Modificar Productos", "Producto modificado correctamente")
            # Cerrar el cursor y la conexión
            cur.close()
            conn.close()
            # Destruir el marco de modificación de producto y actualizar la lista de productos
            self.frame_modificar_producto.destroy()
            self.ventana_lista_productos()

        except Exception as e:
            # Mostrar mensaje de error
            messagebox.showerror("Modificar Productos", f"Ocurrió un error al modificar el producto: {str(e)}")
        
def main():
    app=Ventana()
    app.title('Calzado Pacheco')
    app.state('zoomed')
    tb.Style('minty')
    app.mainloop()
    


if __name__ == '__main__':
    main()