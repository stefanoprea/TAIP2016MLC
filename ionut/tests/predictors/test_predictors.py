from __future__ import absolute_import

import os
import unittest

from predictors.alina import synonyms, wup_similarity
from predictors.raluca import levenshtein_distance
from predictors.razvan import definition

os.environ['LEX_JAR'] = '/Users/ihulub/repos/lex/resources/definitions.jar'
os.environ['LEX_VECTOR'] = '/Users/ihulub/repos/lex/resources/glove.6B.300d.txt'


class TestPredictors(unittest.TestCase):
    """Class for testing the predictors"""

    def test_synonyms_returns_4_on_synonyms(self):
        result = synonyms('courage', 'bravery')
        self.assertEqual(result, 4)

    def test_synonyms_returns_0_on_not_synonyms(self):
        result = synonyms('lion', 'tiger')
        self.assertEqual(result, 0)

    def test_wup_similarity_nominal(self):
        result = wup_similarity('lion', 'tiger')
        self.assertEqual(round(result, 2), 2.09)

    def test_levenshtein_distance_nominal(self):
        result = levenshtein_distance('cat', 'cat')
        self.assertEqual(result, 4)

    def test_definition_nominal(self):
        result = definition('ice', 'water')
        self.assertEqual(result, 3.5)
