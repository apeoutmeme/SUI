import requests
import json

sui_rpc_url = "https://fullnode.mainnet.sui.io:443"

payload = {
    "jsonrpc": "2.0",
    "method": "sui_getChainIdentifier", 
    "params": [],
    "id": 1
}

try:
    response = requests.post(sui_rpc_url, json=payload)
    response.raise_for_status()

    result = response.json()
    print("Connected successfully to the Sui Network!")
    print("Chain Identifier:", result.get("result"))
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)
