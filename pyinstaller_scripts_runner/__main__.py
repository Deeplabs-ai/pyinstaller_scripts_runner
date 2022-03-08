import importlib.util
import json
import os
import creopyson


def main():
    main_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(main_path, "scripts", "spec.json")) as f:
        spec = json.load(f)

    list_scripts = spec['list_scripts']
    for item in list_scripts:
        module = importlib.util.spec_from_file_location(item['name'].replace('.py', ''),
                                                        os.path.join(main_path,
                                                                     "scripts",
                                                                     item['name']))
        foo = importlib.util.module_from_spec(module)
        module.loader.exec_module(foo)

        for func in item['funcs']:
            getattr(foo, func)()
