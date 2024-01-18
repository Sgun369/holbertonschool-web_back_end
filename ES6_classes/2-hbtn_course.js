export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string' || typeof length !== 'number' || !Array.isArray(students)) {
      throw TypeError('Wrong data type');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw TypeError('length must be a number');
    } else {
      this._length = length;
    }
  }

  get sttudents() {
    return this._students;
  }

  set(students) {
    if (!Array.isArray(students)) {
      throw TypeError('students must be an array');
    } else {
      this._students = students;
    }
  }
}
