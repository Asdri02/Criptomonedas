import streamlit as st
import pandas as pd
import os
os.system('pip install mysql-connector-python')

# Función para insertar en la base de datos
def insertar_en_bd(modulo, datos):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # ⬅️ CAMBIA esto si es necesario
            password="tu_contraseña",  # ⬅️ CAMBIA esto también
            database="cripto"
        )
        cursor = conexion.cursor()

        if modulo == "Usuario":
            cursor.execute("INSERT INTO Usuario (Fecha, Nombre, Apellidos, Usuario) VALUES (%s, %s, %s, %s)",
                           (datos["Fecha"].strftime('%Y-%m-%d'), datos["Nombre"], datos["Apellidos"], datos["Usuario"]))
        elif modulo == "Consultas":
            cursor.execute("INSERT INTO Consultas (Usuario, Fecha, Asunto, Mensaje) VALUES (%s, %s, %s, %s)",
                           (datos["Usuario"], datos["Fecha"].strftime('%Y-%m-%d'), datos["Asunto"], datos["Mensaje"]))
        elif modulo == "Plan":
            cursor.execute("INSERT INTO Plan (Planes, PeriodoDePrueba, PrecioTotal) VALUES (%s, %s, %s)",
                           (datos["Planes"], datos["PeriodoDePrueba"], datos["PrecioTotal"]))
        elif modulo == "Prediccion":
            cursor.execute("INSERT INTO Prediccion (Fecha, PrecioPredicho, ModeloUsado, Confianza) VALUES (%s, %s, %s, %s)",
                           (datos["Fecha"].strftime('%Y-%m-%d'), datos["PrecioPredicho"], datos["ModeloUsado"], datos["Confianza"]))
        elif modulo == "Suscripcion":
            cursor.execute("INSERT INTO Suscripcion (Usuario, FechaInicio, FechaFin) VALUES (%s, %s, %s)",
                           (datos["Usuario"], datos["FechaInicio"].strftime('%Y-%m-%d'), datos["FechaFin"].strftime('%Y-%m-%d')))

        conexion.commit()
        cursor.close()
        conexion.close()

    except mysql.connector.Error as err:
        st.error(f"Error al insertar en base de datos: {err}")

# Inicializar los DataFrames vacíos
modulos = ["Usuario", "Consultas", "Plan", "Prediccion", "Suscripcion"]
for m in modulos:
    if m not in st.session_state:
        st.session_state[m] = pd.DataFrame()

# Agregar a sesión y base de datos
def agregar_dato(modulo, datos):
    st.session_state[modulo] = pd.concat([st.session_state[modulo], pd.DataFrame([datos])], ignore_index=True)
    insertar_en_bd(modulo, datos)

# Interfaz gráfica
st.title("Metabyte")
modulo = st.sidebar.selectbox("Selecciona un módulo", modulos)

if modulo == "Usuario":
    st.subheader("Agregar Usuario")
    with st.form("form_usuario"):
        Fecha = st.date_input("Fecha de nacimiento")
        Nombre = st.text_input("Nombre")
        Apellidos = st.text_input("Apellidos")
        Usuario = st.text_input("Usuario")
        if st.form_submit_button("Agregar"):
            datos = {"Fecha": Fecha, "Nombre": Nombre, "Apellidos": Apellidos, "Usuario": Usuario}
            agregar_dato("Usuario", datos)
            st.success("Usuario agregado")

elif modulo == "Consultas":
    st.subheader("Agregar Consulta")
    with st.form("form_consulta"):
        Usuario = st.text_input("Usuario")
        Fecha = st.date_input("Fecha")
        Asunto = st.text_input("Asunto")
        Mensaje = st.text_area("Mensaje")
        if st.form_submit_button("Enviar"):
            datos = {"Usuario": Usuario, "Fecha": Fecha, "Asunto": Asunto, "Mensaje": Mensaje}
            agregar_dato("Consultas", datos)
            st.success("Consulta enviada")

elif modulo == "Plan":
    st.subheader("Agregar Plan")
    with st.form("form_plan"):
        Planes = st.selectbox("Tipo de Plan", ["Plan FREE", "Plan ANALISTA", "Plan TRADER", "Plan VIP"])
        Periodo = st.text_input("Periodo de prueba")
        Precio = st.text_input("Precio Total")
        if st.form_submit_button("Agregar"):
            datos = {"Planes": Planes, "PeriodoDePrueba": Periodo, "PrecioTotal": Precio}
            agregar_dato("Plan", datos)
            st.success("Plan registrado")

elif modulo == "Prediccion":
    st.subheader("Agregar Predicción")
    with st.form("form_prediccion"):
        Fecha = st.date_input("Fecha")
        Precio = st.number_input("Precio predicho")
        Modelo = st.text_input("Modelo usado")
        Confianza = st.text_input("Confianza")
        if st.form_submit_button("Agregar"):
            datos = {"Fecha": Fecha, "PrecioPredicho": Precio, "ModeloUsado": Modelo, "Confianza": Confianza}
            agregar_dato("Prediccion", datos)
            st.success("Predicción guardada")

elif modulo == "Suscripcion":
    st.subheader("Agregar Suscripción")
    with st.form("form_suscripcion"):
        Usuario = st.text_input("Usuario")
        FechaInicio = st.date_input("Fecha de Inicio")
        FechaFin = st.date_input("Fecha de Fin")
        if st.form_submit_button("Agregar"):
            datos = {"Usuario": Usuario, "FechaInicio": FechaInicio, "FechaFin": FechaFin}
            agregar_dato("Suscripcion", datos)
            st.success("Suscripción añadida")

# Mostrar datos actuales
st.subheader("Registros actuales")
st.dataframe(st.session_state[modulo])


