from enum import Enum
from datetime import date, datetime, time
from typing import Optional

from pydantic import BaseModel

from mta_api.gtfs import gtfs_realtime_pb2, nyct_subway_pb2

class FeedEntity(Enum):
    Alert = 'alert'
    TripUpdate = 'trip_update'
    Vehicle = 'vehicle'


class Direction(Enum):
    NORTH = 1
    # EAST = 2
    SOUTH = 3
    # West = 4


class TripDescriptor(BaseModel):
    train_id: str
    start_datetime: datetime
    route_id: str


class NyctTripDescriptor(TripDescriptor):
    train_id: Optional[str]
    is_assigned: Optional[bool]
    direction: Optional[Direction]


class StopTimeUpdate(BaseModel):
    stop_id: str
    arrival: datetime
    departure: datetime
    #departure_occupancy_stats: str


class NyctStopTimeUpdate(StopTimeUpdate):
    scheduled_track: Optional[str]
    actual_track: Optional[str]


class TripUpdate(BaseModel):
    trip: NyctTripDescriptor
    stop_time_update: tuple[NyctStopTimeUpdate, ...]


def convert_trip_descriptor(
    trip_descriptor: gtfs_realtime_pb2.TripDescriptor
) -> NyctTripDescriptor:
    nyct_trip_descriptor: nyct_subway_pb2.NyctTripDescriptor = \
        trip_descriptor.Extensions[nyct_subway_pb2.nyct_trip_descriptor]

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


def convert_stop_time_update(
    stop_time_update: gtfs_realtime_pb2.TripUpdate.StopTimeUpdate
) -> NyctStopTimeUpdate:
    nyct_stop_time_update: nyct_subway_pb2.NyctStopTimeUpdate = \
        stop_time_update.Extensions[nyct_subway_pb2.nyct_stop_time_update]

    if nyct_stop_time_update.HasField('scheduled_track'):
        scheduled_track = nyct_stop_time_update.scheduled_track
    else:
        scheduled_track = None

    if nyct_stop_time_update.HasField('actual_track'):
        actual_track = nyct_stop_time_update.actual_track
    else:
        actual_track = None


    return NyctStopTimeUpdate(
        stop_id=stop_time_update.stop_id,
        arrival=datetime.fromtimestamp(stop_time_update.arrival.time),
        departure=datetime.fromtimestamp(stop_time_update.departure.time),
        scheduled_track=scheduled_track,
        actual_track=actual_track
    )


def convert_trip_update(
    trip_update: gtfs_realtime_pb2.TripUpdate
) -> TripUpdate:
    return TripUpdate(
        trip=convert_trip_descriptor(trip_update.trip),
        stop_time_update=tuple(
            map(convert_stop_time_update, trip_update.stop_time_update)
        )
    )
