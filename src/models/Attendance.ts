import Classroom from "./Classroom";
import { Student } from "./Student";
import Subject from "./Subject";
import { AttendanceStatus } from "./enums";

/**
 * Represents attendance information for a student in a particular class.
 */
export default class Attendance {
  /**
   * Creates an instance of Attendance.
   * @param {number | undefined} _id - The ID of the attendance record.
   * @param {Student | undefined} _student - The student associated with the attendance record.
   * @param {Subject | undefined} _subject - The subject associated with the attendance record.
   * @param {Classroom | undefined} _classroom - The classroom associated with the attendance record.
   * @param {string | undefined} _grade - The grade of the student.
   * @param {Date | undefined} _attendanceDate - The date of the attendance record.
   * @param {AttendanceStatus | undefined} _status - The status of the attendance record.
   * @param {string | undefined} _notes - Additional notes related to the attendance record.
   */
  constructor(
    private _id?: number | undefined,
    private _student?: Student | undefined,
    private _subject?: Subject | undefined,
    private _classroom?: Classroom | undefined,
    private _grade?: string | undefined,
    private _attendanceDate?: Date | undefined,
    private _status?: AttendanceStatus | undefined,
    private _notes?: string | undefined
  ) {}

  /**
   * Gets the ID of the attendance record.
   *
   * @returns {number | undefined} The ID of the attendance record.
   */
  get id(): number | undefined {
    return this._id;
  }

  /**
   * Sets the ID of the attendance record.
   *
   * @param {number | undefined} value - The ID of the attendance record.
   */
  set id(value: number | undefined) {
    this._id = value;
  }

  /**
   * Gets the student associated with the attendance record.
   *
   * @returns {Student | undefined} The student associated with the attendance record.
   */
  get student(): Student | undefined {
    return this._student;
  }

  /**
   * Sets the student associated with the attendance record.
   *
   * @param {Student | undefined} value - The student associated with the attendance record.
   */
  set student(value: Student | undefined) {
    this._student = value;
  }

  /**
   * Gets the subject associated with the attendance record.
   *
   * @returns {Subject | undefined} The subject associated with the attendance record.
   */
  get subject(): Subject | undefined {
    return this._subject;
  }

  /**
   * Sets the subject associated with the attendance record.
   *
   * @param {Subject | undefined} value - The subject associated with the attendance record.
   */
  set subject(value: Subject | undefined) {
    this._subject = value;
  }

  /**
   * Gets the classroom associated with the attendance record.
   *
   * @returns {Classroom | undefined} The classroom associated with the attendance record.
   */
  get classroom(): Classroom | undefined {
    return this._classroom;
  }

  /**
   * Sets the classroom associated with the attendance record.
   *
   * @param {Classroom | undefined} value - The classroom associated with the attendance record.
   */
  set classroom(value: Classroom | undefined) {
    this._classroom = value;
  }

  /**
   * Gets the grade of the student.
   *
   * @returns {string | undefined} The grade of the student.
   */
  get grade(): string | undefined {
    return this._grade;
  }

  /**
   * Sets the grade of the student.
   *
   * @param {string | undefined} value - The grade of the student.
   */
  set grade(value: string | undefined) {
    this._grade = value;
  }

  /**
   * Gets the date of the attendance record.
   *
   * @returns {Date | undefined} The date of the attendance record.
   */
  get attendanceDate(): Date | undefined {
    return this._attendanceDate;
  }

  /**
   * Sets the date of the attendance record.
   *
   * @param {Date | undefined} value - The date of the attendance record.
   */
  set attendanceDate(value: Date | undefined) {
    this._attendanceDate = value;
  }

  /**
   * Gets the status of the attendance record.
   *
   * @returns {AttendanceStatus | undefined} The status of the attendance record.
   */
  get status(): AttendanceStatus | undefined {
    return this._status;
  }

  /**
   * Sets the status of the attendance record.
   *
   * @param {AttendanceStatus | undefined} value - The status of the attendance record.
   */
  set status(value: AttendanceStatus | undefined) {
    this._status = value;
  }

  /**
   * Gets additional notes related to the attendance record.
   *
   * @returns {string | undefined} Additional notes related to the attendance record.
   */
  get notes(): string | undefined {
    return this._notes;
  }

  /**
   * Sets additional notes related to the attendance record.
   *
   * @param {string | undefined} value - Additional notes related to the attendance record.
   */
  set notes(value: string | undefined) {
    this._notes = value;
  }

  /**
   * Retrieves the data of the attendance record as an object.
   * @returns {Object} An object containing the data of the attendance record.
   * - id: The ID of the attendance record.
   * - student: The student associated with the attendance record.
   * - subject: The subject associated with the attendance record.
   * - classroom: The classroom associated with the attendance record.
   * - grade: The grade of the student.
   * - attendance_date: The date of the attendance record.
   * - status: The status of the attendance record.
   * - notes: Additional notes related to the attendance record.
   */
  getDataObject(): {
    id: number | undefined;
    student: Student | undefined;
    subject: Subject | undefined;
    classroom: Classroom | undefined;
    grade: string | undefined;
    attendance_date: Date | undefined;
    status: AttendanceStatus | undefined;
    notes: string | undefined;
  } {
    return {
      id: this._id,
      student: this._student,
      subject: this._subject,
      classroom: this._classroom,
      grade: this._grade,
      attendance_date: this._attendanceDate,
      status: this._status,
      notes: this._notes,
    };
  }
}
