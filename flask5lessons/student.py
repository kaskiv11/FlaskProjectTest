from __future__ import annotations
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalc import Base
from associates import student_group_assoc_table
from group import Group

class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(String(250))

    groups: Mapped[List[Group]] = relationship(secondary=student_group_assoc_table)

    def __repr__(self):
        return f"<Student:{self.surname} {self.name} - {self.age}>"