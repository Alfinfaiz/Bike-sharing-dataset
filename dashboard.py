import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
hour_df = pd.read_csv('main_data.csv')

# Set the title and description of the project
st.title("Bicycle Usage Data Analysis: Based on Weather, Days, and User Type")
st.write("""
This project answers key business questions regarding bicycle usage based on various factors such as weather, weekdays vs. weekends, and user types (casual vs. registered).
""")

### 1. How do weather conditions affect bicycle use?
st.header("1. How do weather conditions affect bicycle use?")
st.write("""
Weather is one of the key factors influencing bicycle usage. This visualization shows the relationship between temperature, humidity, wind speed, and bicycle usage.
""")
fig, ax = plt.subplots()
sns.scatterplot(data=hour_df, x='temp', y='cnt', hue='weathersit', ax=ax)
ax.set_title("Bicycle Usage by Temperature and Weather Conditions")
ax.set_xlabel("Temperature")
ax.set_ylabel("Bicycle Count")
st.pyplot(fig)

### 2. How does bicycle use vary between weekdays and weekends?
st.header("2. How does bicycle use vary between weekdays and weekends?")
st.write("""
There is a significant difference in bicycle usage between weekdays and weekends. Weekdays typically see higher usage from registered users, while weekends attract more casual users.
""")
fig, ax = plt.subplots()
sns.boxplot(data=hour_df, x='weekday', y='cnt', ax=ax)
ax.set_title("Distribution of Bicycle Usage: Weekdays vs Weekends")
ax.set_xlabel("Day of the Week (0 = Sunday, 6 = Saturday)")
ax.set_ylabel("Bicycle Count")
st.pyplot(fig)

### 3. How does the behavior of casual and registered users differ?
st.header("3. How does the behavior of casual and registered users differ?")
st.write("""
Casual users are more likely to use bicycles on weekends and during specific times of the day, while registered users typically use bicycles during rush hours for commuting.
""")
fig, ax = plt.subplots()
sns.lineplot(data=hour_df, x='hr', y='casual', label='Casual Users', ax=ax)
sns.lineplot(data=hour_df, x='hr', y='registered', label='Registered Users', ax=ax)
ax.set_title("Bicycle Usage by Hour: Casual vs Registered Users")
ax.set_xlabel("Hour")
ax.set_ylabel("Bicycle Count")
st.pyplot(fig)

### 4. What are the trends in bicycle use throughout the year?
st.header("4. What are the trends in bicycle use throughout the year?")
st.write("""
Bicycle usage fluctuates throughout the year, with peaks during spring and fall, likely due to favorable weather conditions.
""")
fig, ax = plt.subplots()
sns.lineplot(data=hour_df, x='mnth', y='cnt', ax=ax)
ax.set_title("Monthly Bicycle Usage Trends")
ax.set_xlabel("Month")
ax.set_ylabel("Bicycle Count")
st.pyplot(fig)

### 5. What are the patterns of bicycle use throughout the day using manual grouping?
st.header("5. What are the patterns of bicycle use throughout the day using manual grouping?")
st.write("""
The manual grouping method is used to understand patterns of bicycle usage throughout the day by segmenting hours based on usage behavior.
""")

# Assuming manual grouping has already been performed in the EDA, and you've grouped the data into categories
# You can either have a column for 'group' in hour_df, or define the groupings here manually.

# For example, assume you have groups like this (customize based on your manual grouping):
def manual_grouping(hour):
    if 0 <= hour <= 6:
        return 'Late Night'
    elif 7 <= hour <= 10:
        return 'Morning Rush'
    elif 11 <= hour <= 16:
        return 'Daytime'
    elif 17 <= hour <= 19:
        return 'Evening Rush'
    else:
        return 'Night'

hour_df['group'] = hour_df['hr'].apply(manual_grouping)

# Visualize the manual grouping
fig, ax = plt.subplots()
sns.scatterplot(data=hour_df, x='hr', y='cnt', hue='group', palette='Set1', ax=ax)
ax.set_title("Bicycle Usage Patterns by Manual Grouping")
ax.set_xlabel("Hour")
ax.set_ylabel("Bicycle Count")
st.pyplot(fig)

# Footer
st.write("""
### Conclusion:
This analysis highlights that weather conditions, weekdays vs. weekends, and user types (casual vs. registered) have a significant impact on bicycle usage. Additionally, manual grouping helps identify patterns in bicycle usage throughout the day.
""")

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
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input menggunakan 'dteday'
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
