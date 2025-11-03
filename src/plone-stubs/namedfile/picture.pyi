from _typeshed import Incomplete

logger: Incomplete
appendix_re: Incomplete
resolveuid_re: Incomplete

def get_allowed_scales(): ...
def get_picture_variants(): ...

class Img2PictureTag:
    def get_scale_name(self, scale_line): ...
    def get_scale_width(self, scale):
        """get width from allowed_scales line
        large 800:65536
        """
    def create_picture_tag(
        self,
        sourceset,
        attributes,
        uid=None,
        fieldname=None,
        resolve_urls: bool = False,
    ):
        """Converts the img tag to a picture tag with picture_variant definition"""
    def resolve_uid_url(self, href): ...
    def update_src_scale(self, src, scale): ...
