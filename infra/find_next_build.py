import requests
import time
import base64


public_ip = "54.173.88.175"
jenkins_url = f"http://{public_ip}:8080/job/build/lastBuild/buildNumber"
username = "shubham"
api_token = "117d96b00c5a2c73b08ee57c72e9ec721f"

auth_string = base64.b64encode(f"{username}:{api_token}".encode()).decode()

headers = {
    "Authorization": f"Basic {auth_string}"
}
response = requests.get(jenkins_url, headers=headers)
next_build = int(response.text.strip())+1
print(f"next_build={next_build}")
