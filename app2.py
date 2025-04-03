import streamlit as st
import pandas as pd

# Inicializar los DataFrames vacíos si no existen
if "Usuario" not in st.session_state:
    st.session_state.Usuario = pd.DataFrame(columns=["Fecha", "Nombre", "Apellidos", "Usuario"])
if "Consultas" not in st.session_state:
    st.session_state.Consultas = pd.DataFrame(columns=["Usuario", "Fecha", "Asunto", "Mensaje"])
if "Plan" not in st.session_state:
    st.session_state.Plan = pd.DataFrame(columns=["Planes", "Periodo de prueba", "Precio Mensual", "Precio Total"])
if "Predicción" not in st.session_state:
    st.session_state.Prediccion = pd.DataFrame(columns=["Fecha", "Precio predicho", "Modelo usado","Confianza"])
if "Suscripción" not in st.session_state:
    st.session_state.Suscripcion = pd.DataFrame(columns=["Usuario", "Fecha Inicio", "Fecha Fin"])

# Función para agregar datos a un DataFrame
def agregar_dato(modulo, datos):
    if modulo in st.session_state:
        st.session_state[modulo] = pd.concat([st.session_state[modulo], pd.DataFrame([datos])], ignore_index=True)

# Interfaz gráfica con Streamlit
st.title("Metabyte")
st.sidebar.title("Selecciona un Módulo para Agregar Datos")

modulo = st.sidebar.selectbox("Selecciona un módulo", ["Usuario", "Consultas", "Plan", "Prediccion", "Suscripcion"])

if modulo == "Usuario":
    st.subheader("Agregar Registro Contable")
    with st.form(key="Usuario_form"):
        fecha = st.date_input("Fecha")
        Nombre = st.text_input("Nombre")
        Apellidos = st.text_input("Apellidos")
        Usuario = st.text_input("Usuario")
        submit_button = st.form_submit_button("Agregar Registro")

    if submit_button:
        agregar_dato("Usuario", {"Fecha": fecha, "Nombre": Nombre, "Apellidos": Apellidos, "Usuario": Usuario})
        st.success("Registro agregado con éxito")

    st.subheader("Registros Contables")
    st.dataframe(st.session_state.Usuario)

elif modulo == "Consultas":
    st.subheader("¿Alguna consulta?")
    with st.form(key="Consultas_form"):
        Usuario = st.text_input("Usuario")
        Fecha = st.date_input("Fecha")
        Asunto = st.text_input("Asunto")
        Mensaje = st.text_input("Mensaje")
        submit_button = st.form_submit_button("Enviar")

    if submit_button:
        agregar_dato("Consultas", {"Usuario": Usuario, "Fecha": Fecha, "Asunto": Asunto, "Costo Total": Mensaje})
        st.success("Tu mensaje ha sido enviado con éxito con éxito")

    st.subheader("Órdenes de Compra")
    st.dataframe(st.session_state.Consultas)

elif modulo == "Plan":
    st.subheader("Agregar Venta")
    with st.form(key="Plan_form"):
        Planes = st.text_input("Planes")
        Periodo_de_prueba = st.text_input("Periodo de prueba")
        Asunto = st.number_input("Asunto", step=1, min_value=1)
        precio_total = st.number_input("Precio Total", step=100.0)
        submit_button = st.form_submit_button("Agregar Venta")

    if submit_button:
        agregar_dato("Plan", {"Planes": Planes, "Fecha": Fecha, "Asunto": Asunto, "Precio Total": precio_total})
        st.success("Venta agregada con éxito")

    st.subheader("Plan Registradas")
    st.dataframe(st.session_state.Plan)

elif modulo == "Prediccion":
    st.subheader("Agregar Prediccion")
    with st.form(key="Prediccion_form"):
        Fecha = st.text_input("Fecha")
        stock = st.number_input("Stock", step=1, min_value=0)
        ubicacion = st.text_input("Ubicación")
        submit_button = st.form_submit_button("Agregar Prediccion")

    if submit_button:
        agregar_dato("Prediccion", {"Fecha": Fecha, "Stock": stock, "Ubicación": ubicacion})
        st.success("Prediccion agregado con éxito")

    st.subheader("Prediccion Actual")
    st.dataframe(st.session_state.Prediccion)

elif modulo == "Suscripcion":
    st.subheader("Agregar Planes Suscripcion")
    with st.form(key="Suscripcion_form"):
        Planes = st.text_input("Planes")
        interaccion = st.selectbox("Interacción", ["Llamada", "Reunión", "Email", "Demo"])
        estado = st.selectbox("Estado", ["Interesado", "Negociando", "Cerrado", "Abierto"])
        submit_button = st.form_submit_button("Agregar Planes Suscripcion")

    if submit_button:
        agregar_dato("Suscripcion", {"Planes": Planes, "Interacción": interaccion, "Estado": estado})
        st.success("Planes agregado al Suscripcion")

    st.subheader("Planess en Suscripcion")
    st.dataframe(st.session_state.Suscripcion)
