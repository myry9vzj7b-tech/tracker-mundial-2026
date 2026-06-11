import streamlit as st
import pandas as pd

# Configuración principal
st.set_page_config(page_title="Tracker Mundial 2026", layout="wide")

# 🎨 CSS Mundialista
st.markdown("""
    <style>
    .stApp { background-color: #0b3b24; color: #f0f2f6; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Arial Black', sans-serif; }
    div[data-testid="stMarkdownContainer"] > p {
        background-color: #155d3a; padding: 15px; border-radius: 10px; border-left: 5px solid #d4af37;
    }
    button[data-baseweb="tab"] { background-color: #0b3b24 !important; color: white !important; }
    button[data-baseweb="tab"][aria-selected="true"] { border-bottom: 4px solid #d4af37 !important; }
    .stNumberInput > div > div > input { color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 Mi Tracker Mundialista - Reto Novibet")

# 🗂️ Pestañas de la App
tab1, tab2, tab3, tab4 = st.tabs([
    "📅 Jornada 1 (Fase de Grupos)", 
    "🐢 Reto Lento ($20)", 
    "⚡ Reto Sprint ($30)",
    "🧮 Calculadora"
])

# ==========================================
# PESTAÑA 1: CARTELERA Y ANÁLISIS DE LA JORNADA 1
# ==========================================
with tab1:
    st.header("Cartelera Completa: Jornada 1")
    st.write("Despliega cada grupo para ver los análisis y consejos iniciales.")
    
    # Estructura de datos dinámica (Mejor práctica de desarrollo web)
    grupos_jornada1 = {
        "⚽ Grupo A": [
            {"partido": "🇲🇽 México vs. 🇿🇦 Sudáfrica", "info": "11 Jun - 13:00 hrs | Estadio Azteca", "lento": "1X (México o Empate) + Menos 4.5 goles", "sprint": "Victoria México"},
            {"partido": "🇰🇷 Corea del Sur vs. 🇨🇿 Rep. Checa", "info": "11 Jun - 20:00 hrs | Estadio Akron", "lento": "Más de 0.5 goles", "sprint": "Ambos Anotan"}
        ],
        "⚽ Grupo B": [
            {"partido": "🇨🇦 Canadá vs. 🇧🇦 Bosnia y Her.", "info": "12 Jun - 15:00 hrs | Toronto", "lento": "Canadá o Empate", "sprint": "Victoria Canadá"},
            {"partido": "🇶🇦 Qatar vs. 🇨🇭 Suiza", "info": "13 Jun - 12:00 hrs | San Francisco", "lento": "Suiza gana cualquier mitad", "sprint": "Victoria Suiza"}
        ],
        "⚽ Grupo C": [
            {"partido": "🇧🇷 Brasil vs. 🇲🇦 Marruecos", "info": "13 Jun - 18:00 hrs | NY/NJ", "lento": "Más de 1.5 goles totales", "sprint": "Brasil gana + Más de 2.5 goles"},
            {"partido": "🇭🇹 Haití vs. 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia", "info": "13 Jun - 21:00 hrs | Boston", "lento": "Menos de 3.5 goles", "sprint": "Victoria Escocia"}
        ],
        "⚽ Grupo D": [
            {"partido": "🇺🇸 Estados Unidos vs. 🇵🇾 Paraguay", "info": "12 Jun - 18:00 hrs | Los Ángeles", "lento": "USA o Empate", "sprint": "Ambos Anotan"},
            {"partido": "🇦🇺 Australia vs. 🇹🇷 Turquía", "info": "13 Jun - 21:00 hrs | Vancouver", "lento": "Turquía anota (Más de 0.5)", "sprint": "Victoria Turquía"}
        ],
        "⚽ Grupo E": [
            {"partido": "🇩🇪 Alemania vs. 🇨🇼 Curazao", "info": "14 Jun - 12:00 hrs | Houston", "lento": "Victoria Alemania", "sprint": "Alemania gana ambas mitades"},
            {"partido": "🇨🇮 Costa de Marfil vs. 🇪🇨 Ecuador", "info": "14 Jun - 19:00 hrs | Philadelphia", "lento": "Más de 0.5 goles en el 2do tiempo", "sprint": "Empate al Medio Tiempo"}
        ],
        "⚽ Grupo F": [
            {"partido": "🇳🇱 Países Bajos vs. 🇯🇵 Japón", "info": "14 Jun - 15:00 hrs | Dallas", "lento": "Países Bajos o Empate", "sprint": "Ambos Anotan"},
            {"partido": "🇸🇪 Suecia vs. 🇹🇳 Túnez", "info": "14 Jun - 20:00 hrs | Monterrey", "lento": "Menos de 3.5 goles", "sprint": "Victoria Suecia"}
        ],
        "⚽ Grupo G": [
            {"partido": "🇧🇪 Bélgica vs. 🇪🇬 Egipto", "info": "15 Jun - 12:00 hrs | Seattle", "lento": "Más de 1.5 goles", "sprint": "Ambos Anotan"},
            {"partido": "🇮🇷 Irán vs. 🇳🇿 Nueva Zelanda", "info": "15 Jun - 18:00 hrs | Los Ángeles", "lento": "Menos de 2.5 goles", "sprint": "Empate"}
        ],
        "⚽ Grupo H": [
            {"partido": "🇪🇸 España vs. 🇨🇻 Cabo Verde", "info": "15 Jun - 12:00 hrs | Atlanta", "lento": "Victoria España", "sprint": "España gana a cero"},
            {"partido": "🇸🇦 Arabia Saudita vs. 🇺🇾 Uruguay", "info": "15 Jun - 18:00 hrs | Miami", "lento": "Uruguay o Empate", "sprint": "Uruguay gana + Más de 1.5 goles"}
        ],
        "⚽ Grupo I": [
            {"partido": "🇫🇷 Francia vs. 🇸🇳 Senegal", "info": "16 Jun - 15:00 hrs | NY/NJ", "lento": "Francia anota (Más de 0.5)", "sprint": "Victoria Francia"},
            {"partido": "🇮🇶 Irak vs. 🇳🇴 Noruega", "info": "16 Jun - 18:00 hrs | Boston", "lento": "Noruega o Empate", "sprint": "Victoria Noruega"}
        ],
        "⚽ Grupo J": [
            {"partido": "🇦🇷 Argentina vs. 🇩🇿 Argelia", "info": "16 Jun - 20:00 hrs | Kansas City", "lento": "Victoria Argentina", "sprint": "Argentina gana 1er Tiempo"},
            {"partido": "🇦🇹 Austria vs. 🇯🇴 Jordania", "info": "16 Jun - 21:00 hrs | San Francisco", "lento": "Más de 1.5 goles", "sprint": "Victoria Austria"}
        ],
        "⚽ Grupo K": [
            {"partido": "🇵🇹 Portugal vs. 🇨🇩 RD Congo", "info": "17 Jun - 12:00 hrs | Houston", "lento": "Portugal anota en la 1ra mitad", "sprint": "Portugal gana a cero"},
            {"partido": "🇺🇿 Uzbekistán vs. 🇨🇴 Colombia", "info": "17 Jun - 21:00 hrs | CDMX", "lento": "Colombia o Empate", "sprint": "Victoria Colombia"}
        ],
        "⚽ Grupo L": [
            {"partido": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra vs. 🇭🇷 Croacia", "info": "17 Jun - 15:00 hrs | Dallas", "lento": "Más de 1.5 goles", "sprint": "Empate"},
            {"partido": "🇬🇭 Ghana vs. 🇵🇦 Panamá", "info": "17 Jun - 19:00 hrs | Toronto", "lento": "Menos de 3.5 goles", "sprint": "Empate al Medio Tiempo"}
        ]
    }

    # Bucle que dibuja todos los partidos automáticamente
    for grupo, partidos in grupos_jornada1.items():
        # Desplegamos el Grupo A por defecto para que veas el partido del Azteca y el del Akron (ahí en la casa del Rebaño seguro pesa bastante el ambiente)
        expandido = True if grupo == "⚽ Grupo A" else False
        with st.expander(grupo, expanded=expandido):
            for p in partidos:
                st.markdown(f"**{p['partido']}** ({p['info']})")
                st.markdown(f"* 🐢 **Consejo Lento:** {p['lento']}")
                st.markdown(f"* ⚡ **Consejo Sprint:** {p['sprint']}")
                st.write("---")

# ==========================================
# PESTAÑA 2: RETO LENTO (31 DÍAS)
# ==========================================
with tab2:
    st.header("🐢 Progreso del Reto Lento")
    st.write("Meta: 31 días | Inicio: $20.00 | Cuota Objetivo: 1.25")
    
    fondo_actual = 20.0
    
    for dia in range(1, 32):
        st.markdown(f"### Día {dia}")
        col1, col2 = st.columns(2)
        
        with col1:
            completado = st.checkbox(f"✅ Dia {dia} completado", key=f"chk_lento_{dia}")
        
        if completado:
            with col2:
                fondo_actual = st.number_input(
                    f"Cobro exacto del Día {dia} ($):", 
                    value=float(fondo_actual * 1.25), 
                    step=0.5, 
                    key=f"num_lento_{dia}"
                )
            st.success(f"¡Día {dia} superado! Tienes **${fondo_actual:.2f}** para mañana.")
            st.info(f"👉 Meta proyectada para el Día {dia+1}: **${fondo_actual * 1.25:.2f}**")
        else:
            st.warning("Completa este día para desbloquear el siguiente paso.")
            break

# ==========================================
# PESTAÑA 3: RETO SPRINT (14 PASOS)
# ==========================================
with tab3:
    st.header("⚡ Progreso del Reto Sprint")
    st.write("Meta: 14 pasos | Inicio: $30.00 | Cuota Objetivo: 1.50")
    
    fondo_sprint = 30.0
    
    for paso in range(1, 15):
        st.markdown(f"### Paso {paso}")
        col1, col2 = st.columns(2)
        
        with col1:
            completado_s = st.checkbox(f"✅ Palomear Paso {paso}", key=f"chk_sprint_{paso}")
        
        if completado_s:
            with col2:
                fondo_sprint = st.number_input(
                    f"Cobro exacto del Paso {paso} ($):", 
                    value=float(fondo_sprint * 1.50), 
                    step=0.5, 
                    key=f"num_sprint_{paso}"
                )
            st.success(f"¡Paso {paso} superado! Tienes **${fondo_sprint:.2f}** para el siguiente salto.")
            st.info(f"👉 Meta proyectada para el Paso {paso+1}: **${fondo_sprint * 1.50:.2f}**")
        else:
            st.warning("Completa este paso para desbloquear el siguiente.")
            break

# ==========================================
# PESTAÑA 4: CALCULADORA INTERACTIVA
# ==========================================
with tab4:
    st.header("🧮 Calculadora de Interés Compuesto")
    st.write("Proyecta escenarios libres para tus apuestas.")
    
    col_calc1, col_calc2, col_calc3 = st.columns(3)
    with col_calc1:
        monto_ini = st.number_input("Monto Inicial ($):", min_value=1.0, max_value=10000.0, value=20.0, step=5.0)
    with col_calc2:
        cuota_prom = st.slider("Cuota Promedio:", min_value=1.01, max_value=3.00, value=1.25, step=0.01)
    with col_calc3:
        num_pasos = st.slider("Número de Pasos:", min_value=1, max_value=60, value=31, step=1)
        
    datos_proyeccion = []
    acumulado = monto_ini
    
    for i in range(1, num_pasos + 1):
        ganancia = acumulado * cuota_prom
        datos_proyeccion.append({
            "Paso / Día": f"Día {i}",
            "Monto Apostado ($)": round(acumulado, 2),
            "Cobro Potencial ($)": round(ganancia, 2)
        })
        acumulado = ganancia
        
    st.subheader(f"💰 Monto Final Proyectado: ${acumulado:,.2f}")
    
    df_proyeccion = pd.DataFrame(datos_proyeccion)
    st.dataframe(df_proyeccion, use_container_width=True)