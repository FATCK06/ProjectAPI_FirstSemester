# ==============================================================================
# PASSO 1: Título e Imports de Sistema
# ==============================================================================
print("--- [1/7] Bibliotecas serão instaladas via Docker (requirements.txt) ---")
import os
print("Sucesso!")


# ==============================================================================
# PASSO 2: Importando as bibliotecas e configurando pastas.
# ==============================================================================
import subprocess
import time
import atexit
import socket
from flask import Flask, render_template, request, url_for
import pandas as pd
import re
import urllib.parse
import folium
import json
import geopandas as gpd
from shapely.geometry import mapping
from branca.element import Element
import unicodedata
import difflib

print("\n--- [2/7] Criando a estrutura de pastas do projeto... ---")
os.makedirs("templates", exist_ok=True)
os.makedirs("static/css", exist_ok=True)
print("Pastas 'templates' e 'static/css' prontas.")


# ==============================================================================
# PASSO 3: (ETAPA REMOVIDA - Dados são carregados apenas no Streamlit)
# ==============================================================================
print("\n--- [3/7] Configuração de dados delegada ao Streamlit... ---")
print("Sucesso (Etapa pulada intencionalmente).")


# ==============================================================================
# PASSO 4: Criando o arquivo do dashboard Streamlit
# ==============================================================================
print("\n--- [4/7] Criando o arquivo do dashboard Streamlit (app_dashboard.py)... ---")

streamlit_code = r"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re
import unicodedata

st.set_page_config(page_title="Dashboard de Dados - SJC", page_icon="📊", layout="wide")

