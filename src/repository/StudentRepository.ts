import { Student } from "../models/Student";

/**
 * Repository class for handling student-related operations.
 */
export class StudentRepository {
  /**
   * Creates a new student.
   * @param {Student} student - The student object to be created.
   * @throws {Error} If an error occurs during the creation process.
   */
  static async create(student: Student) {
    try {
      const res = await fetch(
        `${window.location.origin}/SGE/api/student.json`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(student.getDataObject()),
        }
      );
      if (!res.ok) {
        throw new Error("Failed to create student: " + res.statusText + res);
      }
      const newStudent = await res.json();
    } catch (error) {
      throw error; // Re-throw the error to be caught in the calling function
    }
  }
}
