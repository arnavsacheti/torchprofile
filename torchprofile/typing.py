from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from torch import Tensor
    from typing import Union, List, Tuple, Dict

    ArrayLikeTensor = Union[
        Tensor,
        List[Tensor],
        Tuple[Tensor, ...],
    ]

    NestedTensor = Union[
        Tensor,
        List["NestedTensor"],
        Tuple["NestedTensor", ...],
        Dict[str, "NestedTensor"],
    ]
