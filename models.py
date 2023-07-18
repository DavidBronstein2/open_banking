from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    date_of_birth: datetime
    phone_number: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted: Optional[bool] = None