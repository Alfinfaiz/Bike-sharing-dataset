# Bike-sharing-dataset
This project analyzes the usage patterns of the **Capital Bikeshare system** using environmental, seasonal, and temporal factors. The dashboard is built using **Streamlit** to visualize how weather conditions, weekdays, weekends, and user behavior (casual vs registered users) affect bike rental usage.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- pandas
- seaborn
- matplotlib
- scikit-learn (if clustering is used)
- Streamlit

You can install the necessary dependencies by running:

```bash
pip install pandas seaborn matplotlib scikit-learn streamlit
```

# How to Run the Dashboard
1. Clone the repository or download the project files:
```bash
git clone <your-repository-url>
cd <project-directory>
```
2. Make sure your dataset files (hour.csv) are in the same directory as the script.
3. To launch the Streamlit dashboard, simply run:
```bash
streamlit run dashboard.py
```
4. Open the displayed local URL in your browser to view the interactive dashboard.

# Dashboard Overview
This dashboard answers five key questions regarding bike usage patterns:

1. How do weather conditions affect bicycle use?
2. How does bicycle use vary between weekdays and weekends?
3. How does the behavior of casual and registered users differ?
4. What are the trends in bicycle use throughout the year?
5. What are the patterns of bicycle use throughout the day?Each section provides visual insights using line plots, bar plots, and scatter plots, helping stakeholders understand the relationship between environmental
6. factors and bike rental usage.

#Conclusion
