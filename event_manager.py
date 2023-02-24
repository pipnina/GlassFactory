from typing import Callable
from enum import Enum

class Event(Enum):
    ComponentChanged = 1

event_subscriber_record = dict()


def subscribe(event: Event, callback: Callable):
    # If the event we want to subscribe to is not registered already, add it to the dict as an array
    # We then add the functions subscribing to this event into that array
    if not event in event_subscriber_record:
        event_subscriber_record[event] = []
    event_subscriber_record[event].append(callback)


def raise_event(event: Event, **kwargs):
    if not event in event_subscriber_record:
        print(f"Tried to raise event {event} but it doesn't exist!")
        return
    for function in event_subscriber_record[event]:
        function(**kwargs)