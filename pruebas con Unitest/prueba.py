import unittest
import cambiaTexto


class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambiaTexto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DIA")


if __name__ == '__main__':
    unittest.main()
