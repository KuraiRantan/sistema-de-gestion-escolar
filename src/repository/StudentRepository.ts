import { Student } from "../models/Student";

export class StudentRepository {
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
