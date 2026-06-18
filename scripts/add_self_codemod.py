"""Add an explicit ``self`` parameter to methods declared inside zope
interface classes in ``.pyi`` stubs.

Zope interfaces declare methods without ``self`` (``def get() -> None``). The
``mypy-zope`` plugin understood that; without it, every type checker treats
the stub class as ordinary and demands ``self``. This codemod prepends
``self`` to each method of an interface-derived class.

Interface detection is base-driven: a class is an interface when any base is
named ``Interface`` or matches the Zope naming convention ``^I[A-Z]`` (e.g.
``IObjectEvent``). This avoids misclassifying concrete classes.

Run it with ``libcst`` available, e.g.::

    uv run --with libcst python scripts/add_self_codemod.py src/plone-stubs/uuid/*.pyi

Pass any number of ``.pyi`` paths; only interface methods are modified and
files without changes are left untouched.
"""

from __future__ import annotations

import re
import sys

import libcst as cst


_INTERFACE_BASE = re.compile(r"^I[A-Z]")


def _base_name(node: cst.BaseExpression) -> str | None:
    """Return the trailing identifier of a base expression, or ``None``.

    :param node: the base-class expression from a ``ClassDef``.
    :returns: the simple name (``Foo`` for both ``Foo`` and ``mod.Foo``).
    """
    if isinstance(node, cst.Name):
        return node.value
    if isinstance(node, cst.Attribute):
        return node.attr.value
    return None


def _is_interface(node: cst.ClassDef) -> bool:
    """Return whether ``node`` declares a zope interface.

    :param node: the class definition to inspect.
    :returns: ``True`` when a base is ``Interface`` or matches ``^I[A-Z]``.
    """
    for base in node.bases:
        name = _base_name(base.value)
        if name == "Interface" or (name and _INTERFACE_BASE.match(name)):
            return True
    return False


class AddSelfTransformer(cst.CSTTransformer):
    """Prepend ``self`` to methods inside interface classes."""

    def __init__(self) -> None:
        self.changed = 0

    def leave_ClassDef(
        self, original: cst.ClassDef, updated: cst.ClassDef
    ) -> cst.ClassDef:
        if not _is_interface(original):
            return updated
        new_body = []
        for stmt in updated.body.body:
            if isinstance(stmt, cst.FunctionDef):
                stmt = self._fix_function(stmt)
            new_body.append(stmt)
        return updated.with_changes(
            body=updated.body.with_changes(body=tuple(new_body))
        )

    def _fix_function(self, func: cst.FunctionDef) -> cst.FunctionDef:
        """Prepend ``self`` to ``func`` unless it is static or already bound.

        :param func: a function defined directly in an interface body.
        :returns: the function with a leading ``self`` parameter when needed.
        """
        # Skip static methods (no implicit first arg).
        for dec in func.decorators:
            if _base_name(dec.decorator) == "staticmethod":
                return func
        params = func.params
        existing = list(params.params)
        if existing and existing[0].name.value in ("self", "cls"):
            return func
        self_param = cst.Param(name=cst.Name("self"))
        # If other params follow, the new first param needs a trailing comma.
        if existing:
            self_param = self_param.with_changes(
                comma=cst.Comma(whitespace_after=cst.SimpleWhitespace(" "))
            )
        self.changed += 1
        return func.with_changes(
            params=params.with_changes(params=[self_param, *existing])
        )


def process(path: str) -> int:
    """Apply the transform to a single stub file in place.

    :param path: path to a ``.pyi`` file.
    :returns: the number of methods that received a ``self`` parameter.
    """
    with open(path) as handle:
        src = handle.read()
    module = cst.parse_module(src)
    transformer = AddSelfTransformer()
    new_module = module.visit(transformer)
    if transformer.changed:
        with open(path, "w") as handle:
            handle.write(new_module.code)
    return transformer.changed


def main(argv: list[str]) -> None:
    """Run the codemod over every path in ``argv`` and report a summary.

    :param argv: the ``.pyi`` paths to process.
    """
    total = 0
    for path in argv:
        n = process(path)
        total += n
        print(f"{path}: +self on {n} method(s)")
    print(f"TOTAL: {total} methods updated")


if __name__ == "__main__":
    main(sys.argv[1:])
