from enum import Enum

class TypeOfIdentifications(Enum):
    """Lists the identification types available."""
    IC = "Identity Card"
    CC = "Citizenship Card"
    CR = "Civil Registration"
    FI = "Foreigner Id"

class Gender(Enum):
    """Lists the types of genres available."""
    M = "Male"
    F = "Female"
    O = "Other"

class AttendanceStatus(Enum):
    """Lists possible states for assistance."""
    UNKNOWN = "Unknown"
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
