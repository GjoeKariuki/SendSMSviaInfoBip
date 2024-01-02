import http.client
import json


BASE_URL = "y31z29.api.infobip.com"
API_KEY = ""

SENDER = "InfoSMS"
RECIPIENT = "254724050208"
MESSAGE_TEXT = "This is a sample message"

conn = http.client.HTTPSConnection(BASE_URL)


payload1 = "{\"messages\":" \
          "[{\"from\":\"" + SENDER + "\"" \
          ",\"destinations\":" \
          "[{\"to\":\"" + RECIPIENT + "\"}]," \
          "\"text\":\"" + MESSAGE_TEXT + "\"}]}"


payload2 = json.dumps({
    "messages": [
        {"destinations":[{"to":"254724050208"}],
         "from": "CintelCoreSMS",
         "text": "This is your OTP code"}
    ]
})

headers = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


#conn.request("POST", "/sms/2/text/advanced", payload1, headers)
conn.request("POST", "/sms/2/text/advanced", payload2, headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))