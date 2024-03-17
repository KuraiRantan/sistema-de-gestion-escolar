export const getEnum = <T>(
  enumValue: T,
  keyValue: string
): T[keyof T] | undefined => {
  if (typeof enumValue === "object" && enumValue !== null) {
    const keys = Object.keys(enumValue) as (keyof T)[];
    for (const key of keys) {
      if (enumValue[key] === keyValue) {
        return enumValue[key];
      }
    }
  }
  return undefined;
};
