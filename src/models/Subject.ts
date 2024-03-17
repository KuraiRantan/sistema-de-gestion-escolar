export default class Subject {
  constructor(
    private _id?: number,
    private _name?: string,
    private _description?: string
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

  get description(): string | undefined {
    return this._description;
  }

  set description(value: string) {
    this._description = value;
  }

  getDataObject() {
    return {
      id: this._id,
      name: this._name,
      description: this._description,
    };
  }
}
