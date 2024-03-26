import requests

# API endpoint (example using SpaceX API for latest launch)
api_url = "https://api.spacexdata.com/v5/launches/latest"

# Sending a GET request
response = requests.get(api_url)

# Handling the response
if response.status_code == 200:
    # Response content as JSON
    data = response.json()

    print(f"Response Status Code: {response.status_code}")
    
    print(f"\n>> LAUNCH INFORMATION <<\n")
    print(f"Mission Group: {data["name"]}")
    print(f"Flight Number: {data["flight_number"]}")
    print(f"Rocket ID: {data["rocket"]}")
    print(f"Success: {data["success"]}")

    crew_list = data["crew"]
    print("Crew:")
    for crew_member in crew_list:
        print(f"  - Crew ID: {crew_member['crew']}")
        print(f"    Role: {crew_member['role']}")
else:
    print(f"Request failed with status code: {response.status_code}")
