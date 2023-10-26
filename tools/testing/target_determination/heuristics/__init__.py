from typing import List

from tools.testing.target_determination.heuristics.correlated_with_historical_failures import (
    CorrelatedWithHistoricalFailures,
)
from tools.testing.target_determination.heuristics.edited_by_pr import EditedByPR
from tools.testing.target_determination.heuristics.historical_class_failure_correlation import (
    HistoricalClassFailurCorrelation,
)

from tools.testing.target_determination.heuristics.interface import (
    AggregatedHeuristics as AggregatedHeuristics,
    HeuristicInterface as HeuristicInterface,
    TestPrioritizations as TestPrioritizations,
)

# Heuristics
from tools.testing.target_determination.heuristics.previously_failed_in_pr import (
    PreviouslyFailedInPR,
)

# All currently running heuristics.
# To add a heurstic in trial mode, specify the keywork argument `trial_mode=True`.
HEURISTICS: List[HeuristicInterface] = [
    PreviouslyFailedInPR(),
    EditedByPR(),
    HistoricalClassFailurCorrelation(),
    CorrelatedWithHistoricalFailures(),
]
