import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the dataset used in the notebook is loaded here
df = pd.read_csv('main_data.csv')

st.title("Bicycle Use: Visualization & Explanatory Analysis")

# Question 1: How do weather conditions affect bicycle use?
st.header("1. How do weather conditions affect bicycle use?")
st.write("""
Weather conditions such as temperature, humidity, and precipitation have a significant impact on bicycle usage. Warmer, drier weather tends to encourage cycling, while cold and wet conditions reduce it.
""")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x='temp', y='cnt', hue='weathersit')
ax.set_title("Bicycle Use vs Temperature and Weather Conditions")
st.pyplot(fig)

# Question 2: How does bicycle use vary between weekdays and weekends?
st.header("2. How does bicycle use vary between weekdays and weekends?")
st.write("""
There is a noticeable difference in bicycle usage between weekdays and weekends. On weekends, casual users often dominate, while weekdays see more consistent use from registered users.
""")

fig, ax = plt.subplots()
sns.boxplot(data=df, x='weekday', y='cnt')
ax.set_title("Bicycle Use on Weekdays vs Weekends")
st.pyplot(fig)

# Question 3: How does the behavior of casual and registered users differ?
st.header("3. How does the behavior of casual and registered users differ?")
st.write("""
Casual users are more likely to use bicycles on weekends and during specific times of the day, while registered users have more consistent patterns, likely due to commuting.
""")

fig, ax = plt.subplots()
sns.lineplot(data=df, x='hr', y='casual', label='Casual Users')
sns.lineplot(data=df, x='hr', y='registered', label='Registered Users')
ax.set_title("Bicycle Use by Hour for Casual and Registered Users")
st.pyplot(fig)

# Question 4: What are the trends in bicycle use throughout the year?
st.header("4. What are the trends in bicycle use throughout the year?")
st.write("""
Bicycle use fluctuates throughout the year, with peaks in spring and fall, likely due to favorable weather. Winter months see lower usage due to colder conditions.
""")

fig, ax = plt.subplots()
sns.lineplot(data=df, x='mnth', y='cnt')
ax.set_title("Monthly Trends in Bicycle Use")
st.pyplot(fig)

# Question 5: What are the patterns of bicycle use throughout the day?
st.header("5. What are the patterns of bicycle use throughout the day?")
st.write("""
Bicycle usage peaks during the morning (commute hours) and decreases in the afternoon and evening. This pattern is common for both casual and registered users.
""")

fig, ax = plt.subplots()
sns.lineplot(data=df, x='hr', y='cnt')
ax.set_title("Hourly Bicycle Use Patterns")
st.pyplot(fig)

all_df = pd.read_csv("main_data.csv")

# Mengonversi kolom 'dteday' ke format datetime
all_df["dteday"] = pd.to_datetime(all_df["dteday"])

# Mengurutkan berdasarkan kolom 'dteday'
all_df.sort_values(by="dteday", inplace=True)

# Reset indeks setelah pengurutan
all_df.reset_index(inplace=True, drop=True)

# Mendapatkan tanggal minimum dan maksimum dari kolom 'dteday'
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/Alfinfaiz/Bike-sharing-dataset/blob/main/istockphoto-979064894-170667a.jpg?raw=true")
    
    # Mengambil start_date & end_date dari date_input menggunakan 'dteday'
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    

