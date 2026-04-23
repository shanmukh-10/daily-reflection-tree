import csv

# Load TSV file
FILE_PATH = "tree/reflection-tree.tsv"

nodes = {}
children = {}

with open(FILE_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for row in reader:
        node_id = row["id"].strip()
        nodes[node_id] = row

        parent = row["parentId"].strip()
        if parent and parent != "null":
            children.setdefault(parent, []).append(node_id)

# Store answers and signals
answers = {}
scores = {
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0},
    "axis3": {"self": 0, "others": 0}
}


def apply_signal(signal):
    if signal:
        signal = signal.strip()
        if ":" in signal:
            axis, side = signal.split(":")
            if axis in scores and side in scores[axis]:
                scores[axis][side] += 1


def get_dominant(axis):
    data = scores[axis]
    return max(data, key=data.get)


def run_node(node_id):
    while node_id:
        node = nodes[node_id]
        node_type = node["type"].strip()
        text = node["text"].strip()
        signal = node["signal"].strip()

        apply_signal(signal)

        # START / REFLECTION / BRIDGE / END
        if node_type in ["start", "reflection", "bridge", "end"]:
            print("\n" + text)

            if node_type == "bridge":
                node_id = node["target"].strip()
            elif node_type == "end":
                break
            else:
                node_id = children.get(node_id, [None])[0]

        # QUESTION NODE
        elif node_type == "question":
            print("\n" + text)

            options = node["options"].split("|")
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")

            while True:
                try:
                    choice = int(input("Choose option: "))
                    if 1 <= choice <= len(options):
                        answers[node_id] = options[choice - 1]
                        break
                except:
                    pass
                print("Invalid choice. Try again.")

            node_id = children.get(node_id, [None])[0]

        # DECISION NODE
        elif node_type == "decision":
            rules = node["options"].split(";")

            parent = node["parentId"].strip()
            previous_answer = answers[parent]

            next_node = None

            for rule in rules:
                left, target = rule.split(":")
                choices = left.replace("answer=", "").split("|")

                if previous_answer in choices:
                    next_node = target.strip()
                    break

            node_id = next_node

        # SUMMARY NODE
        elif node_type == "summary":
            final_text = text.replace(
                "{axis1.dominant}", get_dominant("axis1")
            ).replace(
                "{axis2.dominant}", get_dominant("axis2")
            ).replace(
                "{axis3.dominant}", get_dominant("axis3")
            )

            print("\n" + final_text)
            node_id = children.get(node_id, [None])[0]


# Start Program
run_node("START")
