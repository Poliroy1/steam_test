from pydantic import BaseModel, ConfigDict, Field


class GradeStatisticResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0)

    min: int | None = None
    max: int | None = None
    avg: float | None = None
