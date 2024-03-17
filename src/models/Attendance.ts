import Classroom from "./Classroom";
import { Student } from "./Student";
import Subject from "./Subject";
import { AttendanceStatus } from "./enums";

export default class Attendance {
  constructor(
    private _id?: number,
    private _student?: Student,
    private _subject?: Subject,
    private _classroom?: Classroom,
    private _grade?: string,
    private _attendanceDate?: Date,
    private _status?: AttendanceStatus,
    private _notes?: string
  ) {}

  get id(): number | undefined {
    return this._id;
  }

  set id(value: number) {
    this._id = value;
  }

  get student(): Student | undefined {
    return this._student;
  }

  set student(value: Student) {
    this._student = value;
  }

  get subject(): Subject | undefined {
    return this._subject;
  }

  set subject(value: Subject) {
    this._subject = value;
  }

  get classroom(): Classroom | undefined {
    return this._classroom;
  }

  set classroom(value: Classroom) {
    this._classroom = value;
  }

  get grade(): string | undefined {
    return this._grade;
  }

  set grade(value: string) {
    this._grade = value;
  }

  get attendanceDate(): Date | undefined {
    return this._attendanceDate;
  }

  set attendanceDate(value: Date) {
    this._attendanceDate = value;
  }

  get status(): AttendanceStatus | undefined {
    return this._status;
  }

  set status(value: AttendanceStatus) {
    this._status = value;
  }

  get notes(): string | undefined {
    return this._notes;
  }

  set notes(value: string) {
    this._notes = value;
  }

  getDataObject() {
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
