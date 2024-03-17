export function formatDate(date: Date): string {
  const dia = date.getUTCDate(); // UTC because since it is a fixed date, I am not interested in the time zone.
  const mes = date.getUTCMonth() + 1; // Los meses en JavaScript comienzan desde 0 (enero = 0)
  const anio = date.getUTCFullYear();
  const fechaFormateada = `${anio}-${mes}-${dia}`;
  return fechaFormateada;
}
