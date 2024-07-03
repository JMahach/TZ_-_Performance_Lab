import json
import sys


def inserter(tests, values_dict):
    for test in tests:
        if "value" in test and test["id"] in values_dict:
            test["value"] = values_dict[test["id"]]
        if "values" in test:
            inserter(test["values"], values_dict)


if __name__ == "__main__":
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    with open(values_path, "r") as file:
        values = json.load(file)

    with open(tests_path, "r") as file:
        tests = json.load(file)

    values_dict = dict()
    for element in values["values"]:
        values_dict[element["id"]] = element["value"]

    inserter(tests["tests"], values_dict)

    with open(report_path, "w") as file:
        json.dump(tests, file, indent=2)
