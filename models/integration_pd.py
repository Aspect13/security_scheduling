from typing import Optional, List

from pydantic import BaseModel, AnyUrl
from pydantic.class_validators import validator
from pydantic.fields import ModelField
from pylon.core.tools import log

import croniter


class ScheduleModel(BaseModel):
    cron: str

    @validator('cron')
    def validate_cron(cls, value: list, field: ModelField):
        assert croniter.is_valid(value), 'Cron expression is invalid'
        return value
