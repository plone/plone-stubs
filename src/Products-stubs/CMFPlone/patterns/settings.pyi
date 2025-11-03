from _typeshed import Incomplete

class PatternSettingsAdapter:
    """
    Provides default plone settings relevant for patterns.
    """

    request: Incomplete
    context: Incomplete
    field: Incomplete
    def __init__(self, context, request, field) -> None: ...
    def __call__(self): ...
    def structure_updater(self):
        """Generate the options for the structure updater pattern.
        If we're not in folder contents view, do not expose these options.
        """
    def mark_special_links(self): ...
    @property
    def image_scales(self): ...
    @property
    def picture_variants(self): ...
    @property
    def image_captioning(self): ...
    def tinymce(self):
        """
        data-pat-tinymce : JSON.stringify({
            relatedItems: {
              vocabularyUrl: config.portal_url +
                '/@@getVocabulary?name=plone.app.vocabularies.Catalog'
            },
            tiny: config,
            prependToUrl: 'resolveuid/',
            linkAttribute: 'UID',
            prependToScalePart: '/@@images/image/'
          })
        """
