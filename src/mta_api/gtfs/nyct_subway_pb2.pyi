import gtfs_realtime_pb2 as _gtfs_realtime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor
NYCT_FEED_HEADER_FIELD_NUMBER: ClassVar[int]
NYCT_STOP_TIME_UPDATE_FIELD_NUMBER: ClassVar[int]
NYCT_TRIP_DESCRIPTOR_FIELD_NUMBER: ClassVar[int]
nyct_feed_header: _descriptor.FieldDescriptor
nyct_stop_time_update: _descriptor.FieldDescriptor
nyct_trip_descriptor: _descriptor.FieldDescriptor

class NyctFeedHeader(_message.Message):
    __slots__ = ["nyct_subway_version", "trip_replacement_period"]
    NYCT_SUBWAY_VERSION_FIELD_NUMBER: ClassVar[int]
    TRIP_REPLACEMENT_PERIOD_FIELD_NUMBER: ClassVar[int]
    nyct_subway_version: str
    trip_replacement_period: _containers.RepeatedCompositeFieldContainer[TripReplacementPeriod]
    def __init__(self, nyct_subway_version: Optional[str] = ..., trip_replacement_period: Optional[Iterable[Union[TripReplacementPeriod, Mapping]]] = ...) -> None: ...

class NyctStopTimeUpdate(_message.Message):
    __slots__ = ["actual_track", "scheduled_track"]
    ACTUAL_TRACK_FIELD_NUMBER: ClassVar[int]
    SCHEDULED_TRACK_FIELD_NUMBER: ClassVar[int]
    actual_track: str
    scheduled_track: str
    def __init__(self, scheduled_track: Optional[str] = ..., actual_track: Optional[str] = ...) -> None: ...

class NyctTripDescriptor(_message.Message):
    __slots__ = ["direction", "is_assigned", "train_id"]
    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DIRECTION_FIELD_NUMBER: ClassVar[int]
    EAST: NyctTripDescriptor.Direction
    IS_ASSIGNED_FIELD_NUMBER: ClassVar[int]
    NORTH: NyctTripDescriptor.Direction
    SOUTH: NyctTripDescriptor.Direction
    TRAIN_ID_FIELD_NUMBER: ClassVar[int]
    WEST: NyctTripDescriptor.Direction
    direction: NyctTripDescriptor.Direction
    is_assigned: bool
    train_id: str
    def __init__(self, train_id: Optional[str] = ..., is_assigned: bool = ..., direction: Optional[Union[NyctTripDescriptor.Direction, str]] = ...) -> None: ...

class TripReplacementPeriod(_message.Message):
    __slots__ = ["replacement_period", "route_id"]
    REPLACEMENT_PERIOD_FIELD_NUMBER: ClassVar[int]
    ROUTE_ID_FIELD_NUMBER: ClassVar[int]
    replacement_period: _gtfs_realtime_pb2.TimeRange
    route_id: str
    def __init__(self, route_id: Optional[str] = ..., replacement_period: Optional[Union[_gtfs_realtime_pb2.TimeRange, Mapping]] = ...) -> None: ...
