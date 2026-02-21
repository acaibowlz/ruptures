r"""CostL2 (least squared deviation)"""

import numpy as np
from numpy.typing import NDArray
from typing_extensions import Self

from ruptures.base import BaseCost
from ruptures.costs import NotEnoughPoints


class CostL2(BaseCost):
    r"""Least squared deviation."""

    model = "l2"

    def __init__(self) -> None:
        """Initialize the object."""
        self.signal = None
        self.min_size = 1

    def fit(self, signal: NDArray[np.number]) -> Self:
        """Set parameters of the instance.

        Args:
            signal (array): array of shape (n_samples,) or (n_samples, n_features)

        Returns:
            self
        """
        if signal.ndim == 1:
            self.signal = signal.reshape(-1, 1)
        else:
            self.signal = signal

        return self

    def error(self, start: int, end: int) -> float:
        """Return the approximation cost on the segment [start:end].

        Args:
            start (int): start of the segment
            end (int): end of the segment

        Returns:
            segment cost

        Raises:
            NotEnoughPoints: when the segment is too short (less than `min_size` samples).
        """
        if end - start < self.min_size:
            raise NotEnoughPoints

        return self.signal[start:end].var(axis=0).sum() * (end - start)
