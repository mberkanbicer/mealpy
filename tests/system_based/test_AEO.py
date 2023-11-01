#!/usr/bin/env python
# Created by "Thieu" at 23:02, 19/03/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from mealpy import FloatVar, AEO, Optimizer
import numpy as np
import pytest


@pytest.fixture(scope="module")  # scope: Call only 1 time at the beginning
def problem():
    def objective_function(solution):
        return np.sum(solution ** 2)

    problem = {
        "obj_func": objective_function,
        "bounds": FloatVar(lb=[-10, -15, -4, -2, -8], ub=[10, 15, 12, 8, 20]),
        "minmax": "min",
    }
    return problem


def test_AEO_results(problem):
    models = [
        AEO.AugmentedAEO(epoch=100, pop_size=50),
        AEO.OriginalAEO(epoch=10, pop_size=50),
        AEO.ModifiedAEO(epoch=10, pop_size=50),
        AEO.EnhancedAEO(epoch=10, pop_size=50),
        AEO.ImprovedAEO(epoch=10, pop_size=50)
    ]
    for model in models:
        g_best = model.solve(problem)
        assert isinstance(model, Optimizer)
        assert isinstance(g_best.solution, np.ndarray)
        assert len(g_best.solution) == len(model.problem.lb)
