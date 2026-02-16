from dataclasses import dataclass
from typing import Any
from typing import Literal

__all__ = [
    "AddonInformation",
    "NonInstallableAddons",
    "get",
    "get_addon_ids",
    "get_addons",
    "get_version",
    "install",
    "uninstall",
]

AddonLimitType = Literal[
    "",
    "installed",
    "upgradable",
    "available",
    "non_installable",
    "broken",
]

@dataclass
class NonInstallableAddons:
    """Set of add-ons not available for installation."""

    profiles: list[str]
    products: list[str]

@dataclass
class AddonInformation:
    """Add-on information."""

    id: str
    version: str
    title: str
    description: str
    upgrade_profiles: dict[str, Any]
    other_profiles: list[dict[str, Any]]
    install_profile: dict[str, Any]
    uninstall_profile: dict[str, Any]
    profile_type: str
    upgrade_info: dict[str, Any]
    valid: bool
    flags: list[str]

def get_addons(limit: AddonLimitType = "") -> list[AddonInformation]:
    """List add-ons in this Plone site.

    :param limit: Limit list of add-ons.
    :type limit: AddonLimitType
    :returns: List of AddonInformation.
    """

def get_addon_ids(limit: AddonLimitType = "") -> list[str]:
    """List add-ons ids in this Plone site.

    :param limit: Limit list of add-ons.
    :type limit: AddonLimitType
    :returns: List of add-on ids.
    """

def get_version(addon: str) -> str:
    """Return the version of the product (package).

    :param addon: [required] ID of the add-on.
    :type addon: string
    :returns: Version string.
    """

def get(addon: str) -> AddonInformation:
    """Information about an Add-on.

    :param addon: [required] ID of the add-on to be retrieved.
    :type addon: string
    :returns: Add-on information.
    """

def install(addon: str) -> bool:
    """Install an add-on.

    :param addon: [required] ID of the add-on to be installed.
    :type addon: string
    :returns: Status of the installation.
    """

def uninstall(addon: str) -> bool:
    """Uninstall an add-on.

    :param addon: [required] ID of the add-on to be uninstalled.
    :type addon: string
    :returns: Status of the uninstallation.
    """
