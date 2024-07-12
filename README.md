# ds5100-finalproject-lgr2sge
DS5100 final project


Title: Montecarlo Simulator 
Author: Lea Runesha


Synopsis: This montecarlo simulator package provides the necessary tools for simulating and analyzing dice games and other probabilistic scenarios. 


Installation: 

'''bash

pip install -e . 

'''


Import: 

'''python 

import numpy as np
import pandas as pd
from montecarlo.montecarlo import Die, Game, Analyzer

'''


Code Snippets: 

'''python

faces = np.array([1,2,3,4,5,6])
die1 = Die(faces)
die2 = Die(faces)


game = Game([die1, die2])
game.play(10)


analyzer = Analyzer(game)
jackpot_count = analyzer.jackpot()
face_counts = analyzer.face_counts_per_roll()
combo_counts = analyzer.combo_count()
permutation_counts = analyzer.permutation_counts()

'''



API Description: 

Die Class - a class representing a die with N faces and associated weights 
	Attributes
    ----------
    faces : np.ndarray
        A NumPy array of faces of the die.
    weights : pd.DataFrame
        A DataFrame containing the faces and their respective weights.


	Methods:
		- __init__(self, faces: np.ndarray) : Initialize the die with faces and equal weights.

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

		- change_weight(self, face, weight: float) : Change the weight of a given face.

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

		- roll(self, rolls = 1) : Roll the die one or more times.

        Parameters
        ----------
        rolls : int, optional
            Number of times to roll the die, default is 1.

        Returns
        -------
        list
            List of outcomes.

		- show(self) : Show the current state of the die.

        Returns
        -------
        pd.DataFrame
            DataFrame with faces and weights.





Game Class - a class representing a game involving rolling multiple dice
	Attributes
    ----------
    dice : list
        A list of Die objects.
    results : pd.DataFrame
        A DataFrame to store the results of the most recent play.


	Methods: 
		- __init__(self, dice: list) : Initialize the game with a list of dice.

        Parameters
        ----------
        dice : list
            A list of Die objects.

		- play(self, n_rolls) : Roll all dice a given number of times.

        Parameters
        ----------
        rolls : int
            The number of times to roll the dice.

		- show(self, form = 'wide') : Display the results of the game in the specified format.
        
        Parameters:
        form (str): The format to display the results in. 
            'wide' returns the original DataFrame format.
            'narrow' returns a melted DataFrame with 'Die' and 'Face' columns.
            
        Returns:
        pd.DataFrame: The game results in the specified format.
        
        Raises:
        ValueError: If the form specified is neither 'wide' nor 'narrow'.



Analyzer Class - a class to analyze the results of a game object 
	Attributes
    ----------
    game : Game
        The game object to analyze.
    results : pd.DataFrame
        The results of the game.

	Methods: 
		- __init__(self, game: Game) : Initialize the analyzer with a game object.

        Parameters
        ----------
        game : Game
            A game object to analyze.

        Raises
        ------
        ValueError
            If the passed object is not a Game.

		- jackpot(self) : Compute the number of jackpots.

        Returns
        -------
        int
            Number of jackpots.

		- face_counts_per_roll(self) : Compute the face counts per roll.

        Returns
        -------
        pd.DataFrame
            DataFrame with face counts per roll.

		- combo_count(self) : Compute the distinct combinations and their counts.

        Returns
        -------
        pd.DataFrame
            DataFrame with distinct combinations and their counts.

		- permutation_count(self) : Compute the distinct permutations and their counts.

        Returns
        -------
        pd.DataFrame
            DataFrame with distinct permutations and their counts. 









