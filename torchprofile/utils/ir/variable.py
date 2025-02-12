from typing import List, Optional


class Variable:
    def __init__(self, name: str, dtype: str, shape: Optional[list[int]] = None):
        self.name = name
        self.dtype = dtype
        self.shape = shape

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def dtype(self) -> str:
        return self._dtype

    @dtype.setter
    def dtype(self, dtype: str) -> None:
        self._dtype = dtype.lower()

    @property
    def shape(self) -> Optional[List[int]]:
        return self._shape

    @shape.setter
    def shape(self, shape: Optional[List[int]]) -> None:
        self._shape = shape

    @property
    def ndim(self) -> int:
        return len(self.shape) if self.shape else 0

    def size(self) -> Optional[List[int]]:
        return self.shape

    def dim(self) -> int:
        return self.ndim

    def __repr__(self) -> str:
        text = "%" + self.name + ": " + self.dtype
        if self.shape is not None:
            text += "[" + ", ".join([str(x) for x in self.shape]) + "]"
        return text
