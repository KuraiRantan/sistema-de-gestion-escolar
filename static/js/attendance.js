const handleChangeAttendanceStatus = (e) => {
  let areCheckedAny = false;
  let prevSelectedRadio = null;
  const currentSelectedRadio = e.target;
  const form = e.target.form;

  for (let radio of form.querySelectorAll("input")) {
    const dataUnknow = radio.attributes.getNamedItem("data-unknow");
    if (dataUnknow === null) {
      radio.setAttribute("data-unknow", "False");
      continue;
    }
    if (dataUnknow.value.toLowerCase() === "true") {
      areCheckedAny = true;
      prevSelectedRadio = radio;
      radio.setAttribute("data-unknow", "False");

      break;
    }
    radio.setAttribute("data-unknow", "False");
  }

  const currentUnknow =
    currentSelectedRadio.attributes.getNamedItem("data-unknow");
  if (currentUnknow !== null && currentUnknow.value.toLowerCase() !== "true") {
    currentSelectedRadio.setAttribute("data-unknow", "True");
  }

  let resultConfirm = null;

  if (areCheckedAny) {
    resultConfirm = confirm(
      "¿Realmente desea actualizar el estado de asistencia del estudiante?"
    );
  }

  if ((!resultConfirm && !areCheckedAny) || (resultConfirm && areCheckedAny)) {
    const id = form.querySelector("#id-attendance")?.value;
    const status = currentSelectedRadio.value;
    if (!id && !status) {
      prevSelectedRadio.checked = true;
      prevSelectedRadio.setAttribute("data-unknow", "True");
      currentSelectedRadio.setAttribute("data-unknow", "False");
      return alert(
        "Hay una inconsistencia en los datos, comuniquese con el administrador del sitio."
      );
    }
    const data = {
      id,
      status,
    };
    fetchChangeStatus(data)
      .then()
      .catch(() => {
        prevSelectedRadio.checked = true;
        prevSelectedRadio.setAttribute("data-unknow", "True");
        currentSelectedRadio.setAttribute("data-unknow", "False");
        alert("Error al cambiar el estado del estudiante.");
      });
  } else {
    prevSelectedRadio.checked = true;
    prevSelectedRadio.setAttribute("data-unknow", "True");
    currentSelectedRadio.setAttribute("data-unknow", "False");
  }
};

const fetchChangeStatus = async (data) => {
  const res = await fetch(
    `${window.location.origin}/SGE/api/attendance.json/change-attendance-status`,
    {
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify(data),
    }
  );
};
