import { StudentFactory, studentCreate } from "../factory/StudentFactory";
import { Gender, TypeOfIdentifications } from "../models/enums";
import { StudentRenderer } from "../renderer/StudentRenderer";
import { StudentRepository } from "../repository/StudentRepository";

export class StudentController {
  static init() {
    const container = document.querySelector("#container-form-create-student");

    if (container === null) throw new Error("Container not found in the DOM");

    const renderStudent = new StudentRenderer();
    renderStudent.render(container);

    const form = document.querySelector("#form-create-student");
    if (form === null)
      throw new Error("Form create student not found in the DOM");

    form.addEventListener("submit", StudentController.handleSubmitCreate);
  }

  private static async handleSubmitCreate(e: Event) {
    e.preventDefault();
    if (e.target instanceof HTMLFormElement) {
      const elements = e.target.elements;

      const genderSelect = elements.namedItem("gender") as HTMLSelectElement;
      const gender = genderSelect.options[genderSelect.selectedIndex].value;

      const typeOfISelect = elements.namedItem(
        "typeOfIdentification"
      ) as HTMLSelectElement;
      const typeOfIdentification =
        typeOfISelect.options[typeOfISelect.selectedIndex].value;

      const data: studentCreate = {
        firstName: (elements.namedItem("firstName") as HTMLInputElement).value,
        lastName: (elements.namedItem("lastName") as HTMLInputElement).value,
        identification: (
          elements.namedItem("identification") as HTMLInputElement
        ).value,
        address: (elements.namedItem("address") as HTMLInputElement).value,
        email: (elements.namedItem("email") as HTMLInputElement).value,
        phone: (elements.namedItem("phone") as HTMLInputElement).value,
        gender: Gender[gender as keyof typeof Gender],
        typeOfIdentification:
          TypeOfIdentifications[
            typeOfIdentification as keyof typeof TypeOfIdentifications
          ],
        currentGrade: (elements.namedItem("currentGrade") as HTMLInputElement)
          .value,
        birthdate: new Date(
          (elements.namedItem("birthdate") as HTMLInputElement).value
        ),
      };

      const student = StudentFactory.create(data);
      try {
        await StudentRepository.create(student);
        alert("Estudiante creado exitosamente.");
        e.target.reset();
      } catch (error) {
        alert("Fallo al crear el estudiante: " + (error as Error).message);
      }
    }
  }
}
