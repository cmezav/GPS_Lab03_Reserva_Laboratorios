# E3 - Modulo de disponibilidad

Implementacion correspondiente al Work Package **OpenProject #40**.

## Criterio de aceptacion

Una reserva valida no debe superponerse con otra reserva confirmada del mismo laboratorio y horario.

## Casos automatizados

- Horario libre.
- Cruce parcial.
- Cruce total.
- Otro laboratorio.
- Reserva cancelada.
- Intervalo invalido.

## Trazabilidad

- OpenProject: OP#40
- Work Package local: http://localhost:8080/work_packages/40
- Rama: `feature/e3-modulo-disponibilidad`
- GitHub Actions: `.github/workflows/tests.yml`
