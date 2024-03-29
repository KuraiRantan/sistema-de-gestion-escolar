/**
 * Represents a subject.
 */
export default class Subject {
  /**
   * Creates an instance of Subject.
   *
   * @param {number | undefined} _id - The ID of the subject.
   * @param {string | undefined} _name - The name of the subject.
   * @param {string | undefined} _description - The description of the subject.
   */
  constructor(
    private _id?: number | undefined,
    private _name?: string | undefined,
    private _description?: string | undefined
  ) {}

  /**
   * Gets the ID of the subject.
   *
   * @returns {number | undefined} The ID of the subject.
   */
  get id(): number | undefined {
    return this._id;
  }

  /**
   * Sets the ID of the subject.
   *
   * @param {number | undefined} value - The ID of the subject.
   */
  set id(value: number | undefined) {
    this._id = value;
  }

  /**
   * Gets the name of the subject.
   *
   * @returns {string | undefined} The name of the subject.
   */
  get name(): string | undefined {
    return this._name;
  }

  /**
   * Sets the name of the subject.
   *
   * @param {string | undefined} value - The name of the subject.
   */
  set name(value: string | undefined) {
    this._name = value;
  }

  /**
   * Gets the description of the subject.
   *
   * @returns {string | undefined} The description of the subject.
   */
  get description(): string | undefined {
    return this._description;
  }

  /**
   * Sets the description of the subject.
   *
   * @param {string | undefined} value - The description of the subject.
   */
  set description(value: string) {
    this._description = value;
  }

  /**
   * Gets the data of the subject as an object.
   *
   * @returns {Object} An object containing the data of the subject.
   * - id: The ID of the subject.
   * - name: The name of the subject.
   * - description: The description of the subject.
   */
  getDataObject(): {
    id: number | undefined;
    name: string | undefined;
    description: string | undefined;
  } {
    return {
      id: this._id,
      name: this._name,
      description: this._description,
    };
  }
}
