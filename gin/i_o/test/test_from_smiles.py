import pytest
from gin.i_o.from_smiles import *
import numpy as np
import numpy.testing as npt


def test_ethane():
    atoms, adjacency_map = smiles_to_organic_topological_molecule('CC')
    npt.assert_almost_equal(
        adjacency_map.numpy(),
        np.array(
            [[0, 1],
             [0, 0]]))
    npt.assert_almost_equal(
        atoms.numpy(),
        np.array(
            [0, 0]))

def test_ethene():
    atoms, adjacency_map = smiles_to_organic_topological_molecule('C=C')
    npt.assert_almost_equal(
        adjacency_map.numpy(),
        np.array(
            [[0, 2],
             [0, 0]]))
    npt.assert_almost_equal(
        atoms.numpy(),
        np.array(
            [0, 0]))

def test_ethnol():
    atom, adjacency_map = smiles_to_organic_topological_molecule('CCO')
    npt.assert_almost_equal(
        adjacency_map.numpy(),
        np.array(
            [[0, 1, 0],
             [0, 0, 1],
             [0, 0, 0]]))
    npt.assert_almost_equal(
        atom.numpy(),
        [0, 0, 2])

def test_isobutane():
    atom, adjacency_map = smiles_to_organic_topological_molecule('CC(C)C')
    npt.assert_almost_equal(
        adjacency_map.numpy(),
        np.array(
            [[0, 1, 0, 0],
             [0, 0, 1, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]))
    npt.assert_almost_equal(
        atom.numpy(),
        [0, 0, 0, 0])

def test_cyclohexane():
    atoms, adjacency_map = smiles_to_organic_topological_molecule('C1CCCCC1')
    npt.assert_almost_equal(
        adjacency_map.numpy(),
        np.array(
        [[0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0]], dtype=np.float32))

    npt.assert_almost_equal(
        atoms.numpy(),
        np.array([0, 0, 0, 0, 0, 0]))

def test_isobutyl_acetate():
    atoms, adjacency_map = smiles_to_organic_topological_molecule(
        'O=C(OCC(C)C)C')
    npt.assert_almost_equal(
        adjacency_map.numpy(),
        np.array(
            [[0, 2, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]))
    npt.assert_almost_equal(
        atoms.numpy(),
        np.array([2, 0, 2, 0, 0, 0, 0, 0]))

def test_benzene():
    atoms, adjacency_map = smiles_to_organic_topological_molecule('c1ccccc1')
    npt.assert_almost_equal(
        adjacency_map.numpy(),
        np.array(
        [[0, 0.5, 0, 0, 0, 0.5],
         [0, 0, 0.5, 0, 0, 0],
         [0, 0, 0, 0.5, 0, 0],
         [0, 0, 0, 0, 0.5, 0],
         [0, 0, 0, 0, 0, 0.5],
         [0, 0, 0, 0, 0, 0]], dtype=np.float32))

    npt.assert_almost_equal(
        atoms.numpy(),
        np.array([0, 0, 0, 0, 0, 0]))