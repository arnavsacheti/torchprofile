from typing import TYPE_CHECKING
import warnings

from .handlers import handlers
from .utils.trace import trace

if TYPE_CHECKING:
    from torch import nn, Tensor
    from .typing import ArrayLikeTensor
    from typing import Callable, Any, Iterable, Dict, Optional, Union
    from .utils.ir.node import Node

__all__ = ["profile_macs"]


def profile_macs(
    model: nn.Module,
    args: ArrayLikeTensor = (),
    kwargs: None = None,
    reduction: Optional[Callable[[Iterable[Any]], int]] = sum,
) -> Union[int, Dict[Node, Tensor]]:
    results: Dict[Node, Tensor] = dict()

    graph = trace(model, args, kwargs)
    for node in graph.nodes:
        for operators, func in handlers:
            if isinstance(operators, str):
                operators = [operators]
            if node.operator in operators:
                if func is not None:
                    results[node] = func(node)
                break
        else:
            warnings.warn('No handlers found: "{}". Skipped.'.format(node.operator))

    if reduction is not None:
        return reduction(results.values())
    else:
        return results