@st.cache_data
def carregar_dados_csv(url):
    try:
        try:
            df = pd.read_csv(url, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(url, encoding='latin1')
            
        original_columns = df.columns.tolist()
        rename_map = {}
        for col in original_columns:
            new_col = col.strip().lower()
            replacements = {' ': '_', 'ç': 'c', 'ã': 'a', 'õ': 'o', 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u', '+': 'mais', '(': '', ')': ''}
            for old, new in replacements.items():
                new_col = new_col.replace(old, new)
            new_col = re.sub(r'[^a-z0-9_]', '', new_col)
            rename_map[col] = new_col
        df = df.rename(columns=rename_map)
        if 'regiao' in df.columns:
            df['regiao'] = df['regiao'].astype(str).str.strip()
            
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados de {url}: {e}")
        return pd.DataFrame()

urls_csv = {
    "idade_sexo_2022": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/RubyFox%20-%20Dados%20de%202022%20-%20Idade%20e%20sexo.csv",
    "populacao_residencia_2022": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/RubyFox%20-%20Dados%20de%202022%20-%20popula%C3%A7%C3%A3o%20e%20residencia.csv",
    "densidade_demografica_sjc_2010": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/densidade_demografica_sjc_2010.csv",
    "faixa_etaria_homens_2010": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/faixa_etaria_homens_2010.csv",
    "faixa_etaria_mulheres_2010": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/faixa_etaria_mulheres_2010.csv",
    "populacao_residente_sjc_2010": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/populacao_residente_sjc_2010.csv",
    "frota_veiculos_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/frota_veiculos_sjc.csv",
    "escolaridade_por_nivel_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/escolaridade_por_nivel_sjc.csv",
    "alfabetizacao_geral_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/alfabetizacao_geral_sjc.csv",
    "servicos_geriatricos_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/servicos_geriatricos_sjc.csv",
    "projecao_envelhecimento_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/projecao_envelhecimento_sjc.csv",
    "servicos_publicos_zonas": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/servicos_publicos_zonas.csv",
    "transito_zonas_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/transito_zonas_sjc.csv",
    "pop_cresc_zonas_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/pop_cresc_zonas_sjc.csv",
    "creches_zonas_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/creches_zonas_sjc.csv",
    "ideb_qualidade_zonas_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/ideb_qualidade_zonas_sjc.csv",
    "infraestrutura_escolas_zonas": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/infraestrutura_escolas_zonas.csv",
    "matriculas_por_periodo_zonas": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/matriculas_por_periodo_zonas.csv",
    "alfabetizacao_por_zonas_sjc": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/alfabetizacao_por_zonas_sjc.csv",
    "unidades_saude_idosos_zonas": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/unidades_saude_idosos_zonas.csv",
    "envelhecimento_por_zonas": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/Arquivos%20dados%20CSV/envelhecimento_por_zonas.csv"
}

dataframes = {name: carregar_dados_csv(url) for name, url in urls_csv.items()}

def normalizar_texto(s):
    if not isinstance(s, str): return str(s)
    s = s.lower().strip()
    s = unicodedata.normalize('NFD', s)
    s = s.encode('ascii', 'ignore').decode('utf-8')
    return s

def formatar_faixa_display(faixa):
    return faixa.replace('_', ' ').replace(' a ', '-').replace(' anos', '').replace(' ou mais', '+')

def normalizar_faixa_etaria_2010(indicador):
    indicador = str(indicador).lower()
    if 'menos de 1' in indicador or '1 a 4' in indicador: return '0 a 4 anos'
    if '5 a 9' in indicador: return '5 a 9 anos'
    if '10 a 14' in indicador: return '10 a 14 anos'
    if '15 a 19' in indicador: return '15 a 19 anos'
    if '20 a 24' in indicador: return '20 a 24 anos'
    if '25 a 29' in indicador: return '25 a 29 anos'
    if '30 a 34' in indicador: return '30 a 34 anos'
    if '35 a 39' in indicador: return '35 a 39 anos'
    if '40 a 44' in indicador: return '40 a 44 anos'
    if '45 a 49' in indicador: return '45 a 49 anos'
    if '50 a 54' in indicador: return '50 a 54 anos'
    if '55 a 59' in indicador: return '55 a 59 anos'
    if '60 a 64' in indicador: return '60 a 64 anos'
    if '65 a 69' in indicador: return '65 a 69 anos'
    if '70 a 74' in indicador: return '70 a 74 anos'
    if '75 a 79' in indicador: return '75 a 79 anos'
    if '80 a 84' in indicador: return '80 a 84 anos'
    if '85 a 89' in indicador: return '85 a 89 anos'
    if '90 a 94' in indicador: return '90 a 94 anos'
    if '95 a 99' in indicador: return '95 a 99 anos'
    if '100 anos ou mais' in indicador: return '100 anos ou mais'
    return None

def gerar_grafico_sexo(df_idade_sexo_2022, df_faixa_h_2010, df_faixa_m_2010, df_pop_2022, df_pop_res_2010):
    st.header("Análise Populacional")
    if not df_pop_2022.empty and not df_pop_res_2010.empty:
        total_correto_2022 = df_pop_2022["populacao_residente"].iloc[0]
        total_correto_2010 = df_pop_res_2010.loc[df_pop_res_2010['indicador'] == 'População residente', 'valor'].iloc[0]
        col1, col2 = st.columns([3, 1])
        with col1:
            homens_2022_raw = df_idade_sexo_2022[df_idade_sexo_2022["tipo"].str.contains("homens", na=False, case=False)]["total"].sum()
            mulheres_2022_raw = df_idade_sexo_2022[df_idade_sexo_2022["tipo"].str.contains("mulheres", na=False, case=False)]["total"].sum()
            soma_raw_2022 = homens_2022_raw + mulheres_2022_raw
            homens_2022 = (homens_2022_raw / soma_raw_2022) * total_correto_2022 if soma_raw_2022 > 0 else 0
            mulheres_2022 = (mulheres_2022_raw / soma_raw_2022) * total_correto_2022 if soma_raw_2022 > 0 else 0
            df_sexo_2022 = pd.DataFrame([{"Sexo": "Homens", "População": homens_2022, "Ano": "2022"}, {"Sexo": "Mulheres", "População": mulheres_2022, "Ano": "2022"}])
            homens_2010_raw = df_faixa_h_2010['valor'].sum()
            mulheres_2010_raw = df_faixa_m_2010['valor'].sum()
            soma_raw_2010 = homens_2010_raw + mulheres_2010_raw
            homens_2010 = (homens_2010_raw / soma_raw_2010) * total_correto_2010 if soma_raw_2010 > 0 else 0
            mulheres_2010 = (mulheres_2010_raw / soma_raw_2010) * total_correto_2010 if soma_raw_2010 > 0 else 0
            df_sexo_2010 = pd.DataFrame([{"Sexo": "Homens", "População": homens_2010, "Ano": "2010"}, {"Sexo": "Mulheres", "População": mulheres_2010, "Ano": "2010"}])
            df_sexo_final = pd.concat([df_sexo_2010, df_sexo_2022], ignore_index=True)
            df_sexo_final['Ano'] = df_sexo_final['Ano'].astype(str)
            fig1 = px.bar(df_sexo_final, x="Ano", y="População", color="Sexo", barmode="group", title="População por Sexo (2010 vs 2022)", text_auto='.3s', height=600, labels={"Ano": "Ano", "População": "População", "Sexo": "Sexo"}, color_discrete_map={'Homens': '#1f77b4', 'Mulheres': '#e377c2'})
            fig1.update_layout(xaxis_type='category')
            fig1.update_traces(textangle=0, textposition="outside")
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            st.metric("População Total 2022", f"{int(total_correto_2022):,}".replace(",", "."))
            st.metric("População Total 2010", f"{int(total_correto_2010):,}".replace(",", "."))
            if total_correto_2010 > 0:
                st.metric("Crescimento Populacional", f"{(total_correto_2022/total_correto_2010 - 1):.2%}")

def gerar_grafico_densidade(df_densidade_2010, df_pop_2022):
    st.subheader("Evolução da Densidade Demográfica")
    data_densidade = []
    if not df_densidade_2010.empty and "densidade_demografica_habkm2" in df_densidade_2010.columns:
        densidade_2010 = df_densidade_2010["densidade_demografica_habkm2"].iloc[0]
        data_densidade.append({"Ano": "2010", "Densidade (hab/km²)": densidade_2010})
    if not df_pop_2022.empty and "densidade" in df_pop_2022.columns:
        densidade_2022 = df_pop_2022["densidade"].iloc[0]
        data_densidade.append({"Ano": "2022", "Densidade (hab/km²)": densidade_2022})
    if data_densidade:
        df_densidade = pd.DataFrame(data_densidade)
        df_densidade["Densidade (hab/km²)"] = df_densidade["Densidade (hab/km²)"].astype(str).str.replace(',', '.', regex=False).astype(float)
        fig2 = px.line(df_densidade, x="Ano", y="Densidade (hab/km²)", markers=True, title="Evolução da Densidade Demográfica", height=600)
        fig2.update_traces(text=df_densidade["Densidade (hab/km²)"].round(2), textposition="top center")
        st.plotly_chart(fig2, use_container_width=True)

def gerar_piramide_etaria(df_idade_sexo_2022, df_faixa_h_2010, df_faixa_m_2010, df_pop_2022, df_pop_res_2010):
    st.subheader("Pirâmide Etária")
    ano_selecionado = st.radio("Selecione o ano para a Pirâmide Etária:", ('2022', '2010'), horizontal=True)
    if ano_selecionado == '2022':
        df_idade_sexo_2022['tipo'] = df_idade_sexo_2022['tipo'].str.strip().str.lower()
        faixas_cols = [c for c in df_idade_sexo_2022.columns if c not in ["ano", "tipo", "total", "id"]]
        df_2022_h = df_idade_sexo_2022[df_idade_sexo_2022['tipo'] == 'homens'][faixas_cols].melt(var_name='faixa_etaria', value_name='populacao_raw')
        df_2022_m = df_idade_sexo_2022[df_idade_sexo_2022['tipo'] == 'mulheres'][faixas_cols].melt(var_name='faixa_etaria', value_name='populacao_raw')
        df_2022_h['populacao'] = df_2022_h['populacao_raw']
        df_2022_m['populacao'] = df_2022_m['populacao_raw']
        y_labels = sorted(df_2022_h['faixa_etaria'].unique(), key=lambda x: int(re.search(r'\d+', x).group(0)) if re.search(r'\d+', x) else float('inf'))
        df_final_h = df_2022_h.set_index('faixa_etaria').loc[y_labels].reset_index()
        df_final_m = df_2022_m.set_index('faixa_etaria').loc[y_labels].reset_index()
    else:
        df_2010_h = df_faixa_h_2010.copy()
        df_2010_h['faixa_etaria'] = df_2010_h['indicador'].apply(normalizar_faixa_etaria_2010)
        df_2010_h = df_2010_h.groupby('faixa_etaria')['valor'].sum().reset_index()
        df_2010_h = df_2010_h.rename(columns={'valor': 'populacao_raw'})
        df_2010_m = df_faixa_m_2010.copy()
        df_2010_m['faixa_etaria'] = df_2010_m['indicador'].apply(normalizar_faixa_etaria_2010)
        df_2010_m = df_2010_m.groupby('faixa_etaria')['valor'].sum().reset_index()
        df_2010_m = df_2010_m.rename(columns={'valor': 'populacao_raw'})
        df_2010_h['populacao'] = df_2010_h['populacao_raw']
        df_2010_m['populacao'] = df_2010_m['populacao_raw']
        y_labels = sorted(df_2010_h['faixa_etaria'].dropna().unique(), key=lambda x: int(re.search(r'\d+', x).group(0)) if re.search(r'\d+', x) else float('inf'))
        df_final_h = df_2010_h.set_index('faixa_etaria').loc[y_labels].reset_index()
        df_final_m = df_2010_m.set_index('faixa_etaria').loc[y_labels].reset_index()
    y_display = [formatar_faixa_display(y) for y in y_labels]
    fig = go.Figure()
    fig.add_trace(go.Bar(y=y_display, x=df_final_h['populacao'] * -1, customdata=df_final_h['populacao'], name='Homens', orientation='h', marker_color='#1f77b4', hovertemplate='População: %{customdata:,.0f}<extra></extra>'))
    fig.add_trace(go.Bar(y=y_display, x=df_final_m['populacao'], customdata=df_final_m['populacao'], name='Mulheres', orientation='h', marker_color='#e377c2', hovertemplate='População: %{customdata:,.0f}<extra></extra>'))
    fig.update_layout(title=f'Pirâmide Etária - {ano_selecionado}', height=800, yaxis_title='Faixa Etária', xaxis_title='População', barmode='overlay', bargap=0.1, xaxis=dict(tickmode='array', tickvals=[-50000, -25000, 0, 25000, 50000], ticktext=['50k', '25k', '0', '25k', '50k']))
    st.plotly_chart(fig, use_container_width=True)

def gerar_grafico_populacao_residente(df_pop_2022, df_pop_res_2010, df_cresc):
    st.header("Análise da População Residente")
    if not df_pop_2022.empty and not df_pop_res_2010.empty:
        total_2022 = df_pop_2022["populacao_residente"].iloc[0]
        total_2010 = df_pop_res_2010.loc[df_pop_res_2010['indicador'] == 'População residente', 'valor'].iloc[0]
        data_pop = pd.DataFrame([{"Ano": "2010", "População": total_2010}, {"Ano": "2022", "População": total_2022}])
        col1, col2 = st.columns([3, 1])
        with col1:
            fig = px.bar(data_pop, y="Ano", x="População", orientation='h', title="População Residente Total (2010 vs 2022)", text_auto=True, color="Ano", color_discrete_sequence=["#1f77b4", "#ff7f0e"], height=300)
            fig.update_yaxes(type='category')
            fig.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
            fig.update_traces(textposition='outside')
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.metric("População 2022", f"{int(total_2022):,}".replace(",", "."))
            st.metric("População 2010", f"{int(total_2010):,}".replace(",", "."))
            if total_2010 > 0:
                crescimento = (total_2022 / total_2010 - 1)
                st.metric("Crescimento Total", f"{crescimento:.2%}")
    else:
        st.warning("Não foi possível carregar os dados de população residente.")
    st.subheader("Crescimento Populacional por Zona (2010-2022)")
    if not df_cresc.empty:
        df_cresc_sorted = df_cresc.sort_values(by='crescimento_percentual', ascending=False)
        fig_cresc = px.bar(df_cresc_sorted, x='regiao', y='crescimento_percentual', title='Variação Percentual da População por Zona', text_auto='.2f', labels={'regiao': 'Região', 'crescimento_percentual': 'Crescimento (%)'})
        fig_cresc.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
        fig_cresc.update_layout(height=500)
        st.plotly_chart(fig_cresc, use_container_width=True)
    else:
        st.warning("Dados de crescimento por zona não disponíveis.")

def gerar_grafico_transito_frota(df_frota, df_transito):
    st.header("Análise de Trânsito por Região e Evolução da Frota")
    st.subheader("Evolução da Frota Total de Veículos e Métricas Anuais")
    if df_frota.empty or 'ano' not in df_frota.columns or 'frota_total' not in df_frota.columns:
        st.warning("Dados de frota de veículos não carregados ou colunas essenciais ausentes.")
    else:
        df_frota_clean = df_frota[df_frota['frota_total'] > 0].copy()
        df_frota_clean['frota_total'] = pd.to_numeric(df_frota_clean['frota_total'], errors='coerce')
        df_frota_clean = df_frota_clean.dropna(subset=['frota_total', 'veiculos_por_habitante', 'motocicletas_percentual'])
        fig_frota = px.line(df_frota_clean, x='ano', y='frota_total', title='Frota Total de Veículos (1997-2024)', markers=True, height=550, labels={'frota_total': 'Frota Total', 'ano': 'Ano'})
        fig_frota.update_traces(text=df_frota_clean['frota_total'].apply(lambda x: f'{x:,.0f}'.replace(',', '.')), textposition="top center")
        fig_frota.update_layout(xaxis_type='category')
        st.plotly_chart(fig_frota, use_container_width=True)
        st.markdown("#### Detalhes Anuais da Frota")
        df_display = df_frota_clean[['ano', 'veiculos_por_habitante', 'motocicletas_percentual', 'observacoes']].copy()
        df_display.rename(columns={'veiculos_por_habitante': 'Veículos/Hab', 'motocicletas_percentual': 'Motocicletas (%)', 'observacoes': 'Observações'}, inplace=True)
        st.dataframe(df_display, hide_index=True, use_container_width=True)
    st.subheader("Trânsito e Infraestrutura Viária por Região")
    if df_transito.empty or 'regiao' not in df_transito.columns:
        st.warning("Dados de trânsito por zona não carregados.")
        return
    df_congestionamento = df_transito.copy()
    ordem_congestionamento = {'Baixo': 1, 'Baixo-Medio': 2, 'Medio': 3, 'Medio-Alto': 4, 'Alto': 5, 'Muito Alto': 6}
    df_congestionamento['ordem'] = df_congestionamento['nivel_congestionamento'].map(ordem_congestionamento)
    df_congestionamento = df_congestionamento.sort_values(by='ordem', ascending=False)
    cores = {'Baixo': 'rgb(140, 240, 140)', 'Baixo-Medio': 'rgb(255, 255, 102)', 'Medio': 'rgb(255, 165, 0)', 'Medio-Alto': 'rgb(255, 120, 0)', 'Alto': 'rgb(255, 60, 0)', 'Muito Alto': 'rgb(255, 0, 0)'}
    fig_congestionamento = px.bar(df_congestionamento, y='regiao', x='ordem', color='nivel_congestionamento', orientation='h', title='Nível de Congestionamento por Região', height=550, labels={'regiao': 'Região', 'ordem': 'Nível de Congestionamento'}, color_discrete_map=cores)
    fig_congestionamento.update_layout(xaxis=dict(tickmode='array', tickvals=list(ordem_congestionamento.values()), ticktext=list(ordem_congestionamento.keys())), showlegend=True, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_congestionamento, use_container_width=True)
    st.markdown("#### Detalhes Qualitativos do Trânsito por Região")
    df_textual = df_transito.copy()
    df_textual.rename(columns={'regiao': 'Região', 'caracteristicas_transito': 'Características', 'problemas_principais': 'Problemas Principais', 'infraestrutura_viaria': 'Infraestrutura Viária', 'nivel_congestionamento': 'Congestionamento'}, inplace=True)
    st.dataframe(df_textual, hide_index=True, use_container_width=True)

def gerar_grafico_servicos(df_servicos):
    st.header("Serviços Públicos por Zona da Cidade")
    if df_servicos.empty or 'regiao' not in df_servicos.columns:
        st.warning("Dados de serviços públicos não carregados ou coluna 'regiao' ausente.")
        return
    df_clean = df_servicos[df_servicos['regiao'].str.lower() != 'total_municipio'].copy()

    colunas_saude = ['ubs_unidades_basicas_saude', 'hospitais', 'upa_pronto_atendimento']
    colunas_educacao = ['escolas_municipais', 'escolas_estaduais']

    st.subheader("Nível de Serviço, Renda Média e Percentual de Empregos por Região")
    if all(c in df_clean.columns for c in ['regiao', 'nivel_atendimento', 'renda_media', 'empregos_percentual']):
        df_detalhes = df_clean[['regiao', 'nivel_atendimento', 'renda_media', 'empregos_percentual']].copy()
        df_detalhes.rename(columns={'regiao': 'Região', 'nivel_atendimento': 'Nível de Atendimento', 'renda_media': 'Renda Média', 'empregos_percentual': 'Empregos (%)'}, inplace=True)
        df_detalhes['Empregos (%)'] = df_detalhes['Empregos (%)'].round(1).astype(str) + '%'
        st.dataframe(df_detalhes, hide_index=True, use_container_width=True)

    if all(c in df_clean.columns for c in colunas_saude):
        df_clean['total_saude'] = df_clean[colunas_saude].sum(axis=1)
        st.subheader("Total de Unidades de Saúde por Zona")
        fig_saude = px.bar(df_clean, x='regiao', y='total_saude', title='Total de UBS, Hospitais e UPA por Zona', height=550, labels={'regiao': 'Zona da Cidade', 'total_saude': 'Total de Unidades de Saúde'}, color_discrete_sequence=['#ff9933'])
        fig_saude.update_traces(text=df_clean['total_saude'], textposition='outside')
        st.plotly_chart(fig_saude, use_container_width=True)
    else:
        st.warning("Uma ou mais colunas de dados de saúde (ubs_unidades_basicas_saude, hospitais, upa_pronto_atendimento) não foram encontradas.")

    if 'empregos_percentual' in df_clean.columns:
        st.subheader("Distribuição Percentual de Empregos por Zona")
        df_clean_emprego = df_clean.sort_values(by='empregos_percentual', ascending=False)
        fig_empregos = px.bar(df_clean_emprego, x='regiao', y='empregos_percentual', title='Distribuição Percentual de Empregos', height=550, labels={'regiao': 'Zona da Cidade', 'empregos_percentual': 'Empregos (%)'}, color='empregos_percentual', color_continuous_scale=px.colors.sequential.Bluyl)
        fig_empregos.update_traces(text=df_clean_emprego['empregos_percentual'].round(1).astype(str) + '%', textposition='outside')
        fig_empregos.update_layout(xaxis_type='category', coloraxis_showscale=False)
        st.plotly_chart(fig_empregos, use_container_width=True)

    if all(c in df_clean.columns for c in colunas_educacao):
        st.subheader("Comparativo de Escolas Municipais vs. Estaduais")
        df_educacao = df_clean.melt(id_vars='regiao', value_vars=colunas_educacao, var_name='Tipo de Escola', value_name='Quantidade')
        df_educacao['Tipo de Escola'] = df_educacao['Tipo de Escola'].replace({'escolas_municipais': 'Municipais', 'escolas_estaduais': 'Estaduais'})
        fig_educacao = px.bar(df_educacao, x='regiao', y='Quantidade', color='Tipo de Escola', title='Escolas Municipais vs. Estaduais por Zona', barmode='group', height=550, labels={'regiao': 'Zona da Cidade', 'Quantidade': 'Número de Escolas'})
        fig_educacao.update_layout(xaxis_type='category')
        st.plotly_chart(fig_educacao, use_container_width=True)

def gerar_grafico_alfabetizacao(df_geral, df_zonas, df_ideb, df_matriculas, df_escolaridade, df_creches):
    st.header("Análise da Educação e Alfabetização")

    st.subheader("Taxa de Alfabetização Geral (15+ anos)")
    if not df_geral.empty:
        df_geral['indicador'] = df_geral['indicador'].str.lower()
        df_geral_melted = df_geral.melt(id_vars='indicador', value_vars=['valor_2010', 'valor_2022'], var_name='ano', value_name='valor')
        df_geral_melted = df_geral_melted[df_geral_melted['indicador'] == 'taxa_alfabetizacao_15mais']
        df_geral_melted['ano'] = df_geral_melted['ano'].replace({'valor_2010': '2010', 'valor_2022': '2022'})
        df_geral_melted = df_geral_melted.sort_values(by='ano', ascending=False)
        fig_taxa = px.bar(df_geral_melted, y='ano', x='valor', orientation='h', text_auto=True, title="Comparativo da Taxa de Alfabetização", labels={'ano': 'Ano', 'valor': 'Taxa (%)'}, height=350, color='ano', color_discrete_sequence=["#008080", "#FFC300"])
        fig_taxa.update_traces(texttemplate='%{x:.2f}%', textposition='outside')
        fig_taxa.update_layout(yaxis={'categoryorder':'array', 'categoryarray': ['2010', '2022']}, showlegend=False)
        st.plotly_chart(fig_taxa, use_container_width=True)

    st.subheader("Taxa de Alfabetização por Zona (2010)")
    if not df_zonas.empty:
        fig_zonas = px.bar(df_zonas.sort_values('taxa_alfabetizacao_estimada', ascending=True), y='regiao', x='taxa_alfabetizacao_estimada', orientation='h', title="Alfabetização por Zona", text_auto=True, labels={'regiao':'Região', 'taxa_alfabetizacao_estimada':'Taxa de Alfabetização Estimada (%)'}, height=600, color='taxa_alfabetizacao_estimada', color_continuous_scale=px.colors.sequential.Teal)
        fig_zonas.update_traces(texttemplate='%{x:.2f}%', textposition='outside')
        fig_zonas.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_zonas, use_container_width=True)

    st.subheader("Índice de Desenvolvimento da Educação Básica (IDEB) - 2021")
    if not df_ideb.empty:
        df_ideb_filtered = df_ideb[~df_ideb['regiao'].isin(['media_municipal', 'meta_ideb_2024', 'comparacao_nacional'])]
        df_ideb_melt = df_ideb_filtered.melt(id_vars='regiao', value_vars=['ideb_anos_iniciais_estimado', 'ideb_anos_finais_estimado'], var_name='Nível', value_name='IDEB')
        df_ideb_melt['Nível'] = df_ideb_melt['Nível'].replace({'ideb_anos_iniciais_estimado': 'Anos Iniciais', 'ideb_anos_finais_estimado': 'Anos Finais'})
        fig_ideb = px.bar(df_ideb_melt, x='regiao', y='IDEB', color='Nível', barmode='group', text_auto=True, title="IDEB por Região")
        st.plotly_chart(fig_ideb, use_container_width=True)

    st.subheader("Taxas de Aprovação e Reprovação por Zona (2021)")
    if not df_ideb.empty:
        df_taxas_filtered = df_ideb[~df_ideb['regiao'].isin(['media_municipal', 'meta_ideb_2024', 'comparacao_nacional'])]
        df_taxas_melt = df_taxas_filtered.melt(id_vars='regiao', value_vars=['taxa_aprovacao', 'taxa_reprovacao'], var_name='Tipo de Taxa', value_name='Percentual')
        df_taxas_melt['Tipo de Taxa'] = df_taxas_melt['Tipo de Taxa'].replace({'taxa_aprovacao': 'Aprovação', 'taxa_reprovacao': 'Reprovação'})

        fig_taxas = px.bar(df_taxas_melt,
                            x='regiao',
                            y='Percentual',
                            color='Tipo de Taxa',
                            barmode='group',
                            text_auto=True,
                            title="Aprovação vs. Reprovação por Região",
                            labels={'regiao': 'Região', 'Percentual': 'Taxa (%)'},
                            color_discrete_map={'Aprovação': '#2ca02c', 'Reprovação': '#d62728'})
        fig_taxas.update_traces(texttemplate='%{y:.1f}%', textposition='outside')
        st.plotly_chart(fig_taxas, use_container_width=True)

    st.subheader("Nível de Escolaridade da População (2010)")
    if not df_escolaridade.empty:
        df_escolaridade_filtered = df_escolaridade[df_escolaridade['nivel_instrucao'] != 'idhm_educacao'].copy()
        df_escolaridade_filtered['quantidade_pessoas'] = (df_escolaridade_filtered['percentual_2010_estimado'] * 629921 / 100).astype(int)

        label_map = {
            'sem_instrucao': 'Sem Instrução', 'fundamental_incompleto': 'Fundamental Incompleto',
            'fundamental_completo': 'Fundamental Completo', 'medio_incompleto': 'Médio Incompleto',
            'medio_completo': 'Médio Completo', 'superior_incompleto': 'Superior Incompleto',
            'superior_completo': 'Superior Completo'
        }
        df_escolaridade_filtered['nivel_instrucao'] = df_escolaridade_filtered['nivel_instrucao'].replace(label_map)

        fig_esc = px.funnel(df_escolaridade_filtered, x='quantidade_pessoas', y='nivel_instrucao', title='Distribuição da População por Nível de Escolaridade', height=700)
        fig_esc.update_traces(textinfo="value+percent total", textfont_size=14)
        st.plotly_chart(fig_esc, use_container_width=True)

    st.subheader("Distribuição de Matrículas por Nível de Ensino")
    if not df_matriculas.empty:
        df_mat = df_matriculas.melt(id_vars='regiao', value_vars=['educacao_infantil_0a5', 'ensino_fundamental_6a14', 'ensino_medio_15a17'], var_name='Nível', value_name='Matrículas')
        df_mat['Nível'] = df_mat['Nível'].replace({'educacao_infantil_0a5':'Infantil (0-5)', 'ensino_fundamental_6a14':'Fundamental (6-14)', 'ensino_medio_15a17':'Médio (15-17)'})
        fig_mat = px.bar(df_mat, x='regiao', y='Matrículas', color='Nível', title="Matrículas por Nível e Região", barmode='stack')
        st.plotly_chart(fig_mat, use_container_width=True)

    st.subheader("Infraestrutura de Creches por Zona")
    if not df_creches.empty:
        st.dataframe(df_creches.rename(columns={'regiao': 'Região', 'unidades_educacao_infantil': 'Unidades', 'tipo_unidades': 'Tipo', 'demanda_atual': 'Demanda', 'necessidade_expansao': 'Necessidade de Expansão', 'observacoes': 'Observações'}), use_container_width=True, hide_index=True)

def gerar_grafico_envelhecimento(df_projecao, df_zonas, df_unidades, df_servicos):
    st.header("Análise do Envelhecimento Populacional")

    st.subheader("Crescimento da População Idosa (65+ anos)")
    if not df_projecao.empty and 'idosos_65mais_absoluto' in df_projecao.columns:
        df_projecao_grafico = df_projecao[df_projecao['ano'] != 'tendencia'].copy()

        fig_proj = px.line(df_projecao_grafico, x='ano', y='idosos_65mais_absoluto',
                            title="Crescimento da População Idosa em SJC", markers=True,
                            text='idosos_65mais_absoluto',
                            labels={'idosos_65mais_absoluto': 'População 65+ anos', 'ano': 'Ano'})
        fig_proj.update_traces(textposition="top center")
        fig_proj.update_layout(xaxis_type='category')
        st.plotly_chart(fig_proj, use_container_width=True)

    st.subheader("Percentual da População Idosa por Zona")
    if not df_zonas.empty and 'percentual_idosos_estimado' in df_zonas.columns:
        df_zonas_sorted = df_zonas.sort_values(by='percentual_idosos_estimado', ascending=False)
        fig_zonas = px.bar(df_zonas_sorted, x='regiao', y='percentual_idosos_estimado', title='Distribuição da População Idosa por Zona', color='regiao', text_auto=True, labels={'regiao': 'Região', 'percentual_idosos_estimado': 'Percentual de Idosos (%)'}, height=700)
        fig_zonas.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
        st.plotly_chart(fig_zonas, use_container_width=True)

    st.subheader("Unidades de Saúde com Foco em Idosos por Zona")
    if not df_unidades.empty and 'ubs_existentes' in df_unidades.columns and 'regiao' in df_unidades.columns:
        fig_unidades = px.bar(df_unidades, x='regiao', y='ubs_existentes', title="UBS Existentes por Região", text_auto=True, labels={'regiao':'Região', 'ubs_existentes':'Quantidade de UBS'})
        st.plotly_chart(fig_unidades, use_container_width=True)

    st.subheader("Serviços Geriátricos e de Apoio ao Idoso")
    if not df_servicos.empty:
        st.dataframe(df_servicos.rename(columns={'tipo_servico':'Tipo de Serviço', 'quantidade':'Quantidade', 'regiao_localizacao': 'Região/Localização', 'capacidade_atendimento': 'Capacidade', 'cobertura_estimada_idosos': 'Cobertura Estimada'}), use_container_width=True, hide_index=True)
def gerar_dashboard_zona(zona, dfs):
    st.title(f"Perfil Detalhado: {zona}")
    zona_clean = normalizar_texto(zona).replace('zona ', '').strip()
    DE_PARA_ZONAS = {
        'central': 'centro',
        'centro': 'centro',
        'sul': 'sul',
        'norte': 'norte',
        'leste': 'leste',
        'oeste': 'oeste',
        'sudeste': 'sudeste'
    }
    termo_busca = DE_PARA_ZONAS.get(zona_clean, zona_clean)
    st.write(f"Visualizando dados para a região: **{termo_busca.capitalize()}**")
    def filtrar_zona(df, nome_df):
        if df.empty: return pd.DataFrame()

        col_regiao = next((c for c in df.columns if 'regiao' in c.lower()), None)
        if not col_regiao: return pd.DataFrame()

        df['temp_search'] = df[col_regiao].astype(str).apply(normalizar_texto)

        df_filt = df[df['temp_search'] == termo_busca].copy()
        
        return df_filt.drop(columns=['temp_search'])

    st.header("1. Serviços Públicos")
    df_serv = filtrar_zona(dfs['servicos_publicos_zonas'], 'servicos_publicos_zonas')
    if not df_serv.empty:
        cols = st.columns(3)
        cols[0].metric("UBS", df_serv['ubs_unidades_basicas_saude'].values[0] if 'ubs_unidades_basicas_saude' in df_serv else '-')
        cols[1].metric("Hospitais", df_serv['hospitais'].values[0] if 'hospitais' in df_serv else '-')
        cols[2].metric("Escolas Municipais", df_serv['escolas_municipais'].values[0] if 'escolas_municipais' in df_serv else '-')
        st.dataframe(df_serv.set_index('regiao').T, use_container_width=True)
    else:
        st.info(f"Dados de serviços não encontrados para {zona}")

    st.header("2. Trânsito e Mobilidade")
    df_trans = filtrar_zona(dfs['transito_zonas_sjc'], 'transito_zonas_sjc')
    if not df_trans.empty:
        c1, c2 = st.columns(2)
        c1.metric("Nível de Congestionamento", df_trans['nivel_congestionamento'].values[0])
        st.write(f"**Características:** {df_trans['caracteristicas_transito'].values[0]}")
        st.write(f"**Problemas Principais:** {df_trans['problemas_principais'].values[0]}")
    else:
        st.info("Dados de trânsito não encontrados.")

    st.header("3. Crescimento Populacional")
    df_pop = filtrar_zona(dfs['pop_cresc_zonas_sjc'], 'pop_cresc_zonas_sjc')
    if not df_pop.empty:
        col1, col2 = st.columns(2)
        col1.metric("Crescimento Absoluto (2010-2022)", f"+{df_pop['crescimento_absoluto'].values[0]}")
        col2.metric("Crescimento Percentual", f"{df_pop['crescimento_percentual'].values[0]}%")
    else:
        st.info("Dados de crescimento populacional não encontrados.")

    st.header("4. Educação")
    col_edu1, col_edu2 = st.columns(2)
    
    with col_edu1:
        st.subheader("Creches")
        df_creche = filtrar_zona(dfs['creches_zonas_sjc'], 'creches_zonas_sjc')
        if not df_creche.empty:
            st.metric("Unidades", df_creche['unidades_educacao_infantil'].values[0])
            st.write(f"**Situação:** {df_creche['demanda_atual'].values[0]}")
            st.write(f"**Necessidade de Expansão:** {df_creche['necessidade_expansao'].values[0]}")
        else:
            st.info("Dados de creches não encontrados.")
    
    with col_edu2:
        st.subheader("Qualidade (IDEB)")
        df_ideb = filtrar_zona(dfs['ideb_qualidade_zonas_sjc'], 'ideb_qualidade_zonas_sjc')
        if not df_ideb.empty:
            c1, c2 = st.columns(2)
            c1.metric("Anos Iniciais", df_ideb['ideb_anos_iniciais_estimado'].values[0])
            c2.metric("Anos Finais", df_ideb['ideb_anos_finais_estimado'].values[0])
            st.write(f"**Infraestrutura:** {df_ideb['qualidade_infraestrutura'].values[0]}")
        else:
            st.info("Dados do IDEB não encontrados.")

    st.header("5. Saúde do Idoso")
    df_idoso = filtrar_zona(dfs['unidades_saude_idosos_zonas'], 'unidades_saude_idosos_zonas')
    if not df_idoso.empty:
        c1, c2, c3 = st.columns(3)
        c1.metric("População 65+", df_idoso['idosos_65mais_estimativa'].values[0])
        c2.metric("UBS Existentes", df_idoso['ubs_existentes'].values[0])
        c3.metric("Casa do Idoso", df_idoso['casa_do_idoso'].values[0])
        st.write(f"**Prioridade de Investimento:** {df_idoso['prioridade_investimento'].values[0]}")
    else:
        st.info("Dados de saúde do idoso não encontrados.")


params = st.query_params
zona_param = params.get("zona", None)

if zona_param:

    if isinstance(zona_param, list): zona_param = zona_param[0]
    gerar_dashboard_zona(zona_param, dataframes)
else:

    graph_id = int(params.get("grafico_id", [1])[0])
    
    if graph_id == 1:
        gerar_grafico_sexo(dataframes["idade_sexo_2022"], dataframes["faixa_etaria_homens_2010"], dataframes["faixa_etaria_mulheres_2010"], dataframes["populacao_residencia_2022"], dataframes["populacao_residente_sjc_2010"])
    elif graph_id == 2:
        gerar_grafico_densidade(dataframes["densidade_demografica_sjc_2010"], dataframes["populacao_residencia_2022"])
    elif graph_id == 3:
        gerar_piramide_etaria(dataframes["idade_sexo_2022"], dataframes["faixa_etaria_homens_2010"], dataframes["faixa_etaria_mulheres_2010"], dataframes["populacao_residencia_2022"], dataframes["populacao_residente_sjc_2010"])
    elif graph_id == 4:
        gerar_grafico_populacao_residente(dataframes["populacao_residencia_2022"], dataframes["populacao_residente_sjc_2010"], dataframes["pop_cresc_zonas_sjc"])
    elif graph_id == 5:
        gerar_grafico_transito_frota(dataframes["frota_veiculos_sjc"], dataframes["transito_zonas_sjc"])
    elif graph_id == 6:
        gerar_grafico_servicos(dataframes["servicos_publicos_zonas"])
    elif graph_id == 7:
        gerar_grafico_alfabetizacao(dataframes["alfabetizacao_geral_sjc"], dataframes["alfabetizacao_por_zonas_sjc"], dataframes["ideb_qualidade_zonas_sjc"], dataframes["matriculas_por_periodo_zonas"], dataframes["escolaridade_por_nivel_sjc"], dataframes["creches_zonas_sjc"])
    elif graph_id == 8:
        gerar_grafico_envelhecimento(dataframes["projecao_envelhecimento_sjc"], dataframes["envelhecimento_por_zonas"], dataframes["unidades_saude_idosos_zonas"], dataframes["servicos_geriatricos_sjc"])
    else:
        st.error("Gráfico não encontrado.")
"""
STREAMLIT_APP_FILE = "app_dashboard.py"
with open(STREAMLIT_APP_FILE, "w", encoding="utf-8") as f:
    f.write(streamlit_code)
print(f"Arquivo '{STREAMLIT_APP_FILE}' criado com sucesso.")


# ==============================================================================
# PASSO 5: Cria os arquivos do site para o Flask
# ==============================================================================
print("\n--- [5/7] Criando os arquivos HTML e CSS para o portal Flask... ---")
graficos_info = {
    1: {"titulo": "População por Sexo", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_sex.jpg"},
    2: {"titulo": "Densidade Demográfica", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_dens_demo.jpg"},
    3: {"titulo": "Faixa Etária", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_faix_etar.jpg"},
    4: {"titulo": "População Residente", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_resid.jpg"},
    5: {"titulo": "Trânsito por Região", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_trans_regiao.jpg"},
    6: {"titulo": "Serviços por Região", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_serv_regiao.jpg"},
    7: {"titulo": "Alfabetização", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_alfa.jpg"},
    8: {"titulo": "Envelhecimento", "imagem": "https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/img_enve.jpg"}
}
layout_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} | Prefeitura São José dos Campos</title>
    <link rel="icon" type="image/x-icon" href="https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/logo/icon.ico">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header class="contention-header">
        <div class="header">
            <div>
                <picture class="logo">
                    <a href="{{ url_for('home') }}"><img src="https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/logo/brasao_de_armas.svg" alt="Brasão de armas da Prefeitura de São José dos Campos"></a>
                </picture>
                <h1>
                    <span class="line-1">Prefeitura de </span>
                    <span class="line-2">São José dos Campos</span>
                </h1>
            </div>
            <nav>
                <ul>
                    <li><a href="{{ url_for('home') }}"><p>Início</p></a></li>
                    <li><a href="{{ url_for('home') }}#graficos"><p>Gráficos</p></a></li>
                    <li><a href="{{ url_for('home') }}#mapa"><p>Mapa</p></a></li>
                </ul>
            </nav>
        </div>
        <div class="header-mobile">
            <nav>
                <ul>
                    <li>
                        <a href="{{ url_for('home') }}"><picture><img src="https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/icons/home.svg" alt="Início"></picture></a>
                        <p>Início</p>
                    </li>
                    <li>
                        <a href="{{ url_for('home') }}#graficos"><picture><img src="https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/icons/graphic.svg" alt="Gráficos"></picture></a>
                        <p>Gráficos</p>
                    </li>
                    <li>
                        <a href="{{ url_for('home') }}#mapa"><picture><img src="https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/icons/maps.svg" alt="Mapas"></picture></a>
                        <p>Mapas</p>
                    </li>
                    <li>
                        <a href="#"><picture><img src="https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/icons/transparence.svg" alt="Ajuda"></picture></a>
                        <p>Ajuda</p>
                    </li>
                </ul>
            </nav>
        </div>
    </header>
    {% block content %}{% endblock %}
    <footer class="contention-footer">
        <div class="footer">
            <div>
                <picture class="logo">
                    <a href="{{ url_for('home') }}"><img src="https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/logo/brasao_de_armas.svg" alt="Brasão de armas da Prefeitura de São José dos Campos"></a>
                </picture>
                <h1>
                    <span class="line-1">Prefeitura de </span>
                    <span class="line-2">São José dos Campos</span>
                </h1>
            </div>
        </div>
    </footer>
</body>
</html>
"""
with open("templates/layout.html", "w", encoding="utf-8") as f:
    f.write(layout_html)

index_html = """
{% extends "layout.html" %}
{% block content %}
    <div class="banner"></div>
    <main id="graficos">
        <h1>Resumo dos gráficos</h1>
        <nav>
            <ul class="contention">
                {% for id, info in graficos.items() %}
                    <li>
                        <a href="{{ url_for('pagina_grafico', grafico_id=id) }}">
                            <img src="{{ info.imagem }}" alt="Imagem do gráfico sobre {{ info.titulo }}">
                            <h2>{{ info.titulo }}</h2>
                        </a>
                    </li>
                {% endfor %}
            </ul>
        </nav>
    </main>
    <section id="mapa">
        <h1>Mapa interativo</h1>
        <div class="mapa-container" style="width: 95%; max-width: 1300px; height: 650px; margin: 0 auto; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <iframe src="{{ url_for('pagina_mapa') }}" width="100%" height="100%" style="border:none;" title="Mapa Interativo de São José dos Campos">
                Carregando mapa...
            </iframe>
        </div>
    </section>
{% endblock %}
"""
with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

grafico_html = """
{% extends "layout.html" %}
{% block content %}
    <main>
        <div class="titulo-container">
            <h1>
                Dashboard: {{ title }}
                <span class="titulo-sublinhado"></span>
            </h1>
        </div>
        <div class="content-container">
            <p>Explore os dados de São José dos Campos no gráfico interativo abaixo.
            <br>
            <strong style="color: #EC6608;">Nota:</strong> Pode ser necessário clicar em "Visit Site" para carregar o dashboard.
            </p>
            <div id="loader-container" class="loader-container">
                <div class="loader"></div>
                <p class="loader-text">Carregando dashboard, por favor aguarde...</p>
            </div>
            <iframe id="streamlit-iframe" width="100%" height="3000" style="border:none; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); visibility: hidden;"></iframe>
        </div>
    </main>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const iframe = document.getElementById('streamlit-iframe');
            const loader = document.getElementById('loader-container');
            const streamlitUrl = "{{ streamlit_public_url }}";
            
            // Pega a Zona da URL se existir (injetada pelo Flask)
            const zonaParam = "{{ zona|default('', true) }}";
            const graficoId = "{{ grafico_id|default('', true) }}";
            
            iframe.onload = function() {
                loader.style.display = 'none';
                iframe.style.visibility = 'visible';
            };
            iframe.onerror = function() {
                loader.innerHTML = '<p class="loader-text" style="color: red;">Erro ao carregar o dashboard.</p>';
            }
            
            // Monta a URL correta pro Streamlit
            let finalSrc = streamlitUrl;
            if (zonaParam) {
                finalSrc += "?zona=" + encodeURIComponent(zonaParam);
            } else if (graficoId) {
                finalSrc += "?grafico_id=" + graficoId;
            }
            
            iframe.src = finalSrc;
        });
    </script>
{% endblock %}
"""
with open("templates/grafico.html", "w", encoding="utf-8") as f:
    f.write(grafico_html)
css_content = """
* { padding: 0; margin: 0; border: none; box-sizing: border-box; }
html { scroll-behavior: smooth; }
.contention { max-width: 1300px; margin: 0 auto; padding-left: 24px; padding-right: 24px; }
.contention-header, .contention-footer { margin: 0 auto; }
img { max-width: 100%; display: block; }
:root { --color-base-0: #fff; --color-support-blue: #0654A5; --color-support-yellow: #FFBF00; }
body { font-family: Arial, Helvetica, sans-serif; }
ul { list-style: none; }
a { text-decoration: none; }
h1 { font-size: 28px; font-weight: 700; line-height: 1.1; color: #000; }
p { font-size: 16px; font-weight: 400; line-height: 1.1; color: #000; }
.header { padding: 20px 40px; display: flex; align-items: center; justify-content: space-between; background-color: var(--color-base-0); border-bottom: 8px solid var(--color-support-yellow); }
.header div { display: flex; align-items: center; gap: 20px; }
.header h1 { font-size: 22px; }
.header div .line-1, .header div .line-2 { display: block; }
.logo a img { max-width: 60px; height: auto; }
.header nav ul { display: flex; align-items: center; gap: 15px; }
.header nav a { color: #000; font-size: 20px; }
.header-mobile { display: none; }
.footer { margin-top: 120px; padding: 40px; display: flex; align-items: center; justify-content: left; text-align: center; background-color: var(--color-support-blue); }
.footer h1 { color: var(--color-base-0); }
.footer div { display: flex; align-items: center; gap: 20px; }
.banner { width: 100%; height: 600px; background: url("https://cdn.jsdelivr.net/gh/FATCK06/ProjectAPI_FirstSemester@main/.misc/img_template/img_html/banner/banner.jpg") no-repeat center center/cover; }
main, section { padding: 40px 0; display: grid; justify-items: center; }
main h1, section h1, .titulo-container h1 { text-align: center; max-width: 20ch; padding-bottom: 40px; position: relative; display: inline-block; }
main h1::after, section h1::after, .titulo-sublinhado { content: ''; position: absolute; left: 50%; transform: translateX(-50%); bottom: 30px; width: 120%; height: 4px; background-color: var(--color-support-yellow); }
main nav ul { display: grid; grid-template-columns: repeat(4, 1fr); gap: 25px; }
main nav ul li a { display: block; position: relative; overflow: hidden; border-radius: 16px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
main nav ul li a img { width: 100%; height: 300px; object-fit: cover; filter: grayscale(100%); transition: all 0.4s ease; }
main nav ul li a:hover img { filter: none; transform: scale(1.05); }
main nav ul li a::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); border-radius: 16px; }
main nav ul li a h2 { position: absolute; bottom: 20px; left: 20px; color: #fff; font-size: 24px; z-index: 1; text-shadow: 2px 2px 4px rgba(0,0,0,0.7); }
.content-container { width: 95%; max-width: 1900px; margin: 0 auto; padding: 10px; border-radius: 8px; }
.content-container p { font-size: 1.1rem; line-height: 1.6; margin-bottom: 20px; color: #555; text-align: center; }
.loader-container { display: flex; justify-content: center; align-items: center; min-height: 600px; flex-direction: column; gap: 20px; }
.loader { border: 8px solid #f3f3f3; border-top: 8px solid var(--color-support-blue); border-radius: 50%; width: 60px; height: 60px; animation: spin 1.5s linear infinite; }
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
@media screen and (max-width: 1200px) { main nav ul { grid-template-columns: repeat(3, 1fr); } }
@media screen and (max-width: 920px) { .header nav { display: none; } .header { justify-content: center; } .header-mobile { display: block; } .header-mobile nav ul { display: flex; justify-content: space-evenly; padding: 12px 0; position: fixed; bottom: 0; left: 0; right: 0; z-index: 999; background-color: #fff; border-top: 2px solid #e0e0e0; } .header-mobile nav li { display: grid; gap: 4px; justify-items: center; } .header-mobile nav p { font-size: 12px; } main nav ul { grid-template-columns: repeat(2, 1fr); } .footer { display: none; } section { padding-bottom: 120px; } }
@media screen and (max-width: 600px) { .banner { height: 300px; } main nav ul { grid-template-columns: 1fr; } }
"""
with open("static/css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)
print("Arquivos do portal Flask criados com sucesso.")

# ==============================================================================
# PASSO 5.5: Gerando o arquivo HTML do mapa interativo
# ==============================================================================
print("\n--- [5.5/7] Gerando o mapa interativo (Folium)... ---")

try:
    url_geojson = 'https://raw.githubusercontent.com/FATCK06/ProjectAPI_FirstSemester/main/Delimita%C3%A7%C3%A3o%20da%20Zona%20de%20SJC/zonas_sjc_poligono.geojson'
    zonas = {
        "Zona Norte": {'populacao': 100000, 'area': 23.35},
        "Zona Sul": {'populacao': 90000, 'area': 32.69},
        "Zona Leste": {'populacao': 120000, 'area': 28.02},
        "Zona Centro": {'populacao': 72401, 'area': 18.68},
        "Zona Oeste": {'populacao': 64482, 'area': 25.66},
        "Zona Sudeste": {'populacao': 62541, 'area': 30.37}
    }

    cores = {
        "Zona Norte": "#e41a1c",
        "Zona Sul": "#377eb8",
        "Zona Leste": "#4daf4a",
        "Zona Oeste": "#984ea3",
        "Zona Centro": "#ff7f00",
        "Zona Sudeste": "#ffff33"
    }
    gdf = gpd.read_file(url_geojson)

    if gdf.crs is None:
        gdf.set_crs(epsg=4326, inplace=True)
    gdf_proj = gdf.to_crs(epsg=32723)
    gdf['area_km2'] = gdf_proj.geometry.area / 1e6
    centroids_proj = gdf_proj.centroid
    centroids_wgs = centroids_proj.to_crs(epsg=4326)
    gdf['centroid_lat'] = centroids_wgs.y
    gdf['centroid_lon'] = centroids_wgs.x
    def norm(s):
        if s is None:
            return ""
        s = str(s)
        s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
        s = s.lower()
        s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
        return s

    zonas_norm_map = { norm(k): k for k in zonas.keys() }
    map_center = [gdf['centroid_lat'].mean(), gdf['centroid_lon'].mean()]
    mapa = folium.Map(location=map_center, zoom_start=12, control_scale=True)
    js_functions = []
    for idx, row in gdf.iterrows():
        nome_raw = row.get('nome', '')
        nome_norm = norm(nome_raw)
        possible = difflib.get_close_matches(nome_norm, list(zonas_norm_map.keys()), n=1, cutoff=0.6)
        matched_key = zonas_norm_map[possible[0]] if possible else None
        populacao = zonas[matched_key]['populacao'] if matched_key else None
        area_calc = float(row['area_km2'])
        densidade = (populacao / area_calc) if (populacao and area_calc>0) else None
        cor = cores.get(matched_key if matched_key else nome_raw, "#3388ff")
        lat_c = float(row['centroid_lat'])
        lon_c = float(row['centroid_lon'])
        safe = re.sub(r'\W+', '_', nome_raw if nome_raw else f'zona_{idx}')
        geom_json = json.dumps(mapping(row.geometry))
        js_fn = f"""
    function togglePoly_{safe}(){{
      var map = {mapa.get_name()};
      if(window['poly_{safe}']){{
        map.removeLayer(window['poly_{safe}']);
        window['poly_{safe}'] = null;
      }} else {{
        window['poly_{safe}'] = L.geoJSON({geom_json}, {{
          style: function (feature) {{
            return {{color: '{cor}', weight: 2, fillOpacity: 0.45}};
          }}
        }}).addTo(map);
        try {{ map.fitBounds(window['poly_{safe}'].getBounds()); }} catch(e){{}}
      }}
    }}
    """
        js_functions.append(js_fn)
        pop_str = f"{int(populacao):,}".replace(',', '.') if populacao else "---"
        area_str = f"{area_calc:.2f}"
        dens_str = f"{densidade:.2f} hab/km²" if densidade else "---"
        safe_nome_url = urllib.parse.quote(nome_raw)
        
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; font-size:13px;">
          <b>{nome_raw if nome_raw else 'Sem nome'}</b><br>
          População: {pop_str}<br>
          Área: {area_str} km²<br>
          Densidade: {dens_str}<br>
          <a href="#" onclick="togglePoly_{safe}();return false;" style="color: #0654A5;">Mostrar/Esconder área</a><br>
          <br>
          <a href="/zona_detalhes?zona={safe_nome_url}" target="_top" style="font-weight: bold; color: #EC6608;">
             Ver gráficos desta zona &rarr;
          </a>
        </div>
        """

        folium.Marker(
            location=[lat_c, lon_c],
            popup=folium.Popup(popup_html, max_width=330),
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(mapa)
    script_all = "<script>\n" + "\n".join(js_functions) + "\n</script>"
    mapa.get_root().html.add_child(Element(script_all))
    mapa.save("templates/mapa.html")
    print("Mapa interativo 'templates/mapa.html' salvo com sucesso.")

except Exception as e:
    print(f"ERRO ao gerar o mapa: {e}")
    with open("templates/mapa.html", "w", encoding="utf-8") as f:
        f.write("<html><body><h1>Erro ao gerar o mapa</h1><p>{e}</p></body></html>")


# ==============================================================================
# PASSO 6: Inicia os servidores (Flask e Streamlit)
# ==============================================================================
print("\n--- [6/7] Configurando e iniciando os servidores... ---")

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0
FLASK_PORT = 5000
STREAMLIT_PORT = 8501
streamlit_public_url = None

print(f"Iniciando o Streamlit em background na porta {STREAMLIT_PORT}...")
proc = subprocess.Popen(
    ["streamlit", "run", STREAMLIT_APP_FILE, "--server.port", str(STREAMLIT_PORT), "--server.headless", "true", "--server.address", "0.0.0.0"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8"
)
atexit.register(proc.kill)

print("Aguardando o servidor do Streamlit ficar pronto...")
start_time = time.time()
while not is_port_in_use(STREAMLIT_PORT):
    time.sleep(0.5)
    if time.time() - start_time > 120:
        print("Erro: Streamlit demorou muito para iniciar.", proc.stderr.read())
        exit()
print("Servidor Streamlit iniciado.")


# ==============================================================================
# PASSO 7: Configura o Flask e inicia o Ngrok
# ==============================================================================
print("\n--- [7/7] Configurando e iniciando o servidor Flask ---")
AWS_PUBLIC_IP = os.environ.get('AWS_PUBLIC_IP', 'localhost')
if AWS_PUBLIC_IP == 'localhost':
    print("AVISO: Variável de ambiente 'AWS_PUBLIC_IP' não definida. Usando 'localhost' como fallback.")
    print("Para produção no AWS, defina esta variável ao rodar o Docker.")
streamlit_public_url = f"http://{AWS_PUBLIC_IP}:{STREAMLIT_PORT}"
print(f"URL do Streamlit (para iframes) definida como: {streamlit_public_url}")


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', title="Home", graficos=graficos_info)

@app.route("/grafico/<int:grafico_id>")
def pagina_grafico(grafico_id):
    global streamlit_public_url
    grafico = graficos_info.get(grafico_id)
    if not grafico:
        return "Gráfico não encontrado", 404
    return render_template('grafico.html', title=grafico["titulo"], streamlit_public_url=streamlit_public_url, grafico_id=grafico_id)
@app.route("/mapa")
def pagina_mapa():
    """Serve a página do mapa interativo."""
    return render_template('mapa.html')
@app.route("/zona_detalhes")
def pagina_zona_detalhes():
    global streamlit_public_url
    zona = request.args.get('zona')
    if not zona:
        return "Zona não especificada", 400
    return render_template('grafico.html', 
                           title=f"Dados da {zona}", 
                           streamlit_public_url=streamlit_public_url, 
                           grafico_id=None,
                           zona=zona)
try:
    print("\n" + "=" * 60)
    print(f"Servidor Flask iniciando em http://0.0.0.0:{FLASK_PORT}")
    print("Acesse este aplicativo pelo IP público do seu servidor.")
    print("=" * 60)
    app.run(host='0.0.0.0', port=FLASK_PORT)

except Exception as e:
    print(f"Erro ao iniciar o servidor Flask: {e}")