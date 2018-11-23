"""
    Tests for direct_naive function
"""

import numpy as np
import pytest

from pyssa.simulation import Simulation


def test_plotting(setup_basic):
    V_r, V_p, X0, k = setup_basic
    n_runs = 10
    sim1 = Simulation(V_r, V_p, X0, k)
    sim1.simulate(max_t=150, max_iter=1000, chem_flag=True, n_rep=n_runs)
    sim1.plot()
    assert 1==1