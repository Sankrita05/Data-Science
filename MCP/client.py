import requests

def test_multiply(a, b):
    response = requests.post("http://127.0.0.1:8080/multiply", json={"a":a, "b":b})
    if response.status_code==200:
        print("Multiplication of MCP called successfully", response.json()["result"])
    else:
        print("There is an issue")

if __name__=="__main__":
    test_multiply(6,7)
