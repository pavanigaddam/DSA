import urllib.request, urllib.parse, urllib.error
import json


def get_plus_code(location):
    base_url = "http://py4e-data.dr-chuck.net/opengeo?"

    # Encode the parameters
    params = {"q": location}
    url = base_url + urllib.parse.urlencode(params)

    print(f"Retrieving {url}")

    # Retrieve the data from the API
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()

    print(f"Retrieved {len(data)} characters")

    # Load the JSON data
    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        print("Failed to retrieve JSON")
        return None

    # Extract the plus_code
    plus_code = js.get("plus_code")
    if plus_code:
        return plus_code
    else:
        print("No plus_code found in JSON response")
        return None


if __name__ == "__main__":
    location = input("Enter location: ")
    plus_code = get_plus_code(location)
    if plus_code:
        print("Plus code", plus_code)
