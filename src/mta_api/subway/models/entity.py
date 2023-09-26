from enum import Enum
from datetime import date, datetime, time
from typing import Optional

from pydantic import BaseModel

from mta_api.gtfs import gtfs_realtime_pb2, nyct_subway_pb2

class Entity(Enum):
    Alert = 'alert'
    TripUpdate = 'trip_update'
    Vehicle = 'vehicle'


class Direction(Enum):
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'


class TripDescriptor(BaseModel):
    train_id: str
    start_datetime: datetime
    route_id: str


class NyctTripDescriptor(TripDescriptor):
    train_id: Optional[str]
    is_assigned: Optional[bool]
    direction: Optional[Direction]


class TripUpdate(BaseModel):
    trip: NyctTripDescriptor


def convert_trip_descriptor(
    trip_descriptor: gtfs_realtime_pb2.TripDescriptor
) -> NyctTripDescriptor:
    nyct_trip_descriptor = trip_descriptor.Extensions[
        nyct_subway_pb2.nyct_trip_descriptor
    ]
    if nyct_trip_descriptor.HasField('is_assigned'):
        is_assigned = nyct_trip_descriptor.is_assigned
    else:
        is_assigned = None

    if nyct_trip_descriptor.HasField('train_id'):
        train_id = nyct_trip_descriptor.train_id
    else:
        train_id = None

    if nyct_trip_descriptor.HasField('direction'):
        direction = Direction(nyct_trip_descriptor.direction)
    else:
        direction = None

    return NyctTripDescriptor(
        trip_id=trip_descriptor.trip_id,
        start_datetime=(
            datetime.combine(
                date.fromisoformat(trip_descriptor.start_date),
                time.fromisoformat(trip_descriptor.start_time)
            )
        ),
        route_id=trip_descriptor.route_id,
        is_assigned=is_assigned,
        train_id=train_id,
        direction=direction
    )


def convert_trip_update(
        trip_update: gtfs_realtime_pb2.TripUpdate
) -> TripUpdate:
    return TripUpdate(
        trip=convert_trip_descriptor(trip_update.trip),
    )
