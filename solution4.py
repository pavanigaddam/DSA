import urllib.request
import json

# Prompt the user for a URL
url = input("Enter location: ")

# Retrieve the JSON data from the URL
print(f"Retrieving {url}")
response = urllib.request.urlopen(url)
data = response.read()

# Decode the data into a string and check the length
print(f"Retrieved {len(data)} characters")

# Parse the JSON data
json_data = json.loads(data)

# Extract the 'comments' key, which contains a list of dictionaries
comments = json_data["comments"]

# Initialize the count and sum
count = 0
total_sum = 0

# Loop through the list and sum the 'count' value in each dictionary
for comment in comments:
    count += 1
    total_sum += comment["count"]

# Print the count and sum
print(f"Count: {count}")
print(f"Sum: {total_sum}")
