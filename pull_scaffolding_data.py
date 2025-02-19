# Use Python to pull odata data from the Scaffolding API
# url is https://data.cityofnewyork.us/api/odata/v4/kiqr-y92a

import requests
import json
import pandas as pd
# Set the URL for the API endpoint
url = 'https://data.cityofnewyork.us/resource/kiqr-y92a.json&$count=true'
# Send a GET request to the API endpoint
response = requests.get(url)
# Parse the JSON response
data = json.loads(response.text)
# Convert the JSON data to a Pandas DataFrame
df = pd.DataFrame(data)
# Print the DataFrame
print(
    df
)
# Save the DataFrame to a CSV file
df.to_csv('scaffolding_data.csv', index=False)
# Print a message to confirm the data was saved
print('Data saved to scaffolding_data.csv')


