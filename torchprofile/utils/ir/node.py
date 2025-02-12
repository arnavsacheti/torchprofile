from typing import List, Dict, Any
from .variable import Variable


class Node:
    def __init__(
        self,
        operator: str,
        attributes: Dict[str, Any],
        inputs: List[Variable],
        outputs: List[Variable],
        scope: str,
    ):
        self.operator = operator
        self.attributes = attributes
        self.inputs = inputs
        self.outputs = outputs
        self.scope = scope

    @property
    def operator(self) -> str:
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        self._operator = operator.lower()

    @property
    def attributes(self) -> Dict[str, Any]:
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: Dict[str, Any]) -> None:
        self._attributes = attributes

    @property
    def inputs(self) -> List[Variable]:
        return self._inputs

    @inputs.setter
    def inputs(self, inputs: List[Variable]) -> None:
        self._inputs = inputs

    @property
    def outputs(self) -> List[Variable]:
        return self._outputs

    @outputs.setter
    def outputs(self, outputs: List[Variable]) -> None:
        self._outputs = outputs

    @property
    def scope(self) -> str:
        return self._scope

    @scope.setter
    def scope(self, scope: str) -> None:
        self._scope = scope

    def __repr__(self) -> str:
        text = ", ".join([str(v) for v in self.outputs])
        text += " = " + self.operator
        if self.attributes:
            text += (
                "["
                + ", ".join(
                    [str(k) + " = " + str(v) for k, v in self.attributes.items()]
                )
                + "]"
            )
        text += "(" + ", ".join([str(v) for v in self.inputs]) + ")"
        return text
