import streamlit as st
import pandas as pd

# Inicializar los DataFrames vacíos si no existen
if "contabilidad" not in st.session_state:
    st.session_state.contabilidad = pd.DataFrame(columns=["Fecha", "Concepto", "Monto", "Tipo"])
if "compras" not in st.session_state:
    st.session_state.compras = pd.DataFrame(columns=["Proveedor", "Producto", "Cantidad", "Costo Total"])
if "ventas" not in st.session_state:
    st.session_state.ventas = pd.DataFrame(columns=["Cliente", "Producto", "Cantidad", "Precio Total"])
if "inventario" not in st.session_state:
    st.session_state.inventario = pd.DataFrame(columns=["Producto", "Stock", "Ubicación"])
if "crm" not in st.session_state:
    st.session_state.crm = pd.DataFrame(columns=["Cliente", "Interacción", "Estado"])

# Función para agregar datos a un DataFrame
def agregar_dato(modulo, datos):
    if modulo in st.session_state:
        st.session_state[modulo] = pd.concat([st.session_state[modulo], pd.DataFrame([datos])], ignore_index=True)

# Interfaz gráfica con Streamlit
st.title("Simulación de un ERP-CRM")
st.sidebar.title("Selecciona un Módulo para Agregar Datos")

modulo = st.sidebar.selectbox("Selecciona un módulo", ["Contabilidad", "Compras", "Ventas", "Inventario", "CRM"])

if modulo == "Contabilidad":
    st.subheader("Agregar Registro Contable")
    with st.form(key="contabilidad_form"):
        fecha = st.date_input("Fecha")
        concepto = st.text_input("Concepto")
        monto = st.number_input("Monto", step=100.0)
        tipo = st.selectbox("Tipo", ["Ingreso", "Egreso"])
        submit_button = st.form_submit_button("Agregar Registro")

    if submit_button:
        agregar_dato("contabilidad", {"Fecha": fecha, "Concepto": concepto, "Monto": monto, "Tipo": tipo})
        st.success("Registro agregado con éxito")

    st.subheader("Registros Contables")
    st.dataframe(st.session_state.contabilidad)

elif modulo == "Compras":
    st.subheader("Agregar Orden de Compra")
    with st.form(key="compras_form"):
        proveedor = st.text_input("Proveedor")
        producto = st.text_input("Producto")
        cantidad = st.number_input("Cantidad", step=1, min_value=1)
        costo_total = st.number_input("Costo Total", step=100.0)
        submit_button = st.form_submit_button("Agregar Orden")

    if submit_button:
        agregar_dato("compras", {"Proveedor": proveedor, "Producto": producto, "Cantidad": cantidad, "Costo Total": costo_total})
        st.success("Orden de compra agregada con éxito")

    st.subheader("Órdenes de Compra")
    st.dataframe(st.session_state.compras)

elif modulo == "Ventas":
    st.subheader("Agregar Venta")
    with st.form(key="ventas_form"):
        cliente = st.text_input("Cliente")
        producto = st.text_input("Producto")
        cantidad = st.number_input("Cantidad", step=1, min_value=1)
        precio_total = st.number_input("Precio Total", step=100.0)
        submit_button = st.form_submit_button("Agregar Venta")

    if submit_button:
        agregar_dato("ventas", {"Cliente": cliente, "Producto": producto, "Cantidad": cantidad, "Precio Total": precio_total})
        st.success("Venta agregada con éxito")

    st.subheader("Ventas Registradas")
    st.dataframe(st.session_state.ventas)

elif modulo == "Inventario":
    st.subheader("Agregar Inventario")
    with st.form(key="inventario_form"):
        producto = st.text_input("Producto")
        stock = st.number_input("Stock", step=1, min_value=0)
        ubicacion = st.text_input("Ubicación")
        submit_button = st.form_submit_button("Agregar Inventario")

    if submit_button:
        agregar_dato("inventario", {"Producto": producto, "Stock": stock, "Ubicación": ubicacion})
        st.success("Inventario agregado con éxito")

    st.subheader("Inventario Actual")
    st.dataframe(st.session_state.inventario)

elif modulo == "CRM":
    st.subheader("Agregar Cliente CRM")
    with st.form(key="crm_form"):
        cliente = st.text_input("Cliente")
        interaccion = st.selectbox("Interacción", ["Llamada", "Reunión", "Email", "Demo"])
        estado = st.selectbox("Estado", ["Interesado", "Negociando", "Cerrado", "Abierto"])
        submit_button = st.form_submit_button("Agregar Cliente CRM")

    if submit_button:
        agregar_dato("crm", {"Cliente": cliente, "Interacción": interaccion, "Estado": estado})
        st.success("Cliente agregado al CRM")

    st.subheader("Clientes en CRM")
    st.dataframe(st.session_state.crm)
