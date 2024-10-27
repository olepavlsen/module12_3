import unittest
import tests_12_3
import tests_12_3_1

RunnerST = unittest.TestSuite()
RunnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_1.RunnerTest))
RunnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunnerST)
