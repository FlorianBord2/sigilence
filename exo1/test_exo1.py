import unittest
import exo1

class TestStringMethods(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(exo1.myparse('arbre'), 'a3e')
        self.assertEqual(exo1.myparse('parachute'), 'p7e')
        self.assertEqual(exo1.myparse('toulouse'), 't6e')
        self.assertEqual(exo1.myparse('Arbre3e'), 'ko')
        self.assertEqual(exo1.myparse('la'), 'la')
        self.assertEqual(exo1.myparse('k'), 'k')
        self.assertEqual(exo1.myparse('12'), 'ko')
        self.assertEqual(exo1.myparse('1'), 'ko')
        self.assertEqual(exo1.myparse(''), 'ko')
        self.assertEqual(exo1.myparse('On est 26 dans le batiment 7'), 'ko')
        self.assertEqual(exo1.myparse('On est dans le batiment'), 'ko')
        self.assertEqual(exo1.myparse('ABCDEFGHIJKLMNOPQRSTUVWYYZ'), 'A24Z')
        self.assertEqual(exo1.myparse('aéb'), 'a1b')
        self.assertEqual(exo1.myparse('aéîôûŵĉĵĥĝŝb'), 'a10b')
        self.assertEqual(exo1.myparse('aéîôûŵĉĵĥ1ĝŝb'), 'ko')

if __name__ == '__main__':
    unittest.main()
