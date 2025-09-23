# Paquetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import streamlit as st
import plotly.express as px

Datos = pd.read_csv("Resumen de Asistencia_20250922153841.csv", header = 0)

# Extraer la última columna
Ultima_col = Datos.iloc[:,-1]



# El numero de registros maximo en tiempos es 6

# Ordenar las horas de checada
registros, columnas = Datos.shape


# Extraer strings de ocho caracteres para cada hora
Hora1 = []
Hora2 = []
Hora3 = []
Hora4 = []
Hora5 = []
Hora6 = []
Minutos1 = []
Minutos2 = []
Minutos3 = []
Minutos4 = []
Minutos5 = []
Minutos6 = []
Tabla1 = []
Tabla2 = []
Tabla3 = []
Tabla4 = []
Tabla5 = []
Tabla6 = []
for i in range(registros):
    string_comp = str(Ultima_col.iloc[i])   # Cadena completa
    Tabla1.append(string_comp[0:5])
    Tabla2.append(string_comp[9:14])
    Tabla3.append(string_comp[18:23])
    Tabla4.append(string_comp[27:32])
    Tabla5.append(string_comp[36:41])
    Tabla6.append(string_comp[45:50])
    Hora1.append(string_comp[0:2])
    Minutos1.append(string_comp[3:5])
    Hora2.append(string_comp[9:11])
    Minutos2.append(string_comp[12:14])
    Hora3.append(string_comp[18:20])
    Minutos3.append(string_comp[21:23])
    Hora4.append(string_comp[27:29])
    Minutos4.append(string_comp[30:32])
    Hora5.append(string_comp[36:38])
    Minutos5.append(string_comp[39:41])
    Hora6.append(string_comp[45:47])
    Minutos6.append(string_comp[48:50])

# Cambiar los espacios vacios por ceros
for i in range(registros):
    Hora1[i] = "00" if Hora1[i]=="" else Hora1[i]
    Hora2[i] = "00" if Hora2[i]=="" else Hora2[i]
    Hora3[i] = "00" if Hora3[i]=="" else Hora3[i]
    Hora4[i] = "00" if Hora4[i]=="" else Hora4[i]
    Hora5[i] = "00" if Hora5[i]=="" else Hora5[i]
    Hora6[i] = "00" if Hora6[i]=="" else Hora6[i]
    Minutos1[i] = "00" if Minutos1[i]=="" else Minutos1[i]
    Minutos2[i] = "00" if Minutos2[i]=="" else Minutos2[i]
    Minutos3[i] = "00" if Minutos3[i]=="" else Minutos3[i]
    Minutos4[i] = "00" if Minutos4[i]=="" else Minutos4[i]
    Minutos5[i] = "00" if Minutos5[i]=="" else Minutos5[i]
    Minutos6[i] = "00" if Minutos6[i]=="" else Minutos6[i]
    


# Cambiar a numeros cada string
Hora11 = []
Hora22 = []
Hora33 = []
Hora44 = []
Hora55 = []
Hora66 = []
Minutos11 = []
Minutos22 = []
Minutos33 = []
Minutos44 = []
Minutos55 = []
Minutos66 = []
for i in range(registros):
    Hora11.append(int(Hora1[i]))
    Minutos11.append(int(Minutos1[i]))
    Hora22.append(int(Hora2[i]))
    Minutos22.append(int(Minutos2[i]))
    Hora33.append(int(Hora3[i]))
    Minutos33.append(int(Minutos3[i]))
    Hora44.append(int(Hora4[i]))
    Minutos44.append(int(Minutos4[i]))
    Hora55.append(int(Hora5[i]))
    Minutos55.append(int(Minutos5[i]))
    Hora66.append(int(Hora6[i]))
    Minutos66.append(int(Minutos6[i]))

# Sumar minutos y horas
Time1 = np.zeros((registros,1))
Time2 = np.zeros((registros,1))
Time3 = np.zeros((registros,1))
Time4 = np.zeros((registros,1))
Time5 = np.zeros((registros,1))
Time6 = np.zeros((registros,1))
for i in range(registros):
    Time1[i] = Hora11[i]*60 + Minutos11[i]
    Time2[i] = Hora22[i]*60 + Minutos22[i]
    Time3[i] = Hora33[i]*60 + Minutos33[i]
    Time4[i] = Hora44[i]*60 + Minutos44[i]
    Time5[i] = Hora55[i]*60 + Minutos55[i]
    Time6[i] = Hora66[i]*60 + Minutos66[i]

