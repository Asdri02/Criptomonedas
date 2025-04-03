import streamlit as st
import pandas as pd

# Inicializar los DataFrames vacíos si no existen
if "Usuario" not in st.session_state:
    st.session_state.Usuario = pd.DataFrame(columns=["Fecha", "Nombre", "Apellidos", "Usuario"])
if "Consultas" not in st.session_state:
    st.session_state.Consultas = pd.DataFrame(columns=["Usuario", "Fecha", "Asunto", "Mensaje"])
if "Plan" not in st.session_state:
    st.session_state.Plan = pd.DataFrame(columns=["Planes", "Periodo de prueba", "Asunto", "Precio Total"])
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
        fecha_de_nacimiento = st.date_input("Fecha")
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
        Planes = st.selectbox("Plan", ["Plan FREE", " Plan ANALISTA", "Plan TRADER","Plan VIP"])
        Periodo_de_prueba = st.print("Tendrás un periodo de prueba de 7 días")
        precio_total = st.text_input("Precio Total")
        submit_button = st.form_submit_button("Agregar Venta")

    if submit_button:
        agregar_dato("Plan", {"Planes": Planes, "Periodo de prueba": Periodo_de_prueba, "Precio Total": precio_total})
        st.success("Venta agregada con éxito")

    st.subheader("Plan Registradas")
    st.dataframe(st.session_state.Plan)

elif modulo == "Prediccion":
    st.subheader("Agregar Prediccion")
    with st.form(key="Prediccion_form"):
        Fecha = st.date_input("Fecha")
        Precio predicho = st.number_input("Precio predicho")
        Modelo usado = st.text_input("Modelo usado")
        Confianza = st.print("78%")("Confianza")
        submit_button = st.form_submit_button("Agregar Prediccion")

    if submit_button:
        agregar_dato("Prediccion", {"Fecha": Fecha, "Stock": stock, "Ubicación": ubicacion, "Confianza": Confianza})
        st.success("Prediccion agregada con éxito")

    st.subheader("Prediccion Actual")
    st.dataframe(st.session_state.Prediccion)

elif modulo == "Suscripcion":
    st.subheader("Agregar Planes Suscripcion")
    with st.form(key="Suscripcion_form"):
        Usuario = st.text_input("Usuario")
        Fecha_Inicio = st.date_input("Fecha")
        Fecha_Fin = st.date_input("Fecha")
        submit_button = st.form_submit_button("Agregar Suscripcion")

    if submit_button:
        agregar_dato("Suscripcion", {"Usuario": Usuario, "Fecha Inicio": Fecha_Inicio, "Fecha Fin": Fecha_Fin})
        st.success("Planes agregado al Suscripcion")

    st.subheader("Planess en Suscripcion")
    st.dataframe(st.session_state.Suscripcion)
