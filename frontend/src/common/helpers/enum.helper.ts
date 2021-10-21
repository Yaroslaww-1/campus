// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const getValuesFromEnum = <K = string>(enm: any, typeOfKey = "string"): K[] => {
  return Object.keys(enm).map(key => enm[key]).filter(value => typeof value === typeOfKey);
};
