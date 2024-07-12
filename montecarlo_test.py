
import unittest
import numpy as np
import pandas as pd
from montecarlo.montecarlo import Die, Game, Analyzer



class TestDie(unittest.TestCase):
    """Test cases for Die class."""

    def setUp(self):
        """Set up a Die instance for testing."""
        faces = np.array([1, 2, 3, 4, 5, 6])
        self.die = Die(faces)

    def test_init(self):
        """Test Die initialization."""
        self.assertEqual(len(self.die.faces), 6)
        self.assertTrue(np.array_equal(self.die.faces, np.array([1, 2, 3, 4, 5, 6])))
        self.assertTrue(np.all(self.die.weights['weights'] == 1.0))

    def test_change_weight(self):
        """Test changing the weight of a face."""
        self.die.change_weight(1, 2.0)
        self.assertEqual(self.die.weights.at[1, 'weights'], 2.0)
        with self.assertRaises(IndexError):
            self.die.change_weight(7, 1.0)
        with self.assertRaises(TypeError):
            self.die.change_weight(1, 'a')

    def test_roll(self):
        """Test rolling the die."""
        rolls = self.die.roll(5)
        self.assertEqual(len(rolls), 5)
        for face in rolls:
            self.assertIn(face, self.die.faces)

    def test_show(self):
        """Test showing the die's current state."""
        weights = self.die.show()
        self.assertTrue(weights.equals(self.die.weights))



class TestGame(unittest.TestCase):
    """Test cases for Game class."""

    def setUp(self):
        """Set up a Game instance for testing."""
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])

    def test_init(self):
        """Test Game initialization."""
        self.assertEqual(len(self.game.dice), 2)
        self.assertIsInstance(self.game.dice[0], Die)

    def test_play(self):
        """Test playing the game."""
        self.game.play(10)
        self.assertEqual(len(self.game.results), 10)
        self.assertEqual(self.game.results.shape[1], 2)

    def test_show(self):
        """Test showing the game's most recent play results."""
        self.game.play(5)
        results_wide = self.game.show()
        results_narrow = self.game.show('narrow')
        self.assertEqual(results_wide.shape, (5, 2))
        self.assertEqual(results_narrow.shape, (10, 2))
        with self.assertRaises(ValueError):
            self.game.show('invalid')



class TestAnalyzer(unittest.TestCase):
    """Test cases for Analyzer class."""

    def setUp(self):
        """Set up an Analyzer instance for testing."""
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        game.play(10)
        self.analyzer = Analyzer(game)

    def test_init(self):
        """Test Analyzer initialization"""
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        analyzer = Analyzer(game)
        self.assertIsInstance(analyzer.game,Game)
        self.assertIsInstance(analyzer.results, pd.DataFrame)

    def test_jackpot(self):
        """Test computing the number of jackpots."""
        jackpots = self.analyzer.jackpot()
        self.assertIsInstance(jackpots, int)

    def test_face_counts_per_roll(self):
        """Test computing face counts per roll."""
        face_counts = self.analyzer.face_counts_per_roll()
        self.assertIsInstance(face_counts, pd.DataFrame)
        self.assertEqual(face_counts.shape, (6,2))

    def test_combo_count(self):
        """Test computing distinct combinations of faces rolled."""
        combo_counts = self.analyzer.combo_count()
        self.assertIsInstance(combo_counts, pd.DataFrame)

    def test_permutation_count(self):
        """Test computing distinct permutations of faces rolled."""
        permutation_counts = self.analyzer.permutation_count()
        self.assertIsInstance(permutation_counts, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()













