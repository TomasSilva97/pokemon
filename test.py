from pokemon import readMovements

import unittest
  
class PokemonTests(unittest.TestCase):
  
    def test_unexpected_input(self):
        with self.assertRaises(Exception):
            readMovements("D")
    
    def test_void(self):
        self.assertEqual(readMovements(""), 1)

    def test_examples(self):
        self.assertEqual(readMovements("E"),2)
        self.assertEqual(readMovements("NESO"),4)
        self.assertEqual(readMovements("NSNSNSNS"),2)
        
     
  
if __name__ == '__main__': 
    unittest.main()