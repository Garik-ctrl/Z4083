import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🚀 API ENDPOINTY
API_OPTIONS = {
    "Kryptoměny": "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1",
    "Počasí": "https://api.open-meteo.com/v1/forecast?latitude=50.08&longitude=14.43&daily=temperature_2m_max,temperature_2m_min&timezone=Europe/Prague",
    "Směnné kurzy": "https://api.exchangerate-api.com/v4/latest/USD"
}

# Streamlit UI
st.title("🔗 API Analýza dat")
api_choice = st.sidebar.selectbox("Vyber API", list(API_OPTIONS.keys()))


# 1. Získání dat z API
@st.cache_data
def fetch_data(url):
    response = requests.get(url)
    return response.json()


data = fetch_data(API_OPTIONS[api_choice])

# 2. Analýza a vizualizace podle výběru API

if api_choice == "📈 Kryptoměny":
    st.subheader("📊 Analýza kryptoměn")
    df = pd.DataFrame(data)[["name", "symbol", "current_price", "market_cap", "price_change_percentage_24h"]]

    st.dataframe(df)

    # Vizualizace změny cen
    plt.figure(figsize=(10, 5))
    ax = sns.barplot(x=df["symbol"], y=df["price_change_percentage_24h"])
    plt.xlabel("Kryptoměna")
    plt.ylabel("Změna ceny (%)")
    plt.title("Denní změna ceny kryptoměn")

    # Popisky hodnot
    for index, value in enumerate(df["price_change_percentage_24h"]):
        ax.text(index, value + 0.5, f"{value:.2f}%", ha='center', fontsize=10, color='black')

    st.pyplot(plt)

elif api_choice == "🌍 Počasí":
    st.subheader("🌡 Počasí v Praze")
    df = pd.DataFrame({
        "Den": pd.date_range(start=pd.Timestamp.today(), periods=7, freq="D"),
        "Max Teplota (°C)": data["daily"]["temperature_2m_max"],
        "Min Teplota (°C)": data["daily"]["temperature_2m_min"]
    })

    st.dataframe(df)

    # Vizualizace teplot
    plt.figure(figsize=(10, 5))
    plt.plot(df["Den"], df["Max Teplota (°C)"], marker="o", label="Max Teplota")
    plt.plot(df["Den"], df["Min Teplota (°C)"], marker="o", linestyle="dashed", label="Min Teplota")
    plt.fill_between(df["Den"], df["Min Teplota (°C)"], df["Max Teplota (°C)"], alpha=0.2)
    plt.xlabel("Datum")
    plt.ylabel("Teplota (°C)")
    plt.title("Týdenní předpověď počasí")
    plt.legend()

    st.pyplot(plt)

elif api_choice == "💵 Směnné kurzy":
    st.subheader("💲 Směnné kurzy (USD)")
    rates = data["rates"]
    df = pd.DataFrame(rates.items(), columns=["Měna", "Kurz USD"])
    df = df.sort_values("Kurz USD", ascending=False).head(10)

    st.dataframe(df)

    # Vizualizace kurzů
    plt.figure(figsize=(10, 5))
    ax = sns.barplot(x=df["Měna"], y=df["Kurz USD"])
    plt.xlabel("Měna")
    plt.ylabel("Kurz vůči USD")
    plt.title("Top 10 směnných kurzů vůči USD")

    # Popisky hodnot
    for index, value in enumerate(df["Kurz USD"]):
        ax.text(index, value + 0.1, f"{value:.2f}", ha='center', fontsize=10, color='black')

    st.pyplot(plt)

st.sidebar.info(f"🔗 API: {API_OPTIONS[api_choice]}")
