import streamlit as st


def calcular_porcentaje():
    try:
        if st.session_state['neto'] != "" and st.session_state['porcentaje'] != "":
            neto = float(st.session_state['neto'])
            porcentaje = float(st.session_state['porcentaje'])
            resultado = neto * (1+(porcentaje/100))
            resultado = round(resultado, 2)
            return resultado

    except:
        st.warning("Los valores deben ser numericos")

def calcular_descuento():
    try:
        if st.session_state['neto2'] != "" and st.session_state['descuento'] != "":
            neto = float(st.session_state['neto2'])
            porcentaje = float(st.session_state['descuento'])
            resultado = neto / (1+(porcentaje/100))
            resultado = round(resultado,2)
            return resultado

    except:
        st.warning("Los valores deben ser numericos")


colh1, colh2 = st.columns([1,4])
with colh1:
    st.image("farmacia150x190.png", width=80)
with colh2:
    st.markdown("<h1 style='text-align: left; color: grey;'>Farmacia Soriano</h1>", unsafe_allow_html=True)


st.subheader('Calculo IVA')

col1, col2, col3 = st.columns(3)
with col1:
    st.text_input(label=" Valor Neto ",
                  placeholder='Neto',
                  on_change=calcular_porcentaje,
                  key='neto')
with col2:
    st.text_input(label="Porcentaje",
                  placeholder='%',
                  on_change=calcular_porcentaje,
                  key='porcentaje')
with col3:
    st.metric(label="TOTAL ",
              value=calcular_porcentaje())

st.subheader('Calculo Descuento')

col1, col2, col3 = st.columns(3)
with col1:
    st.text_input(label=" Valor Neto ",
                  placeholder='Neto',
                  on_change=calcular_descuento,
                  key='neto2')
with col2:
    st.text_input(label="Porcentaje Descuento",
                  placeholder='%',
                  on_change=calcular_descuento(),
                  key='descuento')
with col3:
    st.metric(label="TOTAL CON DESCUENTO ",
              value=calcular_descuento())

