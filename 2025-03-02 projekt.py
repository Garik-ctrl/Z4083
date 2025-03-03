import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title("Interaktivní vizualizace akciových dat") # Titulek aplikace

tickers = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"] # Výběr z několika společností
ticker = st.selectbox("Zvolte ticker akcie:", tickers)

# Výběr časového období
start_date = st.date_input("Datum počátku:", pd.to_datetime("2025-01-01"))
end_date = st.date_input("Datum konce:", pd.to_datetime("today"))

# Načtení dat pomocí yfinance
data = yf.download('AAPL', start=start_date, end=end_date)

if not data.empty:
    st.subheader(f"Data pro akcii {ticker}")
    st.write(data)

    # Liniový graf zavírací ceny
    st.subheader("Graf zavírací ceny")
    fig_close, ax_close = plt.subplots()
    ax_close.plot(data.index, data['Close'], label='Zavírací cena')
    ax_close.set_xlabel("Datum")
    ax_close.set_ylabel("Cena (USD)")
    ax_close.legend()
    plt.xticks(rotation=45,ha="right")
    st.pyplot(fig_close)

    # vestavěný linový graf pomocí streamlitu (nad rámec lekce)
    st.subheader("Objem obchodů")
    st.line_chart(data['Volume'])

    # Histogram: Distribuce denních výnosů
    st.subheader("Histogram denních výnosů")
    data['Daily Return'] = data['Close'].pct_change()
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(data['Daily Return'].dropna(), bins=25) #bez prázdných hodnot, 25 'chlívků'
    ax_hist.set_xlabel("Denní výnos")
    ax_hist.set_ylabel("Frekvence")
    st.pyplot(fig_hist)

    # Scatter plot: Vztah mezi objemem a zavírací cenou
    st.subheader("Scatter plot: Objem vs. Zavírací cena")
    fig_scatter, ax_scatter = plt.subplots()
    ax_scatter.scatter(data['Volume'], data['Close'], alpha=0.5)
    ax_scatter.set_xlabel("Objem")
    ax_scatter.set_ylabel("Zavírací cena (USD)")
    st.pyplot(fig_scatter)

    # Heatmapa: Korelační matice vybraných sloupců (extra)
    st.subheader("Heatmapa korelační matice")
    corr_data = data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
    fig_heat, ax_heat = plt.subplots(figsize=(8, 6))

    # Vykreslení heatmapy s barevným schématem "coolwarm"
    cax = ax_heat.imshow(corr_data, cmap='coolwarm', interpolation='nearest')

    # Nastavení os a jejich popisků
    ax_heat.set_xticks(np.arange(len(corr_data.columns)))
    ax_heat.set_yticks(np.arange(len(corr_data.index)))
    ax_heat.set_xticklabels(corr_data.columns)
    ax_heat.set_yticklabels(corr_data.index)
    plt.setp(ax_heat.get_xticklabels(), rotation=45, ha="right")

    # Přidání anotací s hodnotami korelací
    for i in range(len(corr_data.index)):
        for j in range(len(corr_data.columns)):
            ax_heat.text(j, i, f"{corr_data.iloc[i, j]:.2f}", ha="center", va="center", color="black", fontsize=8)

    fig_heat.colorbar(cax)
    st.pyplot(fig_heat)


else:
    st.error("Nebyla nalezena žádná data. Zkontrolujte zadaný ticker nebo časové období.")
