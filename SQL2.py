import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Analýza světových měst")
# Připojení k MySQL databázi
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="world"
    )
def get_largest_cities():
    conn = get_connection()
    query = "SELECT Name, CountryCode, Population FROM city ORDER BY Population DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
nejvetsi_mesta=get_largest_cities()
print(nejvetsi_mesta)
# Funkce pro načtení ekonomických dat států
def get_country_economy():
    conn = get_connection()
    query = """
    SELECT Name, GNP, Population, (GNP / Population) AS GDP_Per_Capita 
    FROM country 
    WHERE GNP IS NOT NULL 
    ORDER BY GDP_Per_Capita DESC 
    LIMIT 10
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Funkce pro načtení nejpoužívanějších jazyků
def get_languages():
    conn = get_connection()
    query = """
    SELECT Language, COUNT(CountryCode) as CountryCount
    FROM countrylanguage
    WHERE IsOfficial = 'T'
    GROUP BY Language
    ORDER BY CountryCount DESC
    LIMIT 10
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit aplikace
st.title("Analýza světových dat")

tab1, tab2, tab3 = st.tabs(["Největší města", "Ekonomika států", "Nejčastější jazyky"])

# Největší města
with tab1:
    st.subheader("🏙 Top 10 nejlidnatějších měst")
    cities_df = get_largest_cities()
    st.dataframe(cities_df)

    # 📊 Vizualizace
    plt.figure(figsize=(10, 5))
    sns.barplot(x=cities_df["Name"], y=cities_df["Population"])
    plt.xticks(rotation=45)
    plt.xlabel("Město")
    plt.ylabel("Populace")
    plt.title("Top 10 nejlidnatějších měst")
    st.pyplot(plt)

# Ekonomika států
with tab2:
    st.subheader("💰 Top 10 zemí podle HDP na obyvatele")
    economy_df = get_country_economy()
    st.dataframe(economy_df)

    # Vizualizace
    plt.figure(figsize=(10, 5))
    sns.barplot(x=economy_df["Name"], y=economy_df["GDP_Per_Capita"])
    plt.xticks(rotation=45)
    plt.xlabel("Země")
    plt.ylabel("HDP na obyvatele")
    plt.title("Top 10 zemí podle HDP na obyvatele")
    st.pyplot(plt)

# Nejčastější jazyky
with tab3:
    st.subheader("🗣 Nejčastější úřední jazyky ve světě")
    languages_df = get_languages()
    st.dataframe(languages_df)

    # Vizualizace
    plt.figure(figsize=(10, 5))
    sns.barplot(x=languages_df["Language"], y=languages_df["CountryCount"])
    plt.xticks(rotation=45)
    plt.xlabel("Jazyk")
    plt.ylabel("Počet zemí, kde je úřední")
    plt.title("Nejčastější úřední jazyky")
    st.pyplot(plt)

st.sidebar.info("Připojeno k MySQL databázi 'world'")