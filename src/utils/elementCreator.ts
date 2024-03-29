/**
 * Creates a new HTML element with the specified attributes.
 *
 * @param {string} targName - The name of the HTML element to create.
 * @param {Record<string, string>} attributes - An object containing the key-value pairs of attributes to set on the element.
 * @returns {HTMLElement} The newly created HTML element with the specified attributes.
 */
export function createElementWithAttributes(
  targName: string,
  attributes: Record<string, string>
): HTMLElement {
  const element = document.createElement(targName);
  for (let keyAttr in attributes) {
    element.setAttribute(keyAttr, attributes[keyAttr]);
  }

  return element;
}
