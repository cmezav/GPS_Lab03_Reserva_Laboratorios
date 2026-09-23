import unittest
from datetime import datetime

from app.disponibilidad import laboratorio_disponible


def dt(hora: int, minuto: int = 0) -> datetime:
    return datetime(2026, 9, 22, hora, minuto)


class TestDisponibilidad(unittest.TestCase):
    def setUp(self):
        self.reservas = [
            {
                "laboratorio": "Lab A",
                "inicio": dt(10),
                "fin": dt(12),
                "estado": "confirmada",
            }
        ]

    def test_horario_libre(self):
        self.assertTrue(
            laboratorio_disponible(self.reservas, "Lab A", dt(12), dt(14))
        )

    def test_cruce_parcial_no_disponible(self):
        self.assertFalse(
            laboratorio_disponible(self.reservas, "Lab A", dt(11), dt(13))
        )

    def test_cruce_total_no_disponible(self):
        self.assertFalse(
            laboratorio_disponible(self.reservas, "Lab A", dt(9), dt(13))
        )

    def test_otro_laboratorio_si_disponible(self):
        self.assertTrue(
            laboratorio_disponible(self.reservas, "Lab B", dt(11), dt(13))
        )

    def test_reserva_cancelada_no_bloquea(self):
        reservas = [
            {
                "laboratorio": "Lab A",
                "inicio": dt(10),
                "fin": dt(12),
                "estado": "cancelada",
            }
        ]
        self.assertTrue(
            laboratorio_disponible(reservas, "Lab A", dt(11), dt(13))
        )

    def test_intervalo_invalido(self):
        with self.assertRaises(ValueError):
            laboratorio_disponible(self.reservas, "Lab A", dt(12), dt(10))


if __name__ == "__main__":
    unittest.main()
