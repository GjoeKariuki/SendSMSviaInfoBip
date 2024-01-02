from infobip_channels.sms.channel import SMSChannel
from infobip_api_client.exceptions import ApiException

class InfoBipSend:
    def __init__(self, base_url, api_key):
        self.channel = SMSChannel.from_auth_params({
            "base_url": base_url,
            "api_key": api_key,
        })

    def send_sms(self, recipient, message):
        try:
            sms_response = self.channel.send_sms_message(
                {
                    "messages": [
                        {
                            "destinations":[{"to":recipient}],
                            "text": message
                        }
                    ]
                }
            )
            # get delivery reports
            query_parameters = {"limit": 10}
            delivery_reports = self.channel.get_outbound_sms_delivery_reports()
            
            # see delivery reports
            print(delivery_reports)
        except ApiException as ex:

            print("Error occurred while trying to send SMS message.")
            print("Error status: %s\n" % ex.status)
            print("Error headers: %s\n" % ex.headers)
            print("Error body: %s\n" % ex.body)
            print("Error reason: %s\n" % ex.reason)


if __name__ == "__main__":

    BASE_URL = "https://y31z29.api.infobip.com"
    API_KEY = ""
    RECIPIENT = "254724050208"
    MESSAGE = "Hello test message from python infoBip"

    info_send_sms = InfoBipSend(BASE_URL,API_KEY)
    info_send_sms.send_sms(RECIPIENT,MESSAGE)