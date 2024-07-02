from datetime import datetime
from enum import Enum
from typing import Optional, List
from sqlmodel import JSON, SQLModel, Field, Relationship
from pydantic import EmailStr

class Sex(int, Enum):
    others = 0
    male = 1
    female = 2

class School(SQLModel, table=True):
    __tablename__ = "schools" 
    
    id: int = Field(default=None, primary_key=True)
    name: str

    student_groups: List["StudentGroup"] = Relationship(back_populates="school")

class StudentGroup(SQLModel, table=True):
    __tablename__ = "student_groups"  
    
    id: int = Field(default=None, primary_key=True)
    year: int

    school_id: int = Field(foreign_key="schools.id")
    school: School = Relationship(back_populates="student_groups")

    invite_keys: List["InviteKey"] = Relationship(back_populates="student_group")
    users: List["User"] = Relationship(back_populates="student_group")

class InviteKey(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    key: str

    student_group_id: int = Field(foreign_key="student_groups.id")
    student_group: StudentGroup = Relationship(back_populates="invite_keys")

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr
    password: str
    idade: int
    telephone: str
    school: str
    interest: str
    year_going_by_japan: datetime
    sex: Sex
    bio: str

    student_group_id: int = Field(foreign_key="student_groups.id")
    student_group: StudentGroup = Relationship(back_populates="users")