from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Alert(_message.Message):
    __slots__ = ["active_period", "cause", "cause_detail", "description_text", "effect", "effect_detail", "header_text", "image", "image_alternative_text", "informed_entity", "severity_level", "tts_description_text", "tts_header_text", "url"]
    class Cause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class SeverityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCESSIBILITY_ISSUE: Alert.Effect
    ACCIDENT: Alert.Cause
    ACTIVE_PERIOD_FIELD_NUMBER: ClassVar[int]
    ADDITIONAL_SERVICE: Alert.Effect
    CAUSE_DETAIL_FIELD_NUMBER: ClassVar[int]
    CAUSE_FIELD_NUMBER: ClassVar[int]
    CONSTRUCTION: Alert.Cause
    DEMONSTRATION: Alert.Cause
    DESCRIPTION_TEXT_FIELD_NUMBER: ClassVar[int]
    DETOUR: Alert.Effect
    EFFECT_DETAIL_FIELD_NUMBER: ClassVar[int]
    EFFECT_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    HEADER_TEXT_FIELD_NUMBER: ClassVar[int]
    HOLIDAY: Alert.Cause
    IMAGE_ALTERNATIVE_TEXT_FIELD_NUMBER: ClassVar[int]
    IMAGE_FIELD_NUMBER: ClassVar[int]
    INFO: Alert.SeverityLevel
    INFORMED_ENTITY_FIELD_NUMBER: ClassVar[int]
    MAINTENANCE: Alert.Cause
    MEDICAL_EMERGENCY: Alert.Cause
    MODIFIED_SERVICE: Alert.Effect
    NO_EFFECT: Alert.Effect
    NO_SERVICE: Alert.Effect
    OTHER_CAUSE: Alert.Cause
    OTHER_EFFECT: Alert.Effect
    POLICE_ACTIVITY: Alert.Cause
    REDUCED_SERVICE: Alert.Effect
    SEVERE: Alert.SeverityLevel
    SEVERITY_LEVEL_FIELD_NUMBER: ClassVar[int]
    SIGNIFICANT_DELAYS: Alert.Effect
    STOP_MOVED: Alert.Effect
    STRIKE: Alert.Cause
    TECHNICAL_PROBLEM: Alert.Cause
    TTS_DESCRIPTION_TEXT_FIELD_NUMBER: ClassVar[int]
    TTS_HEADER_TEXT_FIELD_NUMBER: ClassVar[int]
    UNKNOWN_CAUSE: Alert.Cause
    UNKNOWN_EFFECT: Alert.Effect
    UNKNOWN_SEVERITY: Alert.SeverityLevel
    URL_FIELD_NUMBER: ClassVar[int]
    WARNING: Alert.SeverityLevel
    WEATHER: Alert.Cause
    active_period: _containers.RepeatedCompositeFieldContainer[TimeRange]
    cause: Alert.Cause
    cause_detail: TranslatedString
    description_text: TranslatedString
    effect: Alert.Effect
    effect_detail: TranslatedString
    header_text: TranslatedString
    image: TranslatedImage
    image_alternative_text: TranslatedString
    informed_entity: _containers.RepeatedCompositeFieldContainer[EntitySelector]
    severity_level: Alert.SeverityLevel
    tts_description_text: TranslatedString
    tts_header_text: TranslatedString
    url: TranslatedString
    def __init__(self, active_period: Optional[Iterable[Union[TimeRange, Mapping]]] = ..., informed_entity: Optional[Iterable[Union[EntitySelector, Mapping]]] = ..., cause: Optional[Union[Alert.Cause, str]] = ..., effect: Optional[Union[Alert.Effect, str]] = ..., url: Optional[Union[TranslatedString, Mapping]] = ..., header_text: Optional[Union[TranslatedString, Mapping]] = ..., description_text: Optional[Union[TranslatedString, Mapping]] = ..., tts_header_text: Optional[Union[TranslatedString, Mapping]] = ..., tts_description_text: Optional[Union[TranslatedString, Mapping]] = ..., severity_level: Optional[Union[Alert.SeverityLevel, str]] = ..., image: Optional[Union[TranslatedImage, Mapping]] = ..., image_alternative_text: Optional[Union[TranslatedString, Mapping]] = ..., cause_detail: Optional[Union[TranslatedString, Mapping]] = ..., effect_detail: Optional[Union[TranslatedString, Mapping]] = ...) -> None: ...

