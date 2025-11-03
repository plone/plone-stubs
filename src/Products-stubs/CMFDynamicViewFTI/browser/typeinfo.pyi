from Products.CMFCore.browser.typeinfo import FactoryTypeInformationAddView
from Products.CMFDynamicViewFTI import DynamicViewTypeInformation

class DVFactoryTypeInformationAddView(FactoryTypeInformationAddView):
    """See FactoryTypeInformationAddView that does all the job"""

    klass = DynamicViewTypeInformation
    description: str
