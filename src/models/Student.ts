import { formatDate } from "../utils/manageDate";
import Person from "./Person";
import { Gender, TypeOfIdentifications } from "./enums";

export class Student extends Person {
  constructor(
    private _id?: number,
    typeOfIdentification?: TypeOfIdentifications,
    identification?: string,
    firstName?: string,
    lastName?: string,
    birthdate?: Date,
    gender?: Gender,
    address?: string,
    email?: string,
    phone?: string,
    private _currentGrade?: string
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

  get id(): number | undefined {
    return this._id;
  }

  set id(value: number) {
    this._id = value;
  }

  get currentGrade(): string | undefined {
    return this._currentGrade;
  }

  set currentGrade(value: string) {
    this._currentGrade = value;
  }

  validate(): boolean {
    return true;
  }

  getDataObject() {
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
