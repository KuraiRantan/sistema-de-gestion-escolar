/**
 * Retrieves the enum value associated with the specified key from the given enum object.
 *
 * @param {T} enumValue - The enum object from which to retrieve the value.
 * @param {string} keyValue - The key (string value) to search for in the enum object.
 * @returns {T[keyof T] | undefined} The value associated with the specified key in the enum object, or undefined if the key is not found.
 * @template T - The type of the enum object.
 */
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
