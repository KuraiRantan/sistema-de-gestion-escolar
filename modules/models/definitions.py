from enum import Enum

class TypeOfIdentifications(Enum):
    IC = "Identity Card"
    CC = "Citizenship Card"
    CR = "Civil Registration"
    FI = "Foreigner Id"

class Gender(Enum):
    M = "Male"
    F = "Female"
    O = "Other"

class AttendanceStatus(Enum):
    UNKNOWN = "Unknown"
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
