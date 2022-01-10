from typing import List

from pydantic import parse_obj_as
from security_scheduling.models.integration_pd import ScheduleModel


def validate_data(data: list):
    results = parse_obj_as(List[ScheduleModel], data)