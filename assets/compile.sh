#!/bin/sh

# General Transit Feed Specification (GTFS): https://developers.google.com/transit/gtfs-realtime/
# source: https://gtfs.org/realtime/proto/
protoc --python_out=pyi_out:./ ./gtfs-realtime.proto

# NYCT subway extensions: https://api.mta.info/GTFS.pdf
# source: https://api.mta.info/nyct-subway.proto.txt
protoc --python_out=pyi_out:./ ./nyct-subway.proto
