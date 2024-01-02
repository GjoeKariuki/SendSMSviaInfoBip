from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.exceptions import ApiException


client_config = Configuration(
    host = "https://y31z29.api.infobip.com",
    api_key = {"APIKeyHeader": ""},
    # api_key_prefix= {"APIKeyHeader": "CintelCoreApp"},
)

api_client = ApiClient(client_config)


sms_request = SmsAdvancedTextualRequest(
    messages = [
        SmsTextualMessage(
            destinations = [
                SmsDestination(
                    to="254724050208",
                ),
            ],
            _from = "CintelCoreAMS",
            text = "this is your OTP code",
        )
    ]
)


api_instance = SendSmsApi(api_client)

try:
    api_response:SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
    message_id = api_response.messages[0].message_id
    delivered_ornot = api_instance.get_outbound_sms_message_delivery_reports(message_id=message_id)
    print("API response made: %s\n" % api_response)
    print("Delivery report: %s\n" % delivered_ornot)
except ApiException as ex:
    print("Error occurred while trying to send SMS message.")
    print("Error status: %s\n" % ex.status)
    print("Error headers: %s\n" % ex.headers)
    print("Error body: %s\n" % ex.body)
    print("Error reason: %s\n" % ex.reason)


