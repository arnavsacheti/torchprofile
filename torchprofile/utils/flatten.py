from collections import deque
from typing import TYPE_CHECKING

from torch import Tensor

if TYPE_CHECKING:
    from torch import nn,
    from ..typing import NestedTensor


def flatten(inputs: "NestedTensor") -> list[Tensor]:
    queue = deque([inputs])
    outputs: list[Tensor] = []
    while queue:
        x = queue.popleft()
        if isinstance(x, (list, tuple)):
            queue.extend(x)
        elif isinstance(x, dict):
            queue.extend(x.values())
        elif isinstance(x, Tensor):
            outputs.append(x)
    return outputs


class Flatten(nn.Module):
    def __init__(self, model: nn.Module):
        super().__init__()
        self.model = model

    def forward(self, *args, **kwargs):
        outputs = self.model(*args, **kwargs)
        return flatten(outputs)
