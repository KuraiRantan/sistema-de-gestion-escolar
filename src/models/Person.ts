import { Gender, TypeOfIdentifications } from "./enums";

export default abstract class Person {
  constructor(
    protected _typeOfIdentification?: TypeOfIdentifications,
    protected _identification?: string,
    protected _firstName?: string,
    protected _lastName?: string,
    protected _birthdate?: Date,
    protected _gender?: Gender,
    protected _address?: string,
    protected _email?: string,
    protected _phone?: string
  ) {}

  get typeOfIdentification(): TypeOfIdentifications | undefined {
    return this._typeOfIdentification;
  }

  set typeOfIdentification(value: TypeOfIdentifications) {
    this._typeOfIdentification = value;
  }

  get identification(): string | undefined {
    return this._identification;
  }

  set identification(value: string) {
    this._identification = value;
  }

  get firstName(): string | undefined {
    return this._firstName;
  }

  set firstName(value: string) {
    this._firstName = value;
  }

  get lastName(): string | undefined {
    return this._lastName;
  }

  set lastName(value: string) {
    this._lastName = value;
  }

  get birthdate(): Date | undefined {
    return this._birthdate;
  }

  set birthdate(value: Date) {
    this._birthdate = value;
  }

  get gender(): Gender | undefined {
    return this._gender;
  }

  set gender(value: Gender) {
    this._gender = value;
  }

  get address(): string | undefined {
    return this._address;
  }

  set address(value: string) {
    this._address = value;
  }

  get email(): string | undefined {
    return this._email;
  }

  set email(value: string) {
    this._email = value;
  }

  get phone(): string | undefined {
    return this._phone;
  }

  set phone(value: string) {
    this._phone = value;
  }

  abstract validate(): boolean;
}
