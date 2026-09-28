# %%
from ruaml.yaml import YAML

fname = example.yaml

yaml = YAML()
content = yaml.load(fname)
print(content)