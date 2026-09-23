"""Modulo de disponibilidad para el sistema de reserva de laboratorios.

Implementa el criterio de aceptacion del piloto:
una reserva valida no debe superponerse con otra reserva confirmada
del mismo laboratorio y horario.
"""

from __future__ import annotations

from datetime import datetime
from typing import Iterable, Mapping, Any


def se_superponen(
    inicio_a: datetime,
    fin_a: datetime,
    inicio_b: datetime,
    fin_b: datetime,
) -> bool:
    """Retorna True cuando dos intervalos de tiempo se superponen."""
    return inicio_a < fin_b and fin_a > inicio_b


def laboratorio_disponible(
    reservas: Iterable[Mapping[str, Any]],
    laboratorio: str,
    inicio: datetime,
    fin: datetime,
) -> bool:
    """Indica si un laboratorio puede reservarse en el intervalo solicitado.

    Solo bloquean la disponibilidad las reservas con estado ``confirmada``
    pertenecientes al mismo laboratorio.
    """
    if inicio >= fin:
        raise ValueError("La hora de inicio debe ser anterior a la hora de fin.")

    for reserva in reservas:
        if reserva.get("laboratorio") != laboratorio:
            continue

        if str(reserva.get("estado", "")).lower() != "confirmada":
            continue

        if se_superponen(
            inicio,
            fin,
            reserva["inicio"],
            reserva["fin"],
        ):
            return False

    return True
