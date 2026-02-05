from pydantic import BaseModel, ConfigDict, Field
from typing import ClassVar


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")
    MIN_GRADE: ClassVar[int] = 1
    MAX_GRADE: ClassVar[int] = 5

    teacher_id: int
    student_id: int
    grade: int = Field(ge=MIN_GRADE, le=MAX_GRADE)
