import requests

dataset_url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# make a GET request to retrieve the dataset
response = requests.get(dataset_url)

# check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content to a file named "cso.json"
    with open("cso.json", "wb") as file:
        file.write(response.content)
    print("Dataset successfully downloaded and saved to 'cso.json'")
else:
    print(f"Failed to retrieve the dataset. Status code: {response.status_code}")
