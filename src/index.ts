import { StudentController } from "./controller/StudentController";

document.addEventListener("DOMContentLoaded", () => {
  const route = window.location.pathname.replace(".html", "");
  if (route === "/SGE/student/create") {
    StudentController.init();
  }
});
