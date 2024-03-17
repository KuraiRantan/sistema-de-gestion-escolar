import { Gender, TypeOfIdentifications } from "../models/enums";
import { createElementWithAttributes } from "../utils/elementCreator";

export abstract class Render {
  abstract render(container: Element): void;
}

export class StudentRenderer implements Render {
  static htmlElement: HTMLElement | null = null;

  private init() {
    if (StudentRenderer.htmlElement !== null) return;
    const form = createElementWithAttributes("form", {
      id: "form-create-student",
    });
    const selectGender = createElementWithAttributes("select", {
      required: "",
      name: "gender",
    });
    const selectTypeOfIdentifications = createElementWithAttributes("select", {
      required: "",
      name: "typeOfIdentification",
    });

    Object.keys(Gender).forEach((value) => {
      const optionGender = document.createElement("option");
      optionGender.value = value;
      optionGender.text = Gender[value as keyof typeof Gender];
      selectGender.appendChild(optionGender);
    });

    Object.keys(TypeOfIdentifications).forEach((value) => {
      const optionTypeOfIdentification = document.createElement("option");
      optionTypeOfIdentification.value = value;
      optionTypeOfIdentification.text =
        TypeOfIdentifications[value as keyof typeof TypeOfIdentifications];
      selectTypeOfIdentifications.appendChild(optionTypeOfIdentification);
    });

    const inputFirstName = createElementWithAttributes("input", {
      type: "text",
      name: "firstName",
      placeholder: "Ingrese su nombre...",
      required: "",
    });
    const inputLastName = createElementWithAttributes("input", {
      type: "text",
      name: "lastName",
      placeholder: "Ingrese su apellido...",
      required: "",
    });
    const inputIdentification = createElementWithAttributes("input", {
      type: "text",
      name: "identification",
      placeholder: "Ingrese su número de identificación...",
      required: "",
    });
    const inputAddress = createElementWithAttributes("input", {
      type: "text",
      name: "address",
      placeholder: "Ingrese su dirección...",
    });
    const inputEmail = createElementWithAttributes("input", {
      type: "email",
      name: "email",
      placeholder: "Ingrese su correo electrónico...",
    });
    const inputPhone = createElementWithAttributes("input", {
      type: "phone",
      name: "phone",
      placeholder: "Ingrese su número de teléfono...",
    });
    const currentGrade = createElementWithAttributes("input", {
      type: "text",
      name: "currentGrade",
      placeholder: "Ingrese su grado actual...",
      required: "",
    });
    const inputBirthdate = createElementWithAttributes("input", {
      type: "date",
      name: "birthdate",
      required: "",
    });
    const submitButton = createElementWithAttributes("input", {
      type: "submit",
    });

    const wrapperFirstName = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperLastName = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperIdentification = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperAddress = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperEmail = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperPhone = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperGender = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperTypeOfIdentification = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperGrade = createElementWithAttributes("label", {
      style: "display:block",
    });
    const wrapperBirthdate = createElementWithAttributes("label", {
      style: "display:block",
    });

    wrapperFirstName.textContent = "Nombre(s):";
    wrapperFirstName.appendChild(inputFirstName);

    wrapperLastName.textContent = "Apellido(s):";
    wrapperLastName.appendChild(inputLastName);

    wrapperIdentification.textContent = "Identificación:";
    wrapperIdentification.appendChild(inputIdentification);

    wrapperAddress.textContent = "Dirección:";
    wrapperAddress.appendChild(inputAddress);

    wrapperEmail.textContent = "Email:";
    wrapperEmail.appendChild(inputEmail);

    wrapperPhone.textContent = "Teléfono:";
    wrapperPhone.appendChild(inputPhone);

    wrapperGender.textContent = "Género:";
    wrapperGender.appendChild(selectGender);

    wrapperTypeOfIdentification.textContent = "Tipo de identificacion:";
    wrapperTypeOfIdentification.appendChild(selectTypeOfIdentifications);

    wrapperGrade.textContent = "Grado:";
    wrapperGrade.appendChild(currentGrade);

    wrapperBirthdate.textContent = "Fecha de nacimiento:";
    wrapperBirthdate.appendChild(inputBirthdate);

    form.append(
      wrapperFirstName,
      wrapperLastName,
      wrapperIdentification,
      wrapperTypeOfIdentification,
      wrapperBirthdate,
      wrapperGender,
      wrapperGrade,
      wrapperAddress,
      wrapperEmail,
      wrapperPhone,
      submitButton
    );

    StudentRenderer.htmlElement = form;
  }

  render(container: Element): void {
    this.init();
    if (StudentRenderer.htmlElement === null) {
      throw new Error("Failed to create html element for student form");
    }
    container.appendChild(StudentRenderer.htmlElement);
  }
}
