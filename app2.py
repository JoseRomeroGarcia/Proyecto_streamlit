import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dashboard simple")

# Crear datos de ejemplo
data = pd.DataFrame({
    "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    "Ventas": [100, 150, 80, 200, 170]
})

st.write("### Datos:")
st.dataframe(data)

# Selector
dia = st.selectbox("Elige un día:", data["Día"])
venta = data[data["Día"] == dia]["Ventas"].values[0]

st.write(f"Ventas en {dia}: {venta}")

# Gráfico
fig, ax = plt.subplots()
ax.bar(data["Día"], data["Ventas"])
st.pyplot(fig)