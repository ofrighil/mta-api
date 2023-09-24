from typing import NamedTuple

from mta_api.subway.service import Service

class Line(NamedTuple):
    name: str
    services: set

eighth_avenue_line = Line(
    'IND Eighth Avenue Line',
    frozenset((Service.A, Service.C, Service.E))
)
sixth_avenue_line = Line(
    'IND Sixth Avenue Line',
    frozenset((Service.B, Service.D, Service.F, Service.M))
)
