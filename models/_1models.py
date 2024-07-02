from beanie import Document
from pydantic import BaseModel, Field
from typing import List, Optional

class User(Document):
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
    hashed_password: str

    class Settings:
        collection = "users"
