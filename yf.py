import requests
from requests.structures import CaseInsensitiveDict

url = "https://www.your-freedom.net/api.php"

headers = CaseInsensitiveDict()
headers["Content-Length"] = "177"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Host"] = "www.your-freedom.net"
headers["Connection"] = "Keep-Alive"

data = "cmd=create_account&data=%7B%22username%22%3A%22a_fhvkzerkk%22%2C%22password%22%3A%22uux5qQB46p%22%2C%22email%22%3A%22ssjdhjajaaj%40gmail.com%22%2C%22no_verification%22%3Atrue%7D"


resp = requests.post(url, headers=headers, data=data)

print(resp.text)
