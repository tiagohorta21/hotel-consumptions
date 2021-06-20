import pandas as pd


# Returns season from month number
def getSeason(month):
    if 1 <= month <= 2:
        return 'Winter'
    elif 3 <= month <= 5:
        return 'Sprint'
    elif 6 <= month <= 8:
        return 'Summer'
    elif 9 <= month <= 11:
        return 'Autumn'
    elif month == 12:
        return 'Winter'


# Load hotel consumptions csv
hotel_consumptions = pd.read_csv('hotel_consumptions.csv')

# Fill all the NaN values for 0
hotel_consumptions = hotel_consumptions.fillna(0)

# Convert OcupPaxs values to int
hotel_consumptions['OcupPaxs'] = hotel_consumptions['OcupPaxs'].astype(int)

# Rename columns
hotel_consumptions = hotel_consumptions.rename(
    mapper={'windSpeed': 'Wind Speed', 'OcupPaxs': 'Guests', 'CTotal': 'Total Consumption'},
    axis='columns')

# Create a new column for week days
hotel_consumptions['Week Day'] = pd.to_datetime(hotel_consumptions['Timestamp'])
hotel_consumptions['Week Day'] = hotel_consumptions['Week Day'].dt.day_name()

# Add a new seasons column
hotel_consumptions['Season'] = pd.to_datetime(hotel_consumptions['Timestamp'])
hotel_consumptions['Season'] = hotel_consumptions['Season'].dt.month
hotel_consumptions['Season'] = hotel_consumptions['Season'].apply(getSeason)

# Reindex columns
hotel_consumptions = hotel_consumptions.reindex(
    columns=['Wind Speed', 'Temperature', 'Guests', 'Timestamp', 'Week Day', 'Season', 'Total Consumption'])

print(hotel_consumptions)
