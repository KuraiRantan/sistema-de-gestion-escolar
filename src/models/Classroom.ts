/**
 * Represents a classroom.
 */
export default class Classroom {
  /**
   * Creates an instance of Classroom.
   *
   * @param {number | undefined} _id - The ID of the classroom.
   * @param {string | undefined} _name - The name of the classroom.
   * @param {number | undefined} _capacity - The capacity of the classroom.
   * @param {string | undefined} _ubication - The location of the classroom.
   */
  constructor(
    private _id?: number | undefined,
    private _name?: string | undefined,
    private _capacity?: number | undefined,
    private _ubication?: string | undefined
  ) {}

  /**
   * Gets the ID of the classroom.
   *
   * @returns {number | undefined} The ID of the classroom.
   */
  get id(): number | undefined {
    return this._id;
  }

  /**
   * Sets the ID of the classroom.
   *
   * @param {number | undefined} value - The ID of the classroom.
   */
  set id(value: number | undefined) {
    this._id = value;
  }

  /**
   * Gets the name of the classroom.
   *
   * @returns {string | undefined} The name of the classroom.
   */
  get name(): string | undefined {
    return this._name;
  }

  /**
   * Sets the name of the classroom.
   *
   * @param {string | undefined} value - The name of the classroom.
   */
  set name(value: string | undefined) {
    this._name = value;
  }

  /**
   * Gets the capacity of the classroom.
   *
   * @returns {number | undefined} The capacity of the classroom.
   */
  get capacity(): number | undefined {
    return this._capacity;
  }

  /**
   * Sets the capacity of the classroom.
   *
   * @param {number | undefined} value - The capacity of the classroom.
   */
  set capacity(value: number | undefined) {
    this._capacity = value;
  }

  /**
   * Gets the location of the classroom.
   *
   * @returns {string | undefined} The location of the classroom.
   */
  get ubication(): string | undefined {
    return this._ubication;
  }

  /**
   * Sets the location of the classroom.
   *
   * @param {string | undefined} value - The location of the classroom.
   */
  set ubication(value: string | undefined) {
    this._ubication = value;
  }

  /**
   * Gets the data of the classroom as an object.
   *
   * @returns {Object} An object containing the data of the classroom.
   * - id: The ID of the classroom.
   * - name: The name of the classroom.
   * - capacity: The capacity of the classroom.
   * - ubication: The location of the classroom.
   */
  getDataObject(): {
    id: number | undefined;
    name: string | undefined;
    capacity: number | undefined;
    ubication: string | undefined;
  } {
    return {
      id: this._id,
      name: this._name,
      capacity: this._capacity,
      ubication: this._ubication,
    };
  }
}