class EntitySelector(_message.Message):
    __slots__ = ["agency_id", "direction_id", "route_id", "route_type", "stop_id", "trip"]
    AGENCY_ID_FIELD_NUMBER: ClassVar[int]
    DIRECTION_ID_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    ROUTE_ID_FIELD_NUMBER: ClassVar[int]
    ROUTE_TYPE_FIELD_NUMBER: ClassVar[int]
    STOP_ID_FIELD_NUMBER: ClassVar[int]
    TRIP_FIELD_NUMBER: ClassVar[int]
    agency_id: str
    direction_id: int
    route_id: str
    route_type: int
    stop_id: str
    trip: TripDescriptor
    def __init__(self, agency_id: Optional[str] = ..., route_id: Optional[str] = ..., route_type: Optional[int] = ..., trip: Optional[Union[TripDescriptor, Mapping]] = ..., stop_id: Optional[str] = ..., direction_id: Optional[int] = ...) -> None: ...

class FeedEntity(_message.Message):
    __slots__ = ["alert", "id", "is_deleted", "shape", "trip_update", "vehicle"]
    ALERT_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    ID_FIELD_NUMBER: ClassVar[int]
    IS_DELETED_FIELD_NUMBER: ClassVar[int]
    SHAPE_FIELD_NUMBER: ClassVar[int]
    TRIP_UPDATE_FIELD_NUMBER: ClassVar[int]
    VEHICLE_FIELD_NUMBER: ClassVar[int]
    alert: Alert
    id: str
    is_deleted: bool
    shape: Shape
    trip_update: TripUpdate
    vehicle: VehiclePosition
    def __init__(self, id: Optional[str] = ..., is_deleted: bool = ..., trip_update: Optional[Union[TripUpdate, Mapping]] = ..., vehicle: Optional[Union[VehiclePosition, Mapping]] = ..., alert: Optional[Union[Alert, Mapping]] = ..., shape: Optional[Union[Shape, Mapping]] = ...) -> None: ...

class FeedHeader(_message.Message):
    __slots__ = ["gtfs_realtime_version", "incrementality", "timestamp"]
    class Incrementality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DIFFERENTIAL: FeedHeader.Incrementality
    Extensions: _python_message._ExtensionDict
    FULL_DATASET: FeedHeader.Incrementality
    GTFS_REALTIME_VERSION_FIELD_NUMBER: ClassVar[int]
    INCREMENTALITY_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    gtfs_realtime_version: str
    incrementality: FeedHeader.Incrementality
    timestamp: int
    def __init__(self, gtfs_realtime_version: Optional[str] = ..., incrementality: Optional[Union[FeedHeader.Incrementality, str]] = ..., timestamp: Optional[int] = ...) -> None: ...

