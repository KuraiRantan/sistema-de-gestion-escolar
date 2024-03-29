// Person model
/**
 * Enum representing different types of identifications.
 * @enum {string}
 */
export enum TypeOfIdentifications {
  IC = "Identity Card",
  CC = "Citizenship Card",
  CR = "Civil Registration",
  FI = "Foreigner Id",
}

/**
 * Enum representing different genders.
 * @enum {string}
 */
export enum Gender {
  M = "Male",
  F = "Female",
  O = "Other",
}

// Attendance model
/**
 * Enum representing attendance statuses.
 * @enum {string}
 */
export enum AttendanceStatus {
  PRESENT = "Present",
  ABSENT = "Absent",
  LATE = "Late",
}