# Crear matriz de tiempos
Tiempos = np.concatenate((Time1,Time2,Time3,Time4,Time5,Time6), axis = 1)

Maximos = []
# Ordenar por filas
for i in range(registros):
    Tiempos[i,:] = np.sort(Tiempos[i,:])
    Maximos.append(np.max(Tiempos[i,:]))



registros2, columnas2 = Tiempos.shape

Minimos = []
for i in range(registros):
    for j in range(columnas2):
        if Tiempos[i,j] == 0:
            Tiempos[i,j] = 100000000


for i in range(registros):
    Minimos.append(np.min(Tiempos[i,:]))

for i in range(registros):
    for j in range(columnas2):
        if Tiempos[i,j] == 100000000:
            Tiempos[i,j] = 0
        

df = pd.DataFrame(Tiempos,
        columns = ["Tiempo1","Tiempo2","Tiempo3","Tiempo4","Tiempo5","Tiempo6"])

# Eliminar la ultima columna
Datos = Datos.drop(['Hora'], axis=1)


Datos["Hora1"] = Tabla1
Datos["Hora2"] = Tabla2
Datos["Hora3"] = Tabla3
Datos["Hora4"] = Tabla4
Datos["Hora5"] = Tabla5
Datos["Hora6"] = Tabla6


Datos["Hora11"] = df["Tiempo1"]
Datos["Hora22"] = df["Tiempo2"]
Datos["Hora33"] = df["Tiempo3"]
Datos["Hora44"] = df["Tiempo4"]
Datos["Hora55"] = df["Tiempo5"]
Datos["Hora66"] = df["Tiempo6"]

Datos["Minimo"] = Minimos
Datos["Maximo"] = Maximos

# Concatenar las columnas de nombre y apellido
Datos['Nombre_completo'] = Datos.Nombre.str.cat(Datos.Apellido, sep=' ')
Datos[['ID de Empleado', 'Nombre', 'Apellido','Nombre_completo',
       'Fecha', 'Cantidad de Checadas', 'Hora11', 'Hora22', 
       'Hora33', 'Hora44','Hora55', 'Hora66', 'Minimo', 'Maximo']]


# Cambiar NAs
Datos = Datos.fillna(0)




# Asistencias
Asistencias = Datos[["ID de Empleado", "Nombre","Apellido"]].value_counts()


# Registros
Registros, cols = Datos.shape


Datos["Maximo"] = pd.to_numeric(Datos["Maximo"], errors="coerce").fillna(0)

# Retardos
retardo = np.zeros(Registros)
for registro in range(Registros):
    if Datos.loc[registro,"Minimo"] > 490:
        retardo[registro] = Datos.loc[registro,"Minimo"] - 490


        
Datos["Retardo_min"] = retardo


# Horas extras
overtime = np.zeros(Registros)
for registro in range(Registros):
    if Datos.loc[registro,"Maximo"] > 1050:
        overtime[registro] = np.round((Datos.loc[registro,"Maximo"] - 1020)/60)


Datos["Tiempo_extra"] = overtime

# Ajustar la cantidad de registros si es mayor que 4
for registro in range(Registros):
    if Datos.loc[registro,"Cantidad de Checadas"] > 4 :
        Datos.loc[registro,"Cantidad de Checadas"] = 4



# Agrupar horas extras por ID
Horas_extra = Datos.groupby(['ID de Empleado', 'Nombre','Apellido'])['Tiempo_extra'].sum()

# Tiempo de retardo por ID
Tiempo_retardo = Datos.groupby(['ID de Empleado', 'Nombre','Apellido'])['Retardo_min'].sum()

# Checadas
Checadas = Datos.groupby(['ID de Empleado', 'Nombre','Apellido'])['Cantidad de Checadas'].sum()

# Unir dataframes
Asistencias = pd.DataFrame(Asistencias)
Horas_extra = pd.DataFrame(Horas_extra)
Tiempo_retardo = pd.DataFrame(Tiempo_retardo)
Checadas = pd.DataFrame(Checadas)

