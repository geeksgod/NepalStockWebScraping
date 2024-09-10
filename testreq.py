import requests

# Step 1: Define the URL
url = "https://nepalstock.com.np/api/nots/nepse-data/floorsheet?&size=20&sort=contractId,desc"

# Step 2: Set up headers to mimic a real browser request (User-Agent)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.7',
    'Authorization': 'Salter eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..jlmETKloQaIzLmoDDBP0ZQ.0Qu7H0tcUBW3WWwQI_XzusCyWIkjt5aj-Z31GoosZt6CN2jHonJBwd_79ml2_MnCIACrndhizbH_jLdEgcE0WArKgEGwIO0ylbc0EbpV9LQb-5W4e-7WV1JiI_IUmqzOTPcCL4KAJzEjVnaG-YYBNQ.RfwwFXw0KgH3p-z-IakfEg',
    'Connection': 'keep-alive',
    'Content-Length': '13',
    'Content-Type': 'application/json'

}

# Step 3: Send the GET request with headers
response = requests.post(url, headers=headers, verify=False)  # verify=False to skip SSL certificate verification

# Step 4: Print the response
print("Status Code:", response.status_code)
print("Response Content:", response.text)