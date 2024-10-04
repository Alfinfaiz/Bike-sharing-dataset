import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
hour_df = pd.read_csv('hour_clean.csv')

# Set the title and description of the project
st.title("Weather and Seasonal Influences on Bike Sharing: A Study Using the Capital Bikeshare Dataset")
st.write("""
The purpose of this project is to analyze bike rental patterns from the Capital Bikeshare system in Washington D.C. and understand how environmental factors such as weather conditions, temperature, and seasonality affect the number of bicycle users.
""")

### 1. How do weather conditions affect bicycle use?
st.header("1. How do weather conditions affect bicycle use?")
st.write("""
Weather is one of the key factors influencing bicycle usage. This boxplot shows the distribution of bicycle usage across different weather conditions.
""")
# Mapping of weather conditions
weather_conditions = {
    1: 'Clear/Partly Cloudy',
    2: 'Mist/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Heavy Rain/Snow'
}
# Replace numerical weather codes with descriptive labels
hour_df['weathersit'] = hour_df['weathersit'].map(weather_conditions)

# Calculate the average number of users for each weather condition
weather_avg = hour_df.groupby('weathersit')['cnt'].mean().reset_index()

# Create the Streamlit interface
st.title('The Effect of Weather Conditions on Bicycle Use')

# Create a bar chart using Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(weather_avg['weathersit'], weather_avg['cnt'], color='skyblue')

# Set titles and labels
ax.set_title('The Effect of Weather Conditions on Bicycle Use')
ax.set_xlabel('Weather Conditions')
ax.set_ylabel('Average Number of Bicycle Users')

# Rotate x-ticks for readability
plt.xticks(rotation=45)

# Display the chart in Streamlit
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
st.header("Conclusion")

conclusions = """
- **Question 1: How do weather conditions affect bicycle use?**  
  The analysis results show that weather conditions significantly impact the number of bicycle users. The highest usage is recorded during clear weather and light mist, while usage drastically decreases during light to heavy rain. This highlights that good weather encourages more people to use bicycles.

- **Question 2: How does bicycle use vary between weekdays and weekends?**  
  The analysis indicates a significant difference between bicycle usage on workdays and weekends. Usage tends to be higher on workdays compared to weekends, likely due to more registered users using bicycles for their regular commutes.

- **Question 3: How does the behavior of casual and registered users differ?**  
  Registered users demonstrate a more consistent usage pattern throughout the day compared to casual users. Casual users tend to use bicycles during specific times, particularly on weekends, suggesting that they prefer using bicycles for recreational purposes.

- **Question 4: What are the trends in bicycle use throughout the year?**  
  Monthly trend analysis shows fluctuations in bicycle usage throughout the year, with peaks occurring in specific months such as May and September. Conversely, lower usage is observed in January and February, likely due to colder weather conditions during those months. This indicates that weather factors influence users' preferences for cycling.

- **Question 5: What are the patterns of bicycle use throughout the day?**  
  1. **Bicycle Usage Patterns Throughout the Day**:  
     The visualization indicates that bicycle usage varies significantly throughout the day. The "Morning" category (from 6:00 AM to 11:59 AM) shows the highest number of users, suggesting that many individuals utilize bicycles for commuting to work or school during this time.
  
  2. **Peak Usage During Daytime**:  
     There is a noticeable decline in the number of bicycle users during the "Afternoon" category (from 12:00 PM to 5:59 PM). This decrease may reflect that many people are indoors at work or engaged in other activities, leading to reduced bicycle usage.
  
  3. **Decrease in Usage During Evening and Night**:  
     The "Evening" category (from 6:00 PM to 5:59 AM) also shows a lower number of users compared to the morning. This may indicate that fewer individuals opt for cycling during the late evening and nighttime hours, possibly due to safety concerns or reduced visibility.
"""

st.write(conclusions)

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
