from pydantic import BaseModel
import enum

class RolesEnum(str, enum.Enum):
    USER = "User"
    MANAGER = "Manager"
    ADMIN = "ADMIN"


class User(BaseModel):
    username: str
    password: str
    role: RolesEnum

    class Config:
        orm_mode = True
        from_attributes=True