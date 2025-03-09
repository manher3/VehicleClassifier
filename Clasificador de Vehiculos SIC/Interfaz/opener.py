import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO

# Cargar el modelo YOLO
model = YOLO(r'C:\Users\manuh\OneDrive\Documentos\Nueva Interfaz\best.pt') 

# Carga y clasificacion de imagen
def cargar_y_clasificar_imagen(file_path):
    # Carga de imagen
    imagen = Image.open(file_path)
    imagen.thumbnail((400, 400))  # Ajustar la imagen a la interfaz
    img_tk = ImageTk.PhotoImage(imagen)
    lbl_imagen.config(image=img_tk)
    lbl_imagen.image = img_tk  

    # Uso del modelo de yolo para identificar
    resultados = model(file_path)
    
    # Obtener la clase de vehiculo
    if resultados and len(resultados) > 0:
        detecciones = resultados[0].boxes
        if len(detecciones) > 0:
            clase_predicha_id = detecciones.cls[0].item()  # Obtener el ID de la clase
            clase_predicha = resultados[0].names[clase_predicha_id]  # Obtener el nombre de la clase
            lbl_resultado.config(text=f"Clase predicha: {clase_predicha}", fg="#4CAF50")  # Color de "Clase predicha"
        else:
            lbl_resultado.config(text="No se detectó ningún vehículo en la imagen.", fg="#F44336")  # Color en caso de no encontrar vehiculo
    else:
        lbl_resultado.config(text="No se pudo realizar la clasificación.", fg="#F44336")  # Rojo suave

# Función para cambiar a la página de clasificación
def ir_a_clasificacion():
    frame_inicio.pack_forget()  # Ocultar la página de inicio
    frame_clasificacion.pack(fill="both", expand=True)  # Mostrar la página de clasificación

# Función para volver a la página de inicio
def volver_a_inicio():
    frame_clasificacion.pack_forget()  # Ocultar la página de clasificación
    frame_seleccion_imagenes.pack_forget()  # Ocultar la sección de selección de imágenes
    frame_inicio.pack(fill="both", expand=True)  # Mostrar la página de inicio

# Función para mostrar la sección de imágenes predefinidas
def mostrar_seleccion_imagenes():
    frame_inicio.pack_forget()  # Ocultar la página de inicio
    frame_seleccion_imagenes.pack(fill="both", expand=True)  # Mostrar la sección de selección de imágenes

# Función para manejar la selección de una imagen predefinida
def seleccionar_imagen_predefinida(file_path):
    cargar_y_clasificar_imagen(file_path)  # Clasificar la imagen seleccionada
    frame_seleccion_imagenes.pack_forget()  # Ocultar la sección de selección de imágenes
    frame_clasificacion.pack(fill="both", expand=True)  # Mostrar la página de clasificación

# Crear la ventana principal de la interfaz
ventana = tk.Tk()
ventana.title("Clasificador de Vehículos")
ventana.geometry("600x700")
ventana.configure(bg="#F5F5F5")  # Fondo gris claro

# Configurar fuentes
fuente_titulo = ("Helvetica", 16, "bold")
fuente_texto = ("Helvetica", 12)
fuente_boton = ("Helvetica", 12, "bold")

# Crear frames para las páginas
frame_inicio = tk.Frame(ventana, bg="#F5F5F5")
frame_clasificacion = tk.Frame(ventana, bg="#F5F5F5")
frame_seleccion_imagenes = tk.Frame(ventana, bg="#F5F5F5")

# Página de inicio
lbl_titulo_inicio = tk.Label(
    frame_inicio, 
    text="Bienvenido al Clasificador de Vehículos", 
    font=fuente_titulo, 
    bg="#F5F5F5", 
    fg="#333333"
)
lbl_titulo_inicio.pack(pady=50)

btn_iniciar = tk.Button(
    frame_inicio, 
    text="Iniciar", 
    command=ir_a_clasificacion, 
    font=fuente_boton, 
    bg="#2196F3",  # Azul suave
    fg="white", 
    activebackground="#1976D2",  # Azul más oscuro al hacer clic
    activeforeground="white", 
    padx=20, 
    pady=10, 
    borderwidth=0, 
    relief="flat"
)
btn_iniciar.pack(pady=20)

btn_seleccionar_imagenes = tk.Button(
    frame_inicio, 
    text="Seleccionar de imágenes predefinidas", 
    command=mostrar_seleccion_imagenes, 
    font=fuente_boton, 
    bg="#4CAF50",  # Verde suave
    fg="white", 
    activebackground="#45a049",  # Verde más oscuro al hacer clic
    activeforeground="white", 
    padx=20, 
    pady=10, 
    borderwidth=0, 
    relief="flat"
)
btn_seleccionar_imagenes.pack(pady=20)

# Página de clasificación
lbl_titulo_clasificacion = tk.Label(
    frame_clasificacion, 
    text="Clasificador de Vehículos", 
    font=fuente_titulo, 
    bg="#F5F5F5", 
    fg="#333333"
)
lbl_titulo_clasificacion.pack(pady=20)