reporte_1 = Asistencias.merge(Horas_extra, on=['ID de Empleado','Nombre','Apellido'])
reporte_2 = reporte_1.merge(Tiempo_retardo, on=['ID de Empleado','Nombre','Apellido'])
reporte_avance = reporte_2.merge(Checadas, on=['ID de Empleado','Nombre','Apellido'])
reporte_avance = reporte_avance.rename(columns={'count': 'Asistencia'})

# Convertir columnas de texto a string
for col in ["Nombre", "Apellido", "Nombre_completo"]:
    if col in Datos.columns:
        Datos[col] = Datos[col].astype(str)

for col in ["Nombre", "Apellido"]:
    if col in reporte_avance.index.names:
        reporte_avance = reporte_avance.reset_index()
        reporte_avance[col] = reporte_avance[col].astype(str)


# ================================
# Dashboard con Streamlit
# ================================

st.set_page_config(page_title="Dashboard de Asistencia", layout="wide")

# Contenedor vacío para evitar la visualización automática
placeholder = st.empty()


st.title("📊 Dashboard de Asistencia de Personal")


st.markdown("---")

# --- Indicadores principales ---
# Número de días trabajados en el dataset
dias_laborales = Datos['Fecha'].nunique()


# Número de empleados únicos
trabajadores = Datos['ID de Empleado'].nunique()

# Asistencias reales (conteo de registros únicos por empleado y fecha)
asistencias_reales = reporte_avance["Asistencia"].sum()

# Asistencias esperadas
asistencias_esperadas = dias_laborales * trabajadores

# Faltas totales
faltas_totales = asistencias_esperadas - asistencias_reales

# Nivel de ausentismo en porcentaje
nivel_ausentismo = round((faltas_totales / asistencias_esperadas) * 100, 2)

tiempo_total_extra = reporte_avance["Tiempo_extra"].sum()
tiempo_total_retardo = reporte_avance["Retardo_min"].sum()

# Supongamos costo de hora extra = 120 pesos/hora
costo_estimado = tiempo_total_extra * 120

col1, col2, col3, col4 = st.columns(4)
col1.metric("📅 Nivel de Ausentismo", f"{nivel_ausentismo} faltas/dia")
col2.metric("⏱ Total Horas Extra", f"{tiempo_total_extra:.1f} hrs")
col3.metric("💲 Costo Estimado Horas Extra", f"$ {costo_estimado:,.0f}")
col4.metric("⌛ Tiempo Total de Retardo", f"{tiempo_total_retardo:.0f} min")

st.markdown("---")

# --- Rankings ---
st.subheader("🏆 Ranking de trabajadores")

top_extra = reporte_avance.sort_values("Tiempo_extra", ascending=False).head(10).reset_index()
top_retardo = reporte_avance.sort_values("Retardo_min", ascending=False).head(10).reset_index()

col5, col6 = st.columns(2)

with col5:
    st.write("### Más Horas Extra")
    fig_extra = px.bar(
        top_extra,
        x="Tiempo_extra",
        y="Nombre",
        orientation="h",
        text="Tiempo_extra",
        labels={"Tiempo_extra": "Horas extra", "Nombre": "Colaborador"},
        title="Top Horas Extra"
    )
    fig_extra.update_traces(marker_color="#1f77b4", textposition="outside")
    fig_extra.update_layout(yaxis={"categoryorder":"total ascending"})
    st.plotly_chart(fig_extra, use_container_width=True)

with col6:
    st.write("### Más Tiempo de Retardo")
    fig_retardo = px.bar(
        top_retardo,
        x="Retardo_min",
        y="Nombre",
        orientation="h",
        text="Retardo_min",
        labels={"Retardo_min": "Minutos de retardo", "Nombre": "Empleado"},
        title="Top Retardos"
    )
    fig_retardo.update_traces(marker_color="#d62728", textposition="outside")
    fig_retardo.update_layout(yaxis={"categoryorder":"total ascending"})
    st.plotly_chart(fig_retardo, use_container_width=True)

# --- Tabla general ---
st.write("📋 Reporte completo de asistencia")
reporte_completo = reporte_avance.reset_index()
st.dataframe(reporte_completo, hide_index=True)
