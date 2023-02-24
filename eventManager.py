event_subscriber_record = dict()


def signal_subscribe(signal: str, recipient):
    # If the event we want to subscribe to is not registered already, add it to the dict as an array
    # We then add the functions subscribing to this event into that array
    if not signal in event_subscriber_record:
        event_subscriber_record[signal] = []
    event_subscriber_record[signal].append(recipient)


def signal_send(signal: str, data):
    if not signal in event_subscriber_record:
        print("Error, no such signal to send")
        return
    for function in event_subscriber_record[signal]:
        function(data)