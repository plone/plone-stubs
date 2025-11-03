SAVE_THRESHOLD: int

def remap_workflow(context, type_ids, chain, state_map={}):
    """Change the workflow for each type in type_ids to use the workflow
    chain given. state_map is a dictionary of old state names to
    new ones. States that are not found will be remapped to the default
    state of the new workflow.
    """
