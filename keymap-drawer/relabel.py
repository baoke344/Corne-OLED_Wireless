import sys, yaml
d = yaml.safe_load(open(sys.argv[1]))
def fix(x):
    if isinstance(x, str):
        return x.replace("⌘", "⊞").replace("⌥", "Alt").replace("Spotlight", "Input")
    if isinstance(x, dict):
        return {k: fix(v) for k, v in x.items()}
    if isinstance(x, list):
        return [fix(v) for v in x]
    return x
for layer in ("Win", "WNav"):
    d["layers"][layer] = fix(d["layers"][layer])
yaml.safe_dump(d, open(sys.argv[1], "w"), allow_unicode=True, sort_keys=False, width=200)
