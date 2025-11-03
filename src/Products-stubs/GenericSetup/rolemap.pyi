from .utils import ExportConfiguratorBase
from .utils import ImportConfiguratorBase
from _typeshed import Incomplete

def importRolemap(context) -> None:
    """Import roles / permission map from an XML file.

    o \'context\' must implement IImportContext.

    o Register via Python:

      registry = site.setup_tool.setup_steps
      registry.registerStep(\'importRolemap\', \'20040518-01\',
                            Products.GenericSetup.rolemap.importRolemap,
                            (), \'Role / Permission import\',
                            \'Import roles and map roles to permissions\')

    o Register via XML:

      <setup-step id="importRolemap"
                  version="20040518-01"
                  handler="Products.GenericSetup.rolemap.importRolemap"
                  title="Role / Permission import"
      >Import additional roles, and map roles to permissions.</setup-step>

    """

def exportRolemap(context) -> None:
    """Export roles / permission map as an XML file

    o \'context\' must implement IExportContext.

    o Register via Python:

      registry = site.setup_tool.export_steps
      registry.registerStep(\'exportRolemap\',
                            Products.GenericSetup.rolemap.exportRolemap
                            \'Role / Permission export\',
                            \'Export roles and role / permission map\')

    o Register via XML:

      <export-script id="exportRolemap"
                     version="20040518-01"
                     handler="Products.GenericSetup.rolemap.exportRolemap"
                     title="Role / Permission export"
      >Export additional roles, and role / permission map.</export-script>

    """

class RolemapExportConfigurator(ExportConfiguratorBase):
    """Synthesize XML description of sitewide role-permission settings."""

    security: Incomplete
    def listRoles(self):
        """List the valid role IDs for our site."""
    def listPermissions(self):
        """List permissions for export.

        o Returns a sqeuence of mappings describing locally-modified
          permission / role settings.  Keys include:

          'permission' -- the name of the permission

          'acquire' -- a flag indicating whether to acquire roles from the
              site's container

          'roles' -- the list of roles which have the permission.

        o Do not include permissions which both acquire and which define
          no local changes to the acquired policy.
        """

class RolemapImportConfigurator(ImportConfiguratorBase):
    """Synthesize XML description of sitewide role-permission settings."""

    security: Incomplete
