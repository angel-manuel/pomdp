
from pomdp import __version__, __author__

import os
from pathlib import Path
import yaml
import matplotlib as mpl
import matplotlib.pyplot as plt


from pomdp.models import MDP

if __name__ == "__main__":
    print("pomdp: A POMDP solver {} by {}".format(__version__, __author__))

    model_path = Path(os.path.dirname(__file__) +
                      '/../models/test_mdp.yml').resolve()

    mpl.use('TkAgg')

    with open(model_path) as f:
        obj = yaml.load(f)

    mdp = MDP.from_object(obj)

    plt.figure()
    mdp.draw()
    plt.show()
