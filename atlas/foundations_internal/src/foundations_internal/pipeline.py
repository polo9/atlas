from .pipeline_context import PipelineContext

class Pipeline(object):

    def __init__(self, pipeline_context=None):
        if pipeline_context is None:
            pipeline_context = PipelineContext()
        self._pipeline_context = pipeline_context

    def pipeline_context(self):
        return self._pipeline_context
