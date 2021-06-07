# para fazer funcionar o site, tem que rodar no terminal dessa forma:
# streamlit run 'caminho do arquivo' (neste caso, C:\Users\carlo\PycharmProjects\pythonProject\venv\MarieCurie\presencasimulado.py)
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

def app():
    #OBS: colocar no papel o "esqueleto" do site
    # tem containers (horizontal) e columns (vertical)
    header = st.beta_container()
    dataset = st.beta_container()
    features = st.beta_container()
    model_training = st.beta_container()

    with header:
        st.title('Inteligência de Dados - Automação de Análises de Simulado')
        st.text('Este projeto-piloto tem como objetivo pegar a planilha de Simulado da eduqo e automaticamente já dar '
                    'como resposta uma outra planilha com login e falta em booleanos')



    with dataset:
        st.header('1. Tabela Crua da Eduqo')
        st.text('O objetivo é transformar a tabela a seguir em uma outra tabela mais simples com a presença')
        num_simulado = st.selectbox('Escolha um Simulado: ', options=['Simulado 1', 'Simulado 2'])
        dic_simulado = {
            'Simulado 1': r'C:\Users\carlo\PycharmProjects\pythonProject\venv\MarieCurie\simulado1mm.xlsx',
            'Simulado 2': r'C:\Users\carlo\PycharmProjects\pythonProject\venv\MarieCurie\simulado2mm.xlsx'
        }
        df = pd.read_excel(dic_simulado[num_simulado])

        #st.write(df.head())
        st.subheader('Distribuição das Notas')
        notas = pd.DataFrame(df['Nota geral(0 a 10)'].value_counts())
        st.bar_chart(notas)

        # OBS: dá para integrar com os gráficos do plotly

        col1 = st.sidebar.selectbox('Escolha um nome da coluna da tabela acima: ', df.columns)
        col2 = st.sidebar.selectbox('Escolha um outro nome da coluna da tabela acima: ', df.columns)
        st.write(df[[col1, col2]])
        # fig, ax = plt.plot(notas['Nota geral(0 a 10)'], notas[col])
        # st.pyplot(fig, ax)

    with features:
        st.header('2. Seção 2')
        st.markdown('* **Motivação: ** automatizar análises que realizamos na área')
        st.markdown('* **Como ela surgiu: ** biblioteca streamlit e baseada no site do Lucas    ')

    with model_training:
        st.header('3. Seção 3 - Machine Learning')
        st.text('Analisar todo histórico de presença em simulados, aulas, etc e com base nisso predizer se e alune'
                    'vai faltar o próximo simulado ou não')

        sel_col, disp_col = st.beta_columns(2)

        # criando algumas coisinhas
        numero_de_alunes = sel_col.slider('Quantes alunes você quer ver na análise?', min_value=10, max_value=60, value=20, step=10)

        tempo_de_atv = sel_col.selectbox('Quanto tempo você quer que seja o mínimo (em h)?', options=[1, 2, 3, 'Sem limites']
                                             , index=0)

        input = sel_col.text_input('Insira um(a) novo(a) aluno(a)')

