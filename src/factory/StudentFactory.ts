import { Student } from "../models/Student";
import { Gender, TypeOfIdentifications } from "../models/enums";

/**
 * Represents the data structure for creating a new student.
 */
export type studentCreate = {
  typeOfIdentification: TypeOfIdentifications;
  identification: string;
  firstName: string;
  lastName: string;
  birthdate: Date;
  gender: Gender;
  address?: string;
  email?: string;
  phone?: string;
  currentGrade: string;
};

/**
 * Represents the data structure for updating an existing student.
 */
export type studentUpdate = {
  id: string;
  typeOfIdentification: TypeOfIdentifications;
  identification: string;
  firstName: string;
  lastName: string;
  birthdate: Date;
  gender: Gender;
  address?: string;
  email?: string;
  phone?: string;
  currentGrade: string;
};

/**
 * Represents the data structure for deleting a student.
 */
export type studentDelete = {
  id: string;
  typeOfIdentification: TypeOfIdentifications;
  identification: string;
  firstName: string;
  lastName: string;
  birthdate: Date;
  gender: Gender;
  address: string;
  email: string;
  phone: string;
  currentGrade: string;
};

/**
 * Represents the data structure for listing student information.
 */
export type studentList = {
  id: string;
  typeOfIdentification: TypeOfIdentifications;
  identification: string;
  firstName: string;
  lastName: string;
  birthdate: Date;
  gender: Gender;
  address?: string;
  email?: string;
  phone?: string;
  currentGrade: string;
};

/**
 * Factory class for creating Student objects.
 */
export class StudentFactory {
  /**
   * Creates a new Student object based on the provided data.
   *
   * @param {studentCreate} data - The data for creating the student.
   * @returns {Student} A new instance of the Student class.
   * @throws {Error} If required fields are empty or if the birthdate is not a valid date.
   */
  static create(data: studentCreate): Student {
    if (
      data.identification.replace(/ /g, "") === "" ||
      data.firstName.replace(/ /g, "") === "" ||
      data.lastName.replace(/ /g, "") === "" ||
      data.currentGrade.replace(/ /g, "") === ""
    ) {
      throw new Error("The required fields cannot be empty.");
    }

    // Validar que el campo birthdate sea una fecha válida
    if (isNaN(data.birthdate.getTime())) {
      throw new Error("The birthdate field must be a valid date.");
    }

    return new Student(
      undefined,
      data.typeOfIdentification,
      data.identification,
      data.firstName,
      data.lastName,
      data.birthdate,
      data.gender,
      data.address,
      data.email,
      data.phone,
      data.currentGrade
    );
  }
}
