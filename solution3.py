import urllib.request
import xml.etree.ElementTree as ET

def main():
    # Prompt for a URL
    url = input('Enter location: ')
    if not url:
        print("No URL provided. Exiting.")
        return

    print(f'Retrieving {url}')
    try:
        # Read the XML data from the URL
        response = urllib.request.urlopen(url)
        data = response.read()
        print(f'Retrieved {len(data)} characters')

        # Parse the XML data
        tree = ET.fromstring(data)

        # Find all <count> tags using XPath
        counts = tree.findall('.//count')

        # Extract the text values of <count> tags and convert them to integers
        count_values = [int(count.text) for count in counts]

        # Compute the sum of the counts
        total_sum = sum(count_values)

        # Output the results
        print(f'Count: {len(count_values)}')
        print(f'Sum: {total_sum}')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()