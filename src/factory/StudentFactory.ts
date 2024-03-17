import { Student } from "../models/Student";
import { Gender, TypeOfIdentifications } from "../models/enums";

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

export class StudentFactory {
  static create(data: studentCreate) {
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
