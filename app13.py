import streamlit as st
import pandas as pd
import os
os.system('pip install mysql-connector-python')



# FUNCION PARA INSERTAR EN LA BASE DE DATOS
def insertar_en_bd(modulo, datos):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="1234", 
            database="Criptomonedas"
        )

        cursor = conexion.cursor()

        if modulo == "Usuario":
            sql = "INSERT INTO Usuario (Fecha, Nombre, Apellidos, Usuario) VALUES (%s, %s, %s, %s)"
            valores = (
                datos["Fecha"].strftime('%Y-%m-%d'),
                datos["Nombre"],
                datos["Apellidos"],
                datos["Usuario"]
            )
            cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()
        print("✅ Registro insertado en la base de datos.")

    except mysql.connector.Error as err:
        print(f"❌ Error al insertar en la base de datos: {err}")

# INICIALIZACIÓN DE DATAFRAMES EN SESIÓN
if "Usuario" not in st.session_state:
    st.session_state.Usuario = pd.DataFrame(columns=["Fecha", "Nombre", "Apellidos", "Usuario"])

# FUNCION PARA AGREGAR DATOS LOCALMENTE EN LA SESIÓN
def agregar_dato(modulo, datos):
    if modulo in st.session_state:
        st.session_state[modulo] = pd.concat([st.session_state[modulo], pd.DataFrame([datos])], ignore_index=True)

# INTERFAZ DE USUARIO CON STREAMLIT
st.title("Metabyte")
st.sidebar.title("Selecciona un Módulo para Agregar Datos")

modulo = st.sidebar.selectbox("Selecciona un módulo", ["Usuario"])

if modulo == "Usuario":
    st.subheader("Agregar Registro de Usuario")
    with st.form(key="Usuario_form"):
        fecha = st.date_input("Fecha de nacimiento")
        nombre = st.text_input("Nombre")
        apellidos = st.text_input("Apellidos")
        usuario = st.text_input("Usuario")
        submit_button = st.form_submit_button("Agregar Registro")

    if submit_button:
        datos = {
            "Fecha": fecha,
            "Nombre": nombre,
            "Apellidos": apellidos,
            "Usuario": usuario
        }
        agregar_dato("Usuario", datos)
        insertar_en_bd("Usuario", datos)
        st.success("✅ Registro agregado con éxito")

    st.subheader("Registros actuales")
    st.dataframe(st.session_state.Usuario)

