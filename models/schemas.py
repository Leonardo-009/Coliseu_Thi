from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    age: int
    phone: str
    year_to_go_japan: int
    school: str
    interests: List[str]
    plans_in_japan: str
    roommate_preference_age: int
    gender: str
    about: Optional[str] = None
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    name: str
    age: int
    phone: str
    year_to_go_japan: int
    school: str
    interests: List[str]
    plans_in_japan: str
    roommate_preference_age: int
    gender: str
    about: Optional[str] = None
    email: str
