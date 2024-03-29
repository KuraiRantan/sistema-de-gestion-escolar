import { formatDate } from "../utils/manageDate";
import Person from "./Person";
import { Gender, TypeOfIdentifications } from "./enums";

/**
 * Represents a student, inheriting properties from the Person class.
 */
export class Student extends Person {
  /**
   * Creates an instance of Student.
   *
   * @param {number | undefined} _id - The student's ID.
   * @param {TypeOfIdentifications | undefined} typeOfIdentification - The type of identification of the student.
   * @param {string | undefined} identification - The identification number of the student.
   * @param {string | undefined} firstName - The first name of the student.
   * @param {string | undefined} lastName - The last name of the student.
   * @param {Date | undefined} birthdate - The date of birth of the student.
   * @param {Gender | undefined} gender - The gender of the student.
   * @param {string | undefined} address - The address of the student.
   * @param {string | undefined} email - The email of the student.
   * @param {string | undefined} phone - The phone number of the student.
   * @param {string | undefined} _currentGrade - The current grade of the student.
   */
  constructor(
    private _id?: number | undefined,
    typeOfIdentification?: TypeOfIdentifications | undefined,
    identification?: string | undefined,
    firstName?: string | undefined,
    lastName?: string | undefined,
    birthdate?: Date | undefined,
    gender?: Gender | undefined,
    address?: string | undefined,
    email?: string | undefined,
    phone?: string | undefined,
    private _currentGrade?: string | undefined
  ) {
    super(
      typeOfIdentification,
      identification,
      firstName,
      lastName,
      birthdate,
      gender,
      address,
      email,
      phone
    );
  }

  /**
   * Gets the student's ID.
   *
   * @returns {number | undefined} The student's ID.
   */
  get id(): number | undefined {
    return this._id;
  }

  /**
   * Sets the student's ID.
   *
   * @param {number | undefined} value - The student's ID.
   */
  set id(value: number | undefined) {
    this._id = value;
  }

  /**
   * Gets the current grade of the student.
   *
   * @returns {string | undefined} The current grade of the student.
   */
  get currentGrade(): string | undefined {
    return this._currentGrade;
  }

  /**
   * Sets the current grade of the student.
   *
   * @param {string | undefined} value - The current grade of the student.
   */
  set currentGrade(value: string | undefined) {
    this._currentGrade = value;
  }

  /**
   * Validates the student's data.
   *
   * @returns {boolean} True if the student's data is valid, otherwise false.
   */
  validate(): boolean {
    return true;
  }

  /**
   * Gets the student data as an object.
   *
   * @returns {Object} An object containing the student data.
   * - id: The student's ID.
   * - type_of_identification: The type of identification of the student.
   * - identification: The identification number of the student.
   * - first_name: The first name of the student.
   * - last_name: The last name of the student.
   * - birthdate: The date of birth of the student.
   * - gender: The gender of the student.
   * - address: The address of the student.
   * - email: The email of the student.
   * - phone: The phone number of the student.
   * - current_grade: The current grade of the student.
   */
  getDataObject(): {
    id: number | undefined;
    type_of_identification: TypeOfIdentifications | undefined;
    identification: string | undefined;
    first_name: string | undefined;
    last_name: string | undefined;
    birthdate: string | undefined;
    gender: Gender | undefined;
    address: string | undefined;
    email: string | undefined;
    phone: string | undefined;
    current_grade: string | undefined;
  } {
    return {
      id: this._id,
      type_of_identification: this._typeOfIdentification,
      identification: this._identification,
      first_name: this._firstName,
      last_name: this._lastName,
      birthdate:
        this._birthdate != undefined ? formatDate(this._birthdate) : undefined,
      gender: this._gender,
      address: this._address,
      email: this._email,
      phone: this._phone,
      current_grade: this._currentGrade,
    };
  }
}
