from kfp import components
from kfp.v2 import compiler, dsl
import config

config = config.PipelineConfig()


@dsl.pipeline(
    name="vertexai-pipeline-image-version-switch",
    description="An example pipeline using Vertex AI Pipelines",
)
def my_pipeline():
    get_data_op = components.load_component_from_file("./components/get_data.yml")
    get_data_op.component_spec.implementation.container.image += (
        ":" + config.pipeline_image_tag
    )
    get_data_task = get_data_op()

    preprocess_op = components.load_component_from_file("./components/preprocess.yml")
    preprocess_op.component_spec.implementation.container.image += (
        ":" + config.pipeline_image_tag
    )
    preprocess_task = preprocess_op(dataset=get_data_task.outputs["dataset"])


if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=my_pipeline,
        package_path="vertexai-pipeline-image-version-switch.json",
    )
