r"""
====================================================================================================
Evaluation
====================================================================================================

:mod:`ruptures.metrics` provides metrics to evaluate change point detection performances and
:mod:`ruptures.show` provides a display function for visual inspection.

.. toctree::
    :glob:
    :maxdepth: 1

    hausdorff
    randindex
    precision
    display

"""

from .hamming import hamming
from .hausdorff import hausdorff
from .precisionrecall import precision_recall
from .randindex import randindex
from .timeerror import meantime
