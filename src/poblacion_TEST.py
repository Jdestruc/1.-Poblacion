import unittest
from random import randint
import poblacion
import matplotlib.pyplot as plt

class Test_Poblacion(unittest.TestCase):
    def setUp(self):
        self.pbl = poblacion.lee_poblaciones("/home/pcjulio/Programacion/CleanCodeCurse/1. Poblacion/data/population.csv")

    def tearDown(self):
        pass

    def test_lee_poblaciones(self):
        RandomLine = self.pbl[randint(0, len(self.pbl))]
        self.assertEqual(type(RandomLine[0]), str)
        self.assertEqual(type(RandomLine[1]), str)
        self.assertEqual(type(RandomLine[2]), int)
        self.assertEqual(type(RandomLine[3]), float)

        self.assertEqual(("Caribbean small states", "CSS", 2000, 6530691.0), self.pbl[97])
        self.assertEqual(("European Union", "EUU", 1985, 470637754.0), self.pbl[652])
        self.assertEqual(("North America", "NAC", 1964, 211262900.0), self.pbl[1828])
        self.assertEqual(("World", "WLD", 2016, 7442135578.0), self.pbl[2621])
        self.assertEqual(("Nigeria", "NGA", 1981, 75482552.0), self.pbl[10786])

    def test_calcula_paises(self):
        answer = poblacion.calcula_paises(self.pbl)

        self.assertIn("Bhutan", answer)
        self.assertIn("Grenada", answer)
        self.assertIn("Kenya", answer)
        self.assertIn("Malta", answer)
        self.assertIn("Tajikistan", answer)

    def test_filtra_por_pais(self):
        answer = poblacion.filtra_por_pais(self.pbl, "Guinea")
        self.assertEqual((1976, 4381601.0), answer[16])

        answer = poblacion.filtra_por_pais(self.pbl, "Argentina")
        self.assertEqual((2007, 39970224.0), answer[47])

        answer = poblacion.filtra_por_pais(self.pbl, "Eritrea")
        self.assertEqual((1990, 3113311.0), answer[30])

        answer = poblacion.filtra_por_pais(self.pbl, "Peru")
        self.assertEqual((1968, 12629329.0), answer[8])

        answer = poblacion.filtra_por_pais(self.pbl, "Tuvalu")
        self.assertEqual((1984, 8530.0), answer[24])

    def test_filtra_por_paises_y_anyo(self):
        answer = poblacion.filtra_por_paises_y_anyo(self.pbl, 1999, ["Belgium", "Finland", "Maldives", "Somalia", "Venezuela"])

        self.assertIn(("Belgium", 10226419), answer)
        self.assertIn(("Finland", 5165474), answer)
        self.assertIn(("Maldives", 280000), answer)
        self.assertIn(("Somalia", 8720231), answer)
        self.assertIn(("Venezuela", 24028689), answer)

    def test_muestra_evolucion_poblacion(self):
        habitantes = [63699, 65713, 67808, 69964, 72131, 74289, 76413, 78522, 80673, 82940, 85389, 88022, 90823, 93765, 96796, 99872, 103028, 106222, 109429, 112580]
        plt.plot(list(range(1960, 1980)), habitantes, color = "green")
        poblacion.muestra_evolucion_poblacion(self.pbl, "Vanuatu")

    def test_muestra_comparativa_paises_anyo(self):
        pass

if __name__ == '__main__':
    unittest.main()