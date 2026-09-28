# %%
from ruamel.yaml import YAML

fname = "example.yaml"

yaml = YAML()
with open(fname, "r") as f:
    content = yaml.load(f)
print(content)
# %%
