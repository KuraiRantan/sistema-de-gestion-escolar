export default class Classroom {
  constructor(
    private _id?: number,
    private _name?: string,
    private _capacity?: number,
    private _ubication?: string
  ) {}

  get id(): number | undefined {
    return this._id;
  }

  set id(value: number) {
    this._id = value;
  }

  get name(): string | undefined {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }

  get capacity(): number | undefined {
    return this._capacity;
  }

  set capacity(value: number) {
    this._capacity = value;
  }

  get ubication(): string | undefined {
    return this._ubication;
  }

  set ubication(value: string) {
    this._ubication = value;
  }

  getDataObject() {
    return {
      id: this._id,
      name: this._name,
      capacity: this._capacity,
      ubication: this._ubication,
    };
  }
}
