def ToolWorkflowChain(context, workflow_tool):
    """Looks up the workflow chain by portal type suing a mapping
     stored on the tool::

       >>> from Products.CMFPlone.tests.dummy import DummyContent, DummyWorkflowTool
       >>> tool = DummyWorkflowTool()
       >>> content = DummyContent(id='dummy', portal_type='DummyType')

     Either an object with a portal_type or the portal_type as a
     string.  If we pass in an unknown portal_type we get the default
     chain::

       >>> ToolWorkflowChain('A Type', tool)
       ('Default Workflow',)
       >>> tool.setChainForPortalTypes(('A Type',), ('Some Workflow',))
       >>> ToolWorkflowChain('A Type', tool)
       ('Some Workflow',)

     When we pass in a piece of content we get similar behavior::

       >>> ToolWorkflowChain(content, tool)
       ('Default Workflow',)
       >>> tool.setChainForPortalTypes(('DummyType',), ('Some Workflow',))
       >>> ToolWorkflowChain(content, tool)
       ('Some Workflow',)

    If we can't figure out a portal_type then we return an empty chain::

       >>> ToolWorkflowChain((), tool)
       ()

    """
