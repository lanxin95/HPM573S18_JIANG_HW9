from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import InputData as Data
import scr.MarkovClasses as MarkovCls
import scr.RandomVariantGenerators as Random
import scr.ProbDistParEst as Est


class HealthStats(Enum):
    """ health states of patients with HIV """
    Well = 0
    Stroke = 1
    PostStroke = 2
    DEATH = 3


class Therapies(Enum):
    """ nodrug vs. anticoagulation """
    nodrug = 0
    anticoagulation = 1


class ParametersFixed():
    def __init__(self, drug):

        # selected therapy
        self._drug = drug

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.Well

        # transition probability from input data
        self._prob_matrix =Data.Prob_MATRIX
        # update the transition probability matrix if anticoagulation is being used
        if self._drug == Therapies.anticoagulation:
            self._prob_matrix = Data.Prob_DRUG_MATRIX


    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