class FeedMessage(_message.Message):
    __slots__ = ["entity", "header"]
    ENTITY_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: ClassVar[int]
    entity: _containers.RepeatedCompositeFieldContainer[FeedEntity]
    header: FeedHeader
    def __init__(self, header: Optional[Union[FeedHeader, Mapping]] = ..., entity: Optional[Iterable[Union[FeedEntity, Mapping]]] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ["bearing", "latitude", "longitude", "odometer", "speed"]
    BEARING_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    LATITUDE_FIELD_NUMBER: ClassVar[int]
    LONGITUDE_FIELD_NUMBER: ClassVar[int]
    ODOMETER_FIELD_NUMBER: ClassVar[int]
    SPEED_FIELD_NUMBER: ClassVar[int]
    bearing: float
    latitude: float
    longitude: float
    odometer: float
    speed: float
    def __init__(self, latitude: Optional[float] = ..., longitude: Optional[float] = ..., bearing: Optional[float] = ..., odometer: Optional[float] = ..., speed: Optional[float] = ...) -> None: ...

class Shape(_message.Message):
    __slots__ = ["encoded_polyline", "shape_id"]
    ENCODED_POLYLINE_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    SHAPE_ID_FIELD_NUMBER: ClassVar[int]
    encoded_polyline: str
    shape_id: str
    def __init__(self, shape_id: Optional[str] = ..., encoded_polyline: Optional[str] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ["end", "start"]
    END_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    START_FIELD_NUMBER: ClassVar[int]
    end: int
    start: int
    def __init__(self, start: Optional[int] = ..., end: Optional[int] = ...) -> None: ...

class TranslatedImage(_message.Message):
    __slots__ = ["localized_image"]
    class LocalizedImage(_message.Message):
        __slots__ = ["language", "media_type", "url"]
        Extensions: _python_message._ExtensionDict
        LANGUAGE_FIELD_NUMBER: ClassVar[int]
        MEDIA_TYPE_FIELD_NUMBER: ClassVar[int]
        URL_FIELD_NUMBER: ClassVar[int]
        language: str
        media_type: str
        url: str
        def __init__(self, url: Optional[str] = ..., media_type: Optional[str] = ..., language: Optional[str] = ...) -> None: ...
    Extensions: _python_message._ExtensionDict
    LOCALIZED_IMAGE_FIELD_NUMBER: ClassVar[int]
    localized_image: _containers.RepeatedCompositeFieldContainer[TranslatedImage.LocalizedImage]
    def __init__(self, localized_image: Optional[Iterable[Union[TranslatedImage.LocalizedImage, Mapping]]] = ...) -> None: ...

class TranslatedString(_message.Message):
    __slots__ = ["translation"]
    class Translation(_message.Message):
        __slots__ = ["language", "text"]
        Extensions: _python_message._ExtensionDict
        LANGUAGE_FIELD_NUMBER: ClassVar[int]
        TEXT_FIELD_NUMBER: ClassVar[int]
        language: str
        text: str
        def __init__(self, text: Optional[str] = ..., language: Optional[str] = ...) -> None: ...
    Extensions: _python_message._ExtensionDict
    TRANSLATION_FIELD_NUMBER: ClassVar[int]
    translation: _containers.RepeatedCompositeFieldContainer[TranslatedString.Translation]
    def __init__(self, translation: Optional[Iterable[Union[TranslatedString.Translation, Mapping]]] = ...) -> None: ...

class TripDescriptor(_message.Message):
    __slots__ = ["direction_id", "route_id", "schedule_relationship", "start_date", "start_time", "trip_id"]
    class ScheduleRelationship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDED: TripDescriptor.ScheduleRelationship
    CANCELED: TripDescriptor.ScheduleRelationship
    DELETED: TripDescriptor.ScheduleRelationship
    DIRECTION_ID_FIELD_NUMBER: ClassVar[int]
    DUPLICATED: TripDescriptor.ScheduleRelationship
    Extensions: _python_message._ExtensionDict
    REPLACEMENT: TripDescriptor.ScheduleRelationship
    ROUTE_ID_FIELD_NUMBER: ClassVar[int]
    SCHEDULED: TripDescriptor.ScheduleRelationship
    SCHEDULE_RELATIONSHIP_FIELD_NUMBER: ClassVar[int]
    START_DATE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    TRIP_ID_FIELD_NUMBER: ClassVar[int]
    UNSCHEDULED: TripDescriptor.ScheduleRelationship
    direction_id: int
    route_id: str
    schedule_relationship: TripDescriptor.ScheduleRelationship
    start_date: str
    start_time: str
    trip_id: str
    def __init__(self, trip_id: Optional[str] = ..., route_id: Optional[str] = ..., direction_id: Optional[int] = ..., start_time: Optional[str] = ..., start_date: Optional[str] = ..., schedule_relationship: Optional[Union[TripDescriptor.ScheduleRelationship, str]] = ...) -> None: ...

class TripUpdate(_message.Message):
    __slots__ = ["delay", "stop_time_update", "timestamp", "trip", "trip_properties", "vehicle"]
    class StopTimeEvent(_message.Message):
        __slots__ = ["delay", "time", "uncertainty"]
        DELAY_FIELD_NUMBER: ClassVar[int]
        Extensions: _python_message._ExtensionDict
        TIME_FIELD_NUMBER: ClassVar[int]
        UNCERTAINTY_FIELD_NUMBER: ClassVar[int]
        delay: int
        time: int
        uncertainty: int
        def __init__(self, delay: Optional[int] = ..., time: Optional[int] = ..., uncertainty: Optional[int] = ...) -> None: ...
    class StopTimeUpdate(_message.Message):
        __slots__ = ["arrival", "departure", "departure_occupancy_status", "schedule_relationship", "stop_id", "stop_sequence", "stop_time_properties"]
        class ScheduleRelationship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class StopTimeProperties(_message.Message):
            __slots__ = ["assigned_stop_id"]
            ASSIGNED_STOP_ID_FIELD_NUMBER: ClassVar[int]
            Extensions: _python_message._ExtensionDict
            assigned_stop_id: str
            def __init__(self, assigned_stop_id: Optional[str] = ...) -> None: ...
        ARRIVAL_FIELD_NUMBER: ClassVar[int]
        DEPARTURE_FIELD_NUMBER: ClassVar[int]
        DEPARTURE_OCCUPANCY_STATUS_FIELD_NUMBER: ClassVar[int]
        Extensions: _python_message._ExtensionDict
        NO_DATA: TripUpdate.StopTimeUpdate.ScheduleRelationship
        SCHEDULED: TripUpdate.StopTimeUpdate.ScheduleRelationship
        SCHEDULE_RELATIONSHIP_FIELD_NUMBER: ClassVar[int]
        SKIPPED: TripUpdate.StopTimeUpdate.ScheduleRelationship
        STOP_ID_FIELD_NUMBER: ClassVar[int]
        STOP_SEQUENCE_FIELD_NUMBER: ClassVar[int]
        STOP_TIME_PROPERTIES_FIELD_NUMBER: ClassVar[int]
        UNSCHEDULED: TripUpdate.StopTimeUpdate.ScheduleRelationship
        arrival: TripUpdate.StopTimeEvent
        departure: TripUpdate.StopTimeEvent
        departure_occupancy_status: VehiclePosition.OccupancyStatus
        schedule_relationship: TripUpdate.StopTimeUpdate.ScheduleRelationship
        stop_id: str
        stop_sequence: int
        stop_time_properties: TripUpdate.StopTimeUpdate.StopTimeProperties
        def __init__(self, stop_sequence: Optional[int] = ..., stop_id: Optional[str] = ..., arrival: Optional[Union[TripUpdate.StopTimeEvent, Mapping]] = ..., departure: Optional[Union[TripUpdate.StopTimeEvent, Mapping]] = ..., departure_occupancy_status: Optional[Union[VehiclePosition.OccupancyStatus, str]] = ..., schedule_relationship: Optional[Union[TripUpdate.StopTimeUpdate.ScheduleRelationship, str]] = ..., stop_time_properties: Optional[Union[TripUpdate.StopTimeUpdate.StopTimeProperties, Mapping]] = ...) -> None: ...
    class TripProperties(_message.Message):
        __slots__ = ["shape_id", "start_date", "start_time", "trip_id"]
        Extensions: _python_message._ExtensionDict
        SHAPE_ID_FIELD_NUMBER: ClassVar[int]
        START_DATE_FIELD_NUMBER: ClassVar[int]
        START_TIME_FIELD_NUMBER: ClassVar[int]
        TRIP_ID_FIELD_NUMBER: ClassVar[int]
        shape_id: str
        start_date: str
        start_time: str
        trip_id: str
        def __init__(self, trip_id: Optional[str] = ..., start_date: Optional[str] = ..., start_time: Optional[str] = ..., shape_id: Optional[str] = ...) -> None: ...
    DELAY_FIELD_NUMBER: ClassVar[int]
    Extensions: _python_message._ExtensionDict
    STOP_TIME_UPDATE_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    TRIP_FIELD_NUMBER: ClassVar[int]
    TRIP_PROPERTIES_FIELD_NUMBER: ClassVar[int]
    VEHICLE_FIELD_NUMBER: ClassVar[int]
    delay: int
    stop_time_update: _containers.RepeatedCompositeFieldContainer[TripUpdate.StopTimeUpdate]
    timestamp: int
    trip: TripDescriptor
    trip_properties: TripUpdate.TripProperties
    vehicle: VehicleDescriptor
    def __init__(self, trip: Optional[Union[TripDescriptor, Mapping]] = ..., vehicle: Optional[Union[VehicleDescriptor, Mapping]] = ..., stop_time_update: Optional[Iterable[Union[TripUpdate.StopTimeUpdate, Mapping]]] = ..., timestamp: Optional[int] = ..., delay: Optional[int] = ..., trip_properties: Optional[Union[TripUpdate.TripProperties, Mapping]] = ...) -> None: ...

class VehicleDescriptor(_message.Message):
    __slots__ = ["id", "label", "license_plate", "wheelchair_accessible"]
    class WheelchairAccessible(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    Extensions: _python_message._ExtensionDict
    ID_FIELD_NUMBER: ClassVar[int]
    LABEL_FIELD_NUMBER: ClassVar[int]
    LICENSE_PLATE_FIELD_NUMBER: ClassVar[int]
    NO_VALUE: VehicleDescriptor.WheelchairAccessible
    UNKNOWN: VehicleDescriptor.WheelchairAccessible
    WHEELCHAIR_ACCESSIBLE: VehicleDescriptor.WheelchairAccessible
    WHEELCHAIR_ACCESSIBLE_FIELD_NUMBER: ClassVar[int]
    WHEELCHAIR_INACCESSIBLE: VehicleDescriptor.WheelchairAccessible
    id: str
    label: str
    license_plate: str
    wheelchair_accessible: VehicleDescriptor.WheelchairAccessible
    def __init__(self, id: Optional[str] = ..., label: Optional[str] = ..., license_plate: Optional[str] = ..., wheelchair_accessible: Optional[Union[VehicleDescriptor.WheelchairAccessible, str]] = ...) -> None: ...

class VehiclePosition(_message.Message):
    __slots__ = ["congestion_level", "current_status", "current_stop_sequence", "multi_carriage_details", "occupancy_percentage", "occupancy_status", "position", "stop_id", "timestamp", "trip", "vehicle"]
    class CongestionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class OccupancyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class VehicleStopStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class CarriageDetails(_message.Message):
        __slots__ = ["carriage_sequence", "id", "label", "occupancy_percentage", "occupancy_status"]
        CARRIAGE_SEQUENCE_FIELD_NUMBER: ClassVar[int]
        Extensions: _python_message._ExtensionDict
        ID_FIELD_NUMBER: ClassVar[int]
        LABEL_FIELD_NUMBER: ClassVar[int]
        OCCUPANCY_PERCENTAGE_FIELD_NUMBER: ClassVar[int]
        OCCUPANCY_STATUS_FIELD_NUMBER: ClassVar[int]
        carriage_sequence: int
        id: str
        label: str
        occupancy_percentage: int
        occupancy_status: VehiclePosition.OccupancyStatus
        def __init__(self, id: Optional[str] = ..., label: Optional[str] = ..., occupancy_status: Optional[Union[VehiclePosition.OccupancyStatus, str]] = ..., occupancy_percentage: Optional[int] = ..., carriage_sequence: Optional[int] = ...) -> None: ...
    CONGESTION: VehiclePosition.CongestionLevel
    CONGESTION_LEVEL_FIELD_NUMBER: ClassVar[int]
    CRUSHED_STANDING_ROOM_ONLY: VehiclePosition.OccupancyStatus
    CURRENT_STATUS_FIELD_NUMBER: ClassVar[int]
    CURRENT_STOP_SEQUENCE_FIELD_NUMBER: ClassVar[int]
    EMPTY: VehiclePosition.OccupancyStatus
    Extensions: _python_message._ExtensionDict
    FEW_SEATS_AVAILABLE: VehiclePosition.OccupancyStatus
    FULL: VehiclePosition.OccupancyStatus
    INCOMING_AT: VehiclePosition.VehicleStopStatus
    IN_TRANSIT_TO: VehiclePosition.VehicleStopStatus
    MANY_SEATS_AVAILABLE: VehiclePosition.OccupancyStatus
    MULTI_CARRIAGE_DETAILS_FIELD_NUMBER: ClassVar[int]
    NOT_ACCEPTING_PASSENGERS: VehiclePosition.OccupancyStatus
    NOT_BOARDABLE: VehiclePosition.OccupancyStatus
    NO_DATA_AVAILABLE: VehiclePosition.OccupancyStatus
    OCCUPANCY_PERCENTAGE_FIELD_NUMBER: ClassVar[int]
    OCCUPANCY_STATUS_FIELD_NUMBER: ClassVar[int]
    POSITION_FIELD_NUMBER: ClassVar[int]
    RUNNING_SMOOTHLY: VehiclePosition.CongestionLevel
    SEVERE_CONGESTION: VehiclePosition.CongestionLevel
    STANDING_ROOM_ONLY: VehiclePosition.OccupancyStatus
    STOPPED_AT: VehiclePosition.VehicleStopStatus
    STOP_AND_GO: VehiclePosition.CongestionLevel
    STOP_ID_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    TRIP_FIELD_NUMBER: ClassVar[int]
    UNKNOWN_CONGESTION_LEVEL: VehiclePosition.CongestionLevel
    VEHICLE_FIELD_NUMBER: ClassVar[int]
    congestion_level: VehiclePosition.CongestionLevel
    current_status: VehiclePosition.VehicleStopStatus
    current_stop_sequence: int
    multi_carriage_details: _containers.RepeatedCompositeFieldContainer[VehiclePosition.CarriageDetails]
    occupancy_percentage: int
    occupancy_status: VehiclePosition.OccupancyStatus
    position: Position
    stop_id: str
    timestamp: int
    trip: TripDescriptor
    vehicle: VehicleDescriptor
    def __init__(self, trip: Optional[Union[TripDescriptor, Mapping]] = ..., vehicle: Optional[Union[VehicleDescriptor, Mapping]] = ..., position: Optional[Union[Position, Mapping]] = ..., current_stop_sequence: Optional[int] = ..., stop_id: Optional[str] = ..., current_status: Optional[Union[VehiclePosition.VehicleStopStatus, str]] = ..., timestamp: Optional[int] = ..., congestion_level: Optional[Union[VehiclePosition.CongestionLevel, str]] = ..., occupancy_status: Optional[Union[VehiclePosition.OccupancyStatus, str]] = ..., occupancy_percentage: Optional[int] = ..., multi_carriage_details: Optional[Iterable[Union[VehiclePosition.CarriageDetails, Mapping]]] = ...) -> None: ...
