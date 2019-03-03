import unittest

import os
from pathlib import Path
import yaml

from pomdp.models import MDP


class MDPTests(unittest.TestCase):
    def test_from_obj(self):
        model_path = Path(os.path.dirname(__file__) +
                          '/../models/test_mdp.yml').resolve()
        print(model_path)
        with open(model_path) as f:
            obj = yaml.load(f)

        mdp = MDP.from_object(obj)

        self.assertEqual(mdp.name, 'unnamed')
        self.assertEqual(mdp.get_state('A').name, 'A')
        self.assertEqual(mdp.get_state('A').get_action('right').reward, 0.0)
        self.assertEqual(mdp.get_state('C').get_action('nothing').reward, 1.0)
