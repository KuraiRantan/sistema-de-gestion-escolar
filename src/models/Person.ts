import { Gender, TypeOfIdentifications } from "./enums";

/**
 * @abstract Abstract class that represents a person.
 */
export default abstract class Person {
  /**
   * Constructor of the abstract class Person.
   *
   * @param {TypeOfIdentification | undefined} _typeOfIdentification - Type of identification of the person.
   * @param {string | undefined} _identification - Identification number of the person.
   * @param {string | undefined} _firstName - First name of the person.
   * @param {string | undefined} _lastName - Last name of the person.
   * @param {Date | undefined} _birthdate - Date of birth of the person.
   * @param {Gender | undefined} _gender - Gender of the person.
   * @param {string | undefined} _address - Address of the person.
   * @param {string | undefined} _email - Email of the person.
   * @param {string | undefined} _phone - Person's telephone number.
   */
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

  /**
   * Gets the type of identification of the person.
   *
   * @returns {TypeOfIdentifications | undefined} The type of identification of the person
   */
  get typeOfIdentification(): TypeOfIdentifications | undefined {
    return this._typeOfIdentification;
  }

  /**
   * Sets the type of identification of the person.
   *
   * @param {TypeOfIdentifications | undefined} value - The type of identification of the person.
   */
  set typeOfIdentification(value: TypeOfIdentifications | undefined) {
    this._typeOfIdentification = value;
  }

  /**
   * Gets the identification number of the person.
   *
   * @returns {string | undefined} The identification number of the person.
   */
  get identification(): string | undefined {
    return this._identification;
  }

  /**
   * Sets the identification number of the person.
   *
   * @param {string | undefined} value - The identification number of the person.
   */
  set identification(value: string | undefined) {
    this._identification = value;
  }

  /**
   * Gets the first name of the person.
   *
   * @returns {string | undefined} The first name of the person.
   */
  get firstName(): string | undefined {
    return this._firstName;
  }

  /**
   * Sets the first name of the person.
   *
   * @param {string | undefined} value - The first name of the person.
   */
  set firstName(value: string | undefined) {
    this._firstName = value;
  }

  /**
   * Gets the last name of the person.
   *
   * @returns {string | undefined} The last name of the person.
   */
  get lastName(): string | undefined {
    return this._lastName;
  }

  /**
   * Sets the last name of the person.
   *
   * @param {string | undefined} value - The last name of the person.
   */
  set lastName(value: string | undefined) {
    this._lastName = value;
  }

  /**
   * Gets the date of birth of the person.
   *
   * @returns {Date | undefined} The date of birth of the person.
   */
  get birthdate(): Date | undefined {
    return this._birthdate;
  }

  /**
   * Sets the date of birth of the person.
   *
   * @param {Date | undefined} value - The date of birth of the person.
   */
  set birthdate(value: Date | undefined) {
    this._birthdate = value;
  }

  /**
   * Gets the gender of the person.
   *
   * @returns {Gender | undefined} The gender of the person.
   */
  get gender(): Gender | undefined {
    return this._gender;
  }

  /**
   * Sets the gender of the person.
   *
   * @param {Gender | undefined} value - The gender of the person.
   */
  set gender(value: Gender | undefined) {
    this._gender = value;
  }

  /**
   * Gets the address of the person.
   *
   * @returns {string | undefined} The address of the person.
   */
  get address(): string | undefined {
    return this._address;
  }

  /**
   * Sets the address of the person.
   *
   * @param {string | undefined} value - The address of the person.
   */
  set address(value: string | undefined) {
    this._address = value;
  }

  /**
   * Gets the email of the person.
   *
   * @returns {string | undefined} The email of the person.
   */
  get email(): string | undefined {
    return this._email;
  }

  /**
   * Sets the email of the person.
   *
   * @param {string | undefined} value - The email of the person.
   */
  set email(value: string | undefined) {
    this._email = value;
  }

  /**
   * Gets the phone number of the person.
   *
   * @returns {string | undefined} The phone number of the person.
   */
  get phone(): string | undefined {
    return this._phone;
  }

  /**
   * Sets the phone number of the person.
   *
   * @param {string | undefined} value - The phone number of the person.
   */
  set phone(value: string | undefined) {
    this._phone = value;
  }

  /**
   * @abstract Abstract method that must be implemented by child classes to validate the person's data.
   *
   * @returns {boolean} True if the person's data is valid, false otherwise.
   */
  abstract validate(): boolean;
}
