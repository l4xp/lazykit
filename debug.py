import re

from core import context

with open("lazykit/__TestProjDir__/utils.py") as f:
    content = f.read()
print(repr(content))


tree = context.crawl_project_context("lazykit/__TestProjDir__")
for f in tree['children']:
    if f['name'] == 'utils.py':
        print(f['metadata'])


MAGIC_COMMENT_REGEX = re.compile(
    r"(?:#|//|<!--)\s*@kit:(\w+):\s*(.*)"
)

text = "# @kit:name:test\n# @kit:author:Jane Doe\n# @kit:note: test\n"

print(dict(MAGIC_COMMENT_REGEX.findall(text)))
