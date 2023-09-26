from datetime import datetime, tzinfo

from pydantic import BaseModel

from mta_api.gtfs import gtfs_realtime_pb2, nyct_subway_pb2

class TimeRange(BaseModel):
    # start: datetime = datetime.min
    end: datetime


class TripReplacementPeriod(BaseModel):
    route_id: str
    replacement_period: TimeRange


class FeedHeader(BaseModel):
    gtfs_realtime_version: str
    timestamp: datetime 


class NyctFeedHeader(FeedHeader):
    nyct_subway_version: str
    trip_replacement_period: tuple[TripReplacementPeriod, ...]


def map_trip_replacement_period(
    trip_replacement_period: nyct_subway_pb2.TripReplacementPeriod
) -> TripReplacementPeriod:
    return TripReplacementPeriod(
        route_id=trip_replacement_period.route_id,
        replacement_period=TimeRange(
            end=datetime.fromtimestamp(
                trip_replacement_period.replacement_period.end
            )
        )
    )


def convert_header(
        gtfs_header: gtfs_realtime_pb2.FeedHeader
) -> NyctFeedHeader:
    nyct_header = gtfs_header.Extensions[nyct_subway_pb2.nyct_feed_header]
    return NyctFeedHeader(
        gtfs_realtime_version=gtfs_header.gtfs_realtime_version,
        timestamp=datetime.fromtimestamp(gtfs_header.timestamp),
        nyct_subway_version=nyct_header.nyct_subway_version,
        trip_replacement_period=tuple(
            map(
                map_trip_replacement_period,
                nyct_header.trip_replacement_period
            )
        )
    )

