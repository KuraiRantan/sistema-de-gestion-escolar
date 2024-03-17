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