btn_cargar = tk.Button(
    frame_clasificacion, 
    text="Cargar Imagen", 
    command=lambda: cargar_y_clasificar_imagen(filedialog.askopenfilename()), 
    font=fuente_boton, 
    bg="#2196F3",  # Azul suave
    fg="white", 
    activebackground="#1976D2",  # Azul más oscuro al hacer clic
    activeforeground="white", 
    padx=20, 
    pady=10, 
    borderwidth=0, 
    relief="flat"
)
btn_cargar.pack(pady=20)

# Etiqueta para mostrar la imagen
lbl_imagen = tk.Label(frame_clasificacion, bg="#F5F5F5")
lbl_imagen.pack()

# Etiqueta para mostrar el resultado de la clasificación
lbl_resultado = tk.Label(frame_clasificacion, text="Clase predicha: ", font=fuente_texto, bg="#F5F5F5", fg="#333333")
lbl_resultado.pack(pady=20)

# Botón para volver a la página de inicio
btn_volver = tk.Button(
    frame_clasificacion, 
    text="Volver al Inicio", 
    command=volver_a_inicio, 
    font=fuente_boton, 
    bg="#9E9E9E",  # Gris suave
    fg="white", 
    activebackground="#757575",  # Gris más oscuro al hacer clic
    activeforeground="white", 
    padx=20, 
    pady=10, 
    borderwidth=0, 
    relief="flat"
)
btn_volver.pack(pady=20)

# Sección de selección de imágenes predefinidas
lbl_titulo_seleccion = tk.Label(
    frame_seleccion_imagenes, 
    text="Selecciona una imagen", 
    font=fuente_titulo, 
    bg="#F5F5F5", 
    fg="#333333"
)
lbl_titulo_seleccion.grid(row=0, column=0, columnspan=4, pady=20)  # Usar grid aquí

# Cargar las imágenes predefinidas (asegúrate de que las rutas sean correctas)
rutas_imagenes = [
    r"C:\Users\manuh\OneDrive\Documentos\VehicleClassifier\Clasificador de Vehiculos SIC\Interfaz\Fotos predet\0DC3R0VJK38J - copia.jpg",
    r"C:\Users\manuh\OneDrive\Documentos\VehicleClassifier\Clasificador de Vehiculos SIC\Interfaz\Fotos predet\Image_013192 - copia.jpg",
    r"C:\Users\manuh\OneDrive\Documentos\VehicleClassifier\Clasificador de Vehiculos SIC\Interfaz\Fotos predet\0JNYMW5VMOVW - copia.jpg",
    r"C:\Users\manuh\OneDrive\Documentos\VehicleClassifier\Clasificador de Vehiculos SIC\Interfaz\Fotos predet\Image_014341 - copia.jpg",
    r"C:\Users\manuh\OneDrive\Documentos\VehicleClassifier\Clasificador de Vehiculos SIC\Interfaz\Fotos predet\0IVEUZ7SGKSF - copia.jpg",
    r"C:\Users\manuh\OneDrive\Documentos\VehicleClassifier\Clasificador de Vehiculos SIC\Interfaz\Fotos predet\Image_000007.jpg",
    r"C:\Users\manuh\OneDrive\Documentos\VehicleClassifier\Clasificador de Vehiculos SIC\Interfaz\Fotos predet\Image_014342 - copia.jpg"
]

# Mostrar las imágenes en una cuadrícula (2 filas y 4 columnas)
for i, ruta in enumerate(rutas_imagenes):
    imagen = Image.open(ruta)
    imagen.thumbnail((120, 120))  # Redimensionar la imagen para que quepa en la cuadrícula
    img_tk = ImageTk.PhotoImage(imagen)
    
    btn_imagen = tk.Button(
        frame_seleccion_imagenes, 
        image=img_tk, 
        command=lambda ruta=ruta: seleccionar_imagen_predefinida(ruta), 
        borderwidth=0, 
        relief="flat"
    )
    btn_imagen.image = img_tk  # Mantener una referencia para evitar que la imagen sea eliminada por el recolector de basura
    btn_imagen.grid(row=(i // 4) + 1, column=i % 4, padx=10, pady=10)  # Usar grid aquí

# Botón para volver a la página de inicio desde la sección de selección de imágenes
btn_volver_seleccion = tk.Button(
    frame_seleccion_imagenes, 
    text="Volver al Inicio", 
    command=volver_a_inicio, 
    font=fuente_boton, 
    bg="#9E9E9E",  # Gris suave
    fg="white", 
    activebackground="#757575",  # Gris más oscuro al hacer clic
    activeforeground="white", 
    padx=20, 
    pady=10, 
    borderwidth=0, 
    relief="flat"
)
btn_volver_seleccion.grid(row=3, column=0, columnspan=4, pady=20)  # Usar grid aquí

# Mostrar la página de inicio al iniciar la aplicación
frame_inicio.pack(fill="both", expand=True)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()