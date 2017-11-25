def send_sms(message):
    import time
    from sinchsms import SinchSMS
    number = '+447948050817'

    client = SinchSMS('0a0cb8f3-829b-4613-b34c-f96ed8a94978', 'ATOI/bqb0E2XJaSv1KOQ/Q==')

    print("Sending '%s' to %s" % (message, number))
    response = client.send_message(number, message)
    message_id = response['messageId']
    response = client.check_status(message_id)
    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)
    print(response['status'])

