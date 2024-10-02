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
Weather is one of the key factors influencing bicycle usage. This boxplot shows the distribution of bicycle usage across different weather conditions.
""")
fig, ax = plt.subplots()
sns.boxplot(data=hour_df, x='weathersit', y='cnt', ax=ax)
ax.set_title("The Effect of Weather Conditions on Bicycle Use")
ax.set_xlabel("Weather Conditions")
ax.set_ylabel("Number of Bicycle Users")
st.pyplot(fig)

### 2. How does bicycle use vary between weekdays and weekends?
st.header("2. How does bicycle use vary between weekdays and weekends?")
st.write("""
This bar plot shows the average number of bicycle users on weekdays compared to weekends. Weekdays are labeled as 1, and weekends as 0.
""")
fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=hour_df, ci=None, ax=ax)
ax.set_title("Bicycle Use Between Weekdays and Weekends")
ax.set_xlabel("Weekdays (1) vs Weekends (0)")
ax.set_ylabel("Number of Bicycle Users")
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

### 4. What are the trends in bicycle use throughout the year??
st.header("4. What are the trends in bicycle use throughout the year?")
st.write("""
This line plot shows the trends in bicycle usage across different months, comparing usage between two years (Year 0 and Year 1).
""")
fig, ax = plt.subplots()
sns.lineplot(data=hour_df, x='mnth', y='cnt', hue='yr', ax=ax)
ax.set_title("Monthly Bicycle Usage Trends by Year")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Bicycle Users")
st.pyplot(fig)

### 5. What are the patterns of bicycle use throughout the day using manual grouping?
st.header("5. What are the patterns of bicycle use throughout the day using manual grouping?")
st.write("""
This bar plot shows bicycle usage based on different times of the day, grouped into Morning, Afternoon, and Night.
""")

# Manual grouping: Morning (6-12), Afternoon (12-18), and Night (other times)
def manual_grouping(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

# Apply manual grouping to the dataset
hour_df['time_of_day'] = hour_df['hr'].apply(manual_grouping)

# Define the specific order for the x-axis
time_order = ['Afternoon', 'Evening', 'Morning']

# Visualize the manual grouping with a bar plot
fig, ax = plt.subplots(figsize=(7, 5))  # Set figure size to match the provided plot
sns.barplot(x='time_of_day', y='cnt', data=hour_df, estimator=sum, ci=None, ax=ax, color="lightblue", order=time_order)  # Set the specific order and color

ax.set_title("Bicycle Usage Based on Time of Day", fontsize=14)
ax.set_xlabel("Time of Day", fontsize=12)
ax.set_ylabel("Number of Bicycle Users", fontsize=12)

# Rotate the x-axis labels to match the image
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Adjust y-axis format to show numbers in scientific notation (1e6)
ax.ticklabel_format(style='sci', axis='y', scilimits=(6,6))

# Display the plot
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
    st.image("https://github.com/Alfinfaiz/Bike-sharing-dataset/blob/main/istockphoto-979064894-170667a.jpg?raw=true")
    
    # Mengambil start_date & end_date dari date_input menggunakan 'dteday'
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
