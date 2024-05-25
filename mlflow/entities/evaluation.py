from typing import Any, Dict, List, Optional

from mlflow.entities._mlflow_object import _MlflowObject
from mlflow.entities.feedback import Feedback
from mlflow.entities.metric import Metric


class Evaluation(_MlflowObject):
    """
    Evaluation result data.
    """

    def __init__(
        self,
        evaluation_id: str,
        run_id: str,
        inputs_id: str,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any],
        request_id: Optional[str] = None,
        ground_truths: Optional[Dict[str, Any]] = None,
        feedback: Optional[List[Feedback]] = None,
        metrics: Optional[List[Metric]] = None,
    ):
        """
        Construct a new mlflow.entities.Evaluation instance.

        Args:
            evaluation_id: A unique identifier for the evaluation result.
            run_id: The ID of the MLflow Run containing the Evaluation.
            inputs_id: A unique identifier for the input names and values for evaluation.
            inputs: Input names and values for evaluation.
            outputs: Outputs obtained during inference.
            request_id: The ID of an MLflow Trace corresponding to the inputs and outputs.
            ground_truths: Expected values that the GenAI app should produce during inference.
            feedback: Feedback for the given row.
            metrics: Objective numerical metrics for the row, e.g., "number of input tokens",
                "number of output tokens".
        """
        self._evaluation_id = evaluation_id
        self._run_id = run_id
        self._inputs_id = inputs_id
        self._inputs = inputs
        self._outputs = outputs
        self._request_id = request_id
        self._ground_truths = ground_truths
        self._feedback = feedback
        self._metrics = metrics

    @property
    def evaluation_id(self) -> str:
        """Get the evaluation ID."""
        return self._evaluation_id

    @property
    def run_id(self) -> str:
        """Get the run ID."""
        return self._run_id

    @property
    def inputs_id(self) -> str:
        """Get the inputs ID."""
        return self._inputs_id

    @property
    def inputs(self) -> Dict[str, Any]:
        """Get the inputs."""
        return self._inputs

    @property
    def outputs(self) -> Dict[str, Any]:
        """Get the outputs."""
        return self._outputs

    @property
    def request_id(self) -> Optional[str]:
        """Get the request ID."""
        return self._request_id

    @property
    def ground_truths(self) -> Optional[Dict[str, Any]]:
        """Get the ground truths."""
        return self._ground_truths

    @property
    def feedback(self) -> Optional[List[Feedback]]:
        """Get the feedback."""
        return self._feedback

    @property
    def metrics(self) -> Optional[List[Metric]]:
        """Get the metrics."""
        return self._metrics

    def __eq__(self, __o):
        if isinstance(__o, self.__class__):
            return self.to_dictionary() == __o.to_dictionary()

        return False

    def to_dictionary(self) -> Dict[str, Any]:
        """
        Convert the Evaluation object to a dictionary.

        Returns:
            dict: The Evaluation object represented as a dictionary.
        """
        evaluation_dict = {
            "evaluation_id": self.evaluation_id,
            "run_id": self.run_id,
            "inputs_id": self.inputs_id,
            "inputs": self.inputs,
            "outputs": self.outputs,
        }
        if self.request_id:
            evaluation_dict["request_id"] = self.request_id
        if self.ground_truths:
            evaluation_dict["ground_truths"] = self.ground_truths
        if self.feedback:
            evaluation_dict["feedback"] = [fb.to_dictionary() for fb in self.feedback]
        if self.metrics:
            evaluation_dict["metrics"] = [metric.to_dictionary() for metric in self.metrics]
        return evaluation_dict

    @classmethod
    def from_dictionary(cls, evaluation_dict: Dict[str, Any]):
        """
        Create an Evaluation object from a dictionary.

        Args:
            evaluation_dict (dict): Dictionary containing evaluation information.

        Returns:
            Evaluation: The Evaluation object created from the dictionary.
        """
        evaluation_id = evaluation_dict["evaluation_id"]
        run_id = evaluation_dict["run_id"]
        inputs_id = evaluation_dict["inputs_id"]
        inputs = evaluation_dict["inputs"]
        outputs = evaluation_dict["outputs"]
        request_id = evaluation_dict.get("request_id")
        ground_truths = evaluation_dict.get("ground_truths")
        feedback = None
        if "feedback" in evaluation_dict:
            feedback = [Feedback.from_dictionary(fb) for fb in evaluation_dict["feedback"]]
        metrics = None
        if "metrics" in evaluation_dict:
            metrics = [Metric.from_dictionary(metric) for metric in evaluation_dict["metrics"]]
        return cls(
            evaluation_id=evaluation_id,
            run_id=run_id,
            inputs_id=inputs_id,
            inputs=inputs,
            outputs=outputs,
            request_id=request_id,
            ground_truths=ground_truths,
            feedback=feedback,
            metrics=metrics,
        )