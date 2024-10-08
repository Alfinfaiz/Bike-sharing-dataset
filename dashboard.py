import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
hour_df = pd.read_csv('main_data.csv')

# Set the title and description of the project
st.title("Weather and Seasonal Influences on Bike Sharing: A Study Using the Capital Bikeshare Dataset")
st.write("""
The purpose of this project is to analyze bike rental patterns from the Capital Bikeshare system in Washington D.C. and understand how environmental factors such as weather conditions, temperature, and seasonality affect the number of bicycle users.
""")

### Sidebar for image and date range selection
with st.sidebar:
    # Add image with a caption in the sidebar
    st.image("https://github.com/Alfinfaiz/Bike-sharing-dataset/blob/main/istockphoto-979064894-170667a.jpg?raw=true", 
             caption="Rentang Waktu", use_column_width=True)
    
    # Loading all dataset again to get the date range
    all_df = pd.read_csv("main_data.csv")
    
    # Convert 'dteday' to datetime format
    all_df["dteday"] = pd.to_datetime(all_df["dteday"])
    
    # Get the minimum and maximum date from 'dteday' column
    min_date = all_df["dteday"].min()
    max_date = all_df["dteday"].max()
    
    # Add a date range picker
    start_date, end_date = st.date_input(
        label='Rentang Waktu', 
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

### 1. How do weather conditions affect bicycle use?
st.header("1. How do weather conditions affect bicycle use?")
st.write("""
Weather is one of the key factors influencing bicycle usage. This boxplot shows the distribution of bicycle usage across different weather conditions.
""")

# Calculate average users for each weather condition
weather_avg = hour_df.groupby('weathersit')['cnt'].mean().reset_index()

# Map weather conditions
weather_conditions = {
    1: 'Clear/Partly Cloudy',
    2: 'Mist/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Heavy Rain/Snow'
}
weather_avg['weathersit'] = weather_avg['weathersit'].map(weather_conditions)

# Set category order
weather_avg['weathersit'] = pd.Categorical(weather_avg['weathersit'], 
                                            categories=['Clear/Partly Cloudy', 'Mist/Cloudy', 'Light Snow/Rain', 'Heavy Rain/Snow'],
                                            ordered=True)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(weather_avg['weathersit'], weather_avg['cnt'], color='skyblue')

# Set title and labels
plt.title('The Effect of Weather Conditions on Bicycle Use')
plt.xlabel('Weather Conditions')
plt.ylabel('Average Number of Bicycle Users')

# Display plot in Streamlit
st.pyplot(plt)

# Conclusion for Question 1
st.write("""
- **Conclusion**: The analysis results show that weather conditions significantly impact the number of bicycle users. The highest usage is recorded during clear weather and light mist, while usage drastically decreases during light to heavy rain. This highlights that good weather encourages more people to use bicycles.
""")

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

# Conclusion for Question 2
st.write("""
- **Conclusion**: The analysis indicates a significant difference between bicycle usage on workdays and weekends. Usage tends to be higher on workdays compared to weekends, likely due to more registered users using bicycles for their regular commutes.
""")

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

# Conclusion for Question 3
st.write("""
- **Conclusion**: Registered users demonstrate a more consistent usage pattern throughout the day compared to casual users. Casual users tend to use bicycles during specific times, particularly on weekends, suggesting that they prefer using bicycles for recreational purposes.
""")

### 4. What are the trends in bicycle use throughout the year??
st.header("4. What are the trends in bicycle use throughout the year?")
st.write("""
This plot shows bicycle usage trends by month, comparing data between 2011 and 2012.
""")

plt.figure(figsize=(14, 6))
sns.lineplot(x='mnth', y='cnt', hue='yr', data=hour_df, ci=None)
plt.title('Trends in Bicycle Use Throughout the Year')
plt.xlabel('Month')
plt.ylabel('Number of Bicycle Users')

# Modify the legend to show actual years
new_labels = ['2011', '2012']
plt.legend(title='Year', labels=new_labels)

# Display the plot in Streamlit
st.pyplot(plt)

# Conclusion for Question 4
st.write("""
- **Conclusion**: Monthly trend analysis shows fluctuations in bicycle usage throughout the year, with peaks occurring in specific months such as May and September. Conversely, lower usage is observed in January and February, likely due to colder weather conditions during those months. This indicates that weather factors influence users' preferences for cycling.
""")

### 5. What are the patterns of bicycle use throughout the day using manual grouping?
st.header("5. What are the patterns of bicycle use throughout the day using manual grouping?")
st.write("""
This bar plot shows bicycle usage based on different times of the day, grouped into Morning, Afternoon, and Night.
""")

# Manual grouping for time of day
def manual_grouping(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

hour_df['time_of_day'] = hour_df['hr'].apply(manual_grouping)

# Define the order for the x-axis
time_order = ['Afternoon', 'Evening', 'Morning']

# Create a bar plot
fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(x='time_of_day', y='cnt', data=hour_df, estimator=sum, ci=None, ax=ax, color="lightblue", order=time_order)

ax.set_title("Bicycle Usage Based on Time of Day", fontsize=14)
ax.set_xlabel("Time of Day", fontsize=12)
ax.set_ylabel("Number of Bicycle Users", fontsize=12)

# Rotate x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Adjust y-axis format
ax.ticklabel_format(style='sci', axis='y', scilimits=(6,6))

# Display the plot
st.pyplot(fig)

# Conclusion for Question 5 with multiple points
st.write("""
- **Conclusion**:
  1. **Bicycle Usage Patterns Throughout the Day**:  
     The visualization indicates that bicycle usage varies significantly throughout the day. The "Morning" category (from 6:00 AM to 11:59 AM) shows the highest number of users, suggesting that many individuals utilize bicycles for commuting to work or school during this time.
  
  2. **Peak Usage During Daytime**:  
     There is a noticeable decline in the number of bicycle users during the "Afternoon" category (from 12:00 PM to 5:59 PM). This decrease may reflect that many people are indoors at work or engaged in other activities, leading to reduced bicycle usage.
  
  3. **Decrease in Usage During Evening and Night**:  
     The "Evening" category (from 6:00 PM to 5:59 AM) also shows a lower number of users compared to the morning. This may indicate that fewer individuals opt for cycling during the late evening and nighttime hours, possibly due to safety concerns or reduced visibility.
""")
