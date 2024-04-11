import pandas as pd
#from geopy.geocoders import Nominatim

def scale_coordinates(input_file, output_file, target_width, target_height):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Initialize geocoder
   # geolocator = Nominatim(user_agent="coordinate_scaler")

    # Create new columns for scaled coordinates
    df['scaled_latitude'] = 0.0
    df['scaled_longitude'] = 0.0

    # Find the maximum range of latitudes and longitudes in the dataset
    min_lat, max_lat = df['Latitude'].min(), df['Latitude'].max()
    min_lon, max_lon = df['Longitude'].min(), df['Longitude'].max()

    # Calculate scaling factors for latitude and longitude
    lat_scaling_factor = target_height / (max_lat - min_lat)
    lon_scaling_factor = target_width / (max_lon - min_lon)

    # Iterate through rows and scale coordinates
    for index, row in df.iterrows():
        # Get latitude and longitude from the DataFrame
        latitude, longitude = row['Latitude'], row['Longitude']

        # Scale latitude and longitude
        scaled_latitude = (latitude - min_lat) * lat_scaling_factor
        scaled_longitude = (longitude - min_lon) * lon_scaling_factor

        # Store scaled coordinates in the DataFrame
        df.at[index, 'scaled_latitude'] = scaled_latitude
        df.at[index, 'scaled_longitude'] = scaled_longitude

    print(df)
    # Save the DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

# Example usage
input_file = 'campus_buildings.xlsx'
output_file = 'scaled_campus_buildings.xlsx'
target_width = 100   # Example target width in meters
target_height = 200   # Example target height in meters

scale_coordinates(input_file, output_file, target_width, target_height)
