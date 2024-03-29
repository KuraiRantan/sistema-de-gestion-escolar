import { StudentController } from "./controller/StudentController";

/**
 * Initializes the student controller if the page route matches "/SGE/student/create".
 * This method should be called inside the 'DOMContentLoaded' event of the document.
 */
document.addEventListener("DOMContentLoaded", () => {
  const route = window.location.pathname.replace(".html", "");
  if (route === "/SGE/student/create") {
    StudentController.init();
  }
});
