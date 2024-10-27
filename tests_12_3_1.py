import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        ole = runner.Runner('Ole')
        i = 1
        while i <= 10:
            runner.Runner.walk(ole)
            i += 1
        self.assertEqual(ole.distance, 50)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        leo = runner.Runner('Leo')
        i = 1
        while i <= 10:
            runner.Runner.run(leo)
            i += 1
        self.assertEqual(leo.distance, 100)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        alex = runner.Runner('Alex')
        vlad = runner.Runner('Vlad')
        i = 1
        while i <= 10:
            runner.Runner.run(alex)
            runner.Runner.walk(vlad)
            i += 1
        self.assertNotEqual(alex.distance, vlad.distance)


if __name__ == "__main__":
    unittest.main()