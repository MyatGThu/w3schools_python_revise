# use cmd line pip --version to look up pip version installed

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))