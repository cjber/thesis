def remove_entries(bib_file, keys_to_remove, output_file):
    with open(bib_file) as f:
        entries = f.read().split("\n\n")

    with open(keys_to_remove) as f:
        keys = set(f.read().splitlines())

    remaining_entries = [
        entry for entry in entries if any(key in entry for key in keys)
    ]

    with open(output_file, "w") as f:
        f.write("\n\n".join(remaining_entries))


# Usage example
remove_entries("references.bib", "bib_keys", "refs_clean.bib")
