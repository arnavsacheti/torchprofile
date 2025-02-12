import operator
from functools import reduce
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Iterable
    from torch import Tensor


def prod(iterable: Iterable[Tensor]) -> Tensor:
    return reduce(operator.mul, iterable, 1)
