def get_translation_group(content):
    """Get the translation group.

    :param content: Content object which is part of the translation group.
    :type content: Content object
    :returns: UID string identifier of the translation group
    :raises:
        ValueError
    """

def get_translation_manager(content):
    """Get the translation manager.

    :param content: Content for which the translation manager is needed.
    :type content: Content object
    :returns: translation manager instance.
    :raises:
        ValueError
    """

def translate(content, target_language: str = "en"):
    """Translate content into target language.

    :param content: Content to be translated.
    :type content: Content object
    :param target_language: Language to be translated to.
    :type target_language: String
    :returns: Content object in new language
    """

def is_translatable(content):
    """Checks if content is translatable.

    :param content: Content to be translated.
    :type content: Content object
    :returns: Boolean
    """
