export default function appendToEachArrayValue(array, appendString) {
  const narray = [];
  for (const element of array) {
    narray.push(appendString + element);
  }
  return narray;
}
