import streamlit as st


st.set_page_config(
    page_title='Agentes de IA',
    layout="centered",
    menu_items={
        'About' : '''teste'''
    }
       
)

st.sidebar.text('Make By Julio Santos With Streamlit.')
st.sidebar.image(
    'pictures/logo_png.png', 
    
    width=500  # Ajuste o tamanho conforme necessário
)

pag1 = st.Page(
    page= "paginas/conversa.py",
    title="Agentes",
    icon='🤖',
    default= True
)


pag2 = st.Page(
    page="paginas/teste.py",
    title='Gráficos',
    icon='📊'
)

pag3 = st.Page(
    page= "paginas\me.py",
    title="Sobre Mim",
    icon= 'ℹ'
)



pagina= st.navigation({
        "Conversação":[pag1],
        "Gráficos":[pag2],
        'Sobre Mim':[pag3]

    }
)



pagina.run()

