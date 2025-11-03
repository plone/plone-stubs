from _typeshed import Incomplete

import zope.interface

OVERRIDE_RESOURCE_DIRECTORY_NAME: str

class IResourceRegistry(zope.interface.Interface):
    url: Incomplete
    js: Incomplete
    css: Incomplete
    init: Incomplete
    deps: Incomplete
    export: Incomplete
    conf: Incomplete

class IBundleRegistry(zope.interface.Interface):
    jscompilation: Incomplete
    csscompilation: Incomplete
    expression: Incomplete
    enabled: Incomplete
    depends: Incomplete
    load_async: Incomplete
    load_defer: Incomplete
    compile: Incomplete
    resources: Incomplete
    last_compilation: Incomplete
    develop_javascript: Incomplete
    develop_css: Incomplete
    stub_js_modules: Incomplete
    merge_with: Incomplete
