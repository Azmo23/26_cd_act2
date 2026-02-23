import streamlit as st
import random

st.title("Ejercicios de Streamlit")

# Ejercicio 1: Saludo simple
st.subheader("Ejercicio 1: Saludo simple", divider="red")
nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"¡Hola, {nombre}! Bienvenido a Streamlit.")
else:
    st.warning("Por favor, ingresa tu nombre para recibir un saludo.")

st.divider()

#Ejercicio 2: Calculadora de producto

st.subheader("Ejercicio 2: Calculadora de producto", divider="red")
num1 = st.number_input("Ingresa el primer número", value=0)
num2 = st.number_input("Ingresa el segundo número", value=0)
producto = num1 * num2
if num1 > 100 or num2 > 100:
    st.warning("Números grandes")
else:
    st.success(f"El producto de {num1} y {num2} es: {producto}")

st.divider()

#Ejercicio 3: Convertidor de temperatura (Radio Buttons)
st.subheader("Ejercicio 3: Convertidor de temperatura", divider="red")
opcion = st.radio("Selecciona la conversión", ("Celsius a Fahrenheit", "Fahrenheit a Celsius"))
temperatura = st.number_input("Ingresa la temperatura a convertir", value=0.0)
if opcion == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
    st.success(f"{temperatura}°C es igual a {resultado}°F")
else:
    resultado = (temperatura - 32) * 5/9
    st.success(f"{temperatura}°F es igual a {resultado}°C")

st.divider()

#Ejercicio 4: Galeria de mascotas (Tabs)
# *   Crea 3 pestañas: "Gatos", "Perros", "Aves".
# *   En cada pestaña muestra una imagen diferente (puedes usar URLs públicas) y un botón de "Me gusta" que, al ser presionado, muestre un `st.toast` diciendo "Te gusta esta mascota".
st.subheader("Ejercicio 4: Galería de mascotas", divider="red")
tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])
with tab1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/640px-Cat_November_2010-1a.jpg", caption="Gato")
    if st.button("Me gusta", key="like_gato"):
        st.toast("Te gusta esta mascota")
with tab2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/My_dog%2C_her_name_is_Becky.jpg/640px-My_dog%2C_her_name_is_Becky.jpg", caption="Perro")
    if st.button("Me gusta", key="like_perro"):
        st.toast("Te gusta esta mascota")
with tab3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Psittacus_erithacus_qtl1.jpg/640px-Psittacus_erithacus_qtl1.jpg", caption="Ave")
    if st.button("Me gusta", key="like_ave"):
        st.toast("Te gusta esta mascota")

st.divider()

#Ejercicio 5: Caja de comentarios (Formularios)
st.subheader("Ejercicio 5: Caja de comentarios", divider="red")
asunto = st.text_input("Asunto:")
cometario = st.text_area("Escribe tu comentario: ")
if st.button("Enviar comentario"):
    if cometario.strip() != "" and asunto.strip() != "":
        st.json({"Asunto": asunto, "Comentario": cometario})
    else:
        st.warning("El mensaje y/o el asunto no pueden estar vacíos.")
        
st.divider()

#Ejercicio 6: Login Simulado (Session State)
st.subheader("Ejercicio 6: Login Simulado", divider="red")
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if not st.session_state["logged_in"]:
    user = st.text_input("Usuario:")
    password = st.text_input("Contraseña:", type="password")
    ingresar = st.button("Ingresar")
    if ingresar:
        if user == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("¡Has ingresado correctamente!")
        else:
            st.error("Usuario o contraseña incorrectos.")
if st.session_state["logged_in"]:
    logout = st.button("Cerrar sesión")
    if logout:
        st.session_state["logged_in"] = False
        st.info("Has cerrado sesión.")
        st.rerun()  
        
st.divider()

# Ejercicio 7: Lista de Compras (Session State)

st.subheader("Ejercicio 7: Lista de Compras", divider="red")
if "lista_compras" not in st.session_state:
    st.session_state["lista_compras"] = []
if "item_key" not in st.session_state:
    st.session_state["item_key"] = 0
nuevo_producto = st.text_input("Ingresa un producto:" , key=f"item_input_{st.session_state.item_key}") 
if st.button("Agregar"):
    if nuevo_producto.strip() != "":
        st.session_state.lista_compras.append(nuevo_producto)
        st.session_state.item_key += 1
        st.success(f"Producto '{nuevo_producto}' agregado a la lista.")
        st.rerun()
    else:
        st.warning("El producto no puede estar vacío.")

if st.session_state.lista_compras:
    st.subheader("Productos en tu lista de compras:")
    for idx, producto in enumerate(st.session_state.lista_compras, start=1):
        st.write(f"{idx}. {producto}")
if st.button("Limpiar Lista"):
    st.session_state.lista_compras.clear()
    st.session_state.item_key = 0
    st.info("Lista de compras limpiada.")
    st.rerun()        

st.divider()

# Ejercicio 8: Gráfico Interactivo
st.subheader("Ejercicio 8: Gráfico Interactivo", divider="red")
N = st.slider("Selecciona un número N", min_value=10, max_value=100, value=50)
datos = [random.randint(0, 100) for _ in range(N)]
st.line_chart(datos)
if st.button("Regenerar"):
    st.rerun()
    
    
    


        





