# sending sms using Infobip API

from infobip_channels.sms.channel import SMSChannel
from infobip_api_client.exceptions import ApiException


BASE_URL = "https://y31z29.api.infobip.com"
API_KEY = ""
RECIPIENT = "254724050208"
MESSAGE = "Hello test message from python infoBip"
# initialize channel with credentials
channel = SMSChannel.from_auth_params(
    {
        "base_url": BASE_URL,
        "api_key": API_KEY,
    }
)

def main():
    try:
        # populating message fields
        sms_response = channel.send_sms_message(
            {
                "messages": [
                    {
                        "destinations": [{"to": RECIPIENT}],
                        "text": MESSAGE,
                    }
                ]
            }
        )
        # get delivery reports
        query_parameters = {"limit": 10}
        delivery_reports = channel.get_outbound_sms_delivery_reports()
        
        # see delivery reports
        print(delivery_reports)
    except ApiException as ex:
        
        print("Error occurred while trying to send SMS message.")
        print("Error status: %s\n" % ex.status)
        print("Error headers: %s\n" % ex.headers)
        print("Error body: %s\n" % ex.body)
        print("Error reason: %s\n" % ex.reason)




if __name__ == "__main__":
    main()
    
        