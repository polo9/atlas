
def deploy_job(foundations_context, job_name, job_params):
    from foundations_contrib.global_state import deployment_manager, log_manager
    from foundations_contrib.deployment_wrapper import DeploymentWrapper

    logger = log_manager.get_logger(__name__)
    logger.info("Job submission started. Ctrl-C to cancel.")

    from foundations_internal.pipeline_context_wrapper import PipelineContextWrapper
    pipeline_context_wrapper = PipelineContextWrapper(
        foundations_context.pipeline_context()
    )

    job_deployment = deployment_manager.simple_deploy(pipeline_context_wrapper, job_name, job_params)
    return DeploymentWrapper(job_deployment)