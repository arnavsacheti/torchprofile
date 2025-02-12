from typing import List
from .variable import Variable
from .node import Node


class Graph:
    def __init__(
        self,
        name: str,
        variables: List[Variable],
        inputs: List[Variable],
        outputs: List[Variable],
        nodes: List[Node],
    ):
        self.name = name
        self.variables = variables
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = nodes

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def variables(self) -> List[Variable]:
        return self._variables

    @variables.setter
    def variables(self, variables: List[Variable]) -> None:
        self._variables = variables

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
    def nodes(self) -> List[Node]:
        return self._nodes

    @nodes.setter
    def nodes(self, nodes: List[Node]) -> None:
        self._nodes = nodes

    def __repr__(self) -> str:
        text = self.name
        text += " (" + "\n"
        text += ",\n".join(["\t" + str(v) for v in self.inputs]) + "\n"
        text += "):" + "\n"
        text += "\n".join(["\t" + str(x) for x in self.nodes]) + "\n"
        text += "\t" + "return " + ", ".join([str(v) for v in self.outputs])
        return text
