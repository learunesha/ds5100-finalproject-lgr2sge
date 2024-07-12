import numpy as np
import pandas as pd

class Die:
    """
    A class representing a die with N faces and associated weights.

    Attributes
    ----------
    faces : np.ndarray
        A NumPy array of faces of the die.
    weights : pd.DataFrame
        A DataFrame containing the faces and their respective weights.
    """
    
    def __init__(self, faces: np.ndarray):
        """
        Initialize the die with faces and equal weights.

        Parameters
        ----------
        faces : np.ndarray
            An array of faces, either strings or numbers.

        Raises
        ------
        TypeError
            If faces are not a NumPy array.
        ValueError
            If faces are not unique.
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array")
        if len(faces) != len(set(faces)):
            raise ValueError("Faces must be unique")
        
        self.faces = faces
        self.weights = pd.DataFrame({'faces': faces, 'weights': [1.0] * len(faces)}).set_index('faces')

    def change_weight(self, face, weight: float):
        """
        Change the weight of a given face.

        Parameters
        ----------
        face : str or int
            The face whose weight is to be changed.
        weight : float
            The new weight for the face.

        Raises
        ------
        IndexError
            If face is not in the die.
        TypeError
            If weight is not a float.
        """
        if face not in self.weights.index:
            raise IndexError("Face not found in die faces")
        if not isinstance(weight, (float, int)):
            raise TypeError("Weight must be a numeric type")
        
        self.weights.at[face, 'weights'] = weight

    def roll(self, rolls=1):
        """
        Roll the die one or more times.

        Parameters
        ----------
        rolls : int, optional
            Number of times to roll the die, default is 1.

        Returns
        -------
        list
            List of outcomes.
        """
        return self.weights.sample(n=rolls, weights='weights', replace=True).index.tolist()

    def show(self):
        """
        Show the current state of the die.

        Returns
        -------
        pd.DataFrame
            DataFrame with faces and weights.
        """
        return self.weights.copy()



class Game:
    """
    A class representing a game involving rolling multiple dice.

    Attributes
    ----------
    dice : list
        A list of Die objects.
    results : pd.DataFrame
        A DataFrame to store the results of the most recent play.
    """
    
    def __init__(self, dice: list):
        """
        Initialize the game with a list of dice.

        Parameters
        ----------
        dice : list
            A list of Die objects.
        """
        self.dice = dice
        self.results = pd.DataFrame()

    def play(self, rolls: int):
        """
        Roll all dice a given number of times.

        Parameters
        ----------
        rolls : int
            The number of times to roll the dice.
        """
        self.results = pd.DataFrame({i: die.roll(rolls) for i, die in enumerate(self.dice)})

    def show(self, form='wide'):
        """
        Show the results of the most recent play.

        Parameters
        ----------
        form : str, optional
            The format to show the results, either 'wide' or 'narrow'. Default is 'wide'.

        Returns
        -------
        pd.DataFrame
            DataFrame with the results in the specified format.

        Raises
        ------
        ValueError
            If an invalid format is provided.
        """
        if form not in ['wide', 'narrow']:
            raise ValueError("Invalid format. Use 'wide' or 'narrow'.")
        
        if form == 'wide':
            return self.results.copy()
        else:
            return self.results.stack().reset_index(name='face').rename(columns={'level_0': 'roll', 'level_1': 'die'})



class Analyzer:
    """
    A class to analyze the results of a game.

    Attributes
    ----------
    game : Game
        The game object to analyze.
    results : pd.DataFrame
        The results of the game.
    """

    def __init__(self, game: Game):
        """
        Initialize the analyzer with a game object.

        Parameters
        ----------
        game : Game
            A game object to analyze.

        Raises
        ------
        ValueError
            If the passed object is not a Game.
        """
        if not isinstance(game, Game):
            raise ValueError("The input must be a Game object")

        self.game = game
        self.results = game.show()

    def jackpot(self):
        """
        Compute the number of jackpots.

        Returns
        -------
        int
            Number of jackpots.
        """
        return (self.results.nunique(axis=1) == 1).sum()

    def face_counts_per_roll(self):
        """
        Compute the face counts per roll.

        Returns
        -------
        pd.DataFrame
            DataFrame with face counts per roll.
        """
        return self.results.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)

    def combo_count(self):
        """
        Compute the distinct combinations and their counts.

        Returns
        -------
        pd.DataFrame
            DataFrame with distinct combinations and their counts.
        """
        combos = self.results.apply(lambda x: tuple(sorted(x)), axis=1)
        return combos.value_counts().reset_index(name='count').rename(columns={'index': 'combination'})

    def permutation_count(self):
        """
        Compute the distinct permutations and their counts.

        Returns
        -------
        pd.DataFrame
            DataFrame with distinct permutations and their counts.
        """
        permutations = self.results.apply(tuple, axis=1)
        return permutations.value_counts().reset_index(name='count').rename(columns={'index': 'permutation'})







