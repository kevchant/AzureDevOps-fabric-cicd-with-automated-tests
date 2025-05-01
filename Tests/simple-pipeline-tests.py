import os
import pytest
from data_factory_testing_framework import TestFramework, TestFrameworkType
from data_factory_testing_framework.models import Pipeline
from data_factory_testing_framework.state import PipelineRunState,RunParameter, RunParameterType


@pytest.fixture
def test_framework(request: pytest.FixtureRequest) -> TestFramework:
    return TestFramework(
        framework_type=TestFrameworkType.Fabric,
        root_folder_path=os.path.dirname(request.fspath.dirname),
    )

@pytest.fixture
def pipeline(test_framework: TestFramework) -> Pipeline:
    return test_framework.get_pipeline_by_name("Run Hello World")

def test_directory_parameter(request: pytest.FixtureRequest, pipeline: Pipeline) -> None:
    # Arrange
    activity = pipeline.get_activity_by_name("Copy sample data")
    state = PipelineRunState(
    parameters=[
        RunParameter(RunParameterType.Pipeline, name="DirectoryName", value="SampleData")
    ],
    )

    # Act
    activity.evaluate(state)

    # Assert to check correct directory name is used
    assert (
        activity.type_properties["sink"]["datasetSettings"]["typeProperties"]["location"]["folderPath"].result
        == "SampleData"
    )