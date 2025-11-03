def PlacefulWorkflowChain(ob, tool):
    """Monkey-patched by CMFPlacefulWorkflow to look for placeful workflow configurations.

    Goal: find a workflow chain in a policy

    Steps:
    1. ask the object if it contains a policy
    2. if it does, ask him for a chain
    3. if there's no chain for the type the we loop on the parent
    4. if the parent is the portal object or None we stop and ask
       portal_workflow
    """
