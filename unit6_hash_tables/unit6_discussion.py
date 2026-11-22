"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    release_dates = {}
    release_dates["GTA6"] = 2026
    release_dates["Mario64"] = 1996
    release_dates["Halo: Combat Evolved"] = 2001
    release_dates["Hallow Knight"] = 2017
    release_dates["Portal 2"] = 2011

    print("\n=== INSERT OPERATIONS ===")
    print("Creating a dictionary and adding 5 key value pairs")
    print(release_dates)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("Demonstrating lookup process")
    print(f"Release date of Mario64: {release_dates.get("Mario64")}")
    print(f"Release date of Portal2: {release_dates.get("Portal 2")}")
    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Updating the release fate of Mario64 to 1997 for European release")
    release_dates["Mario64"] = 1997
    print(release_dates)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Deleting Halo: Combat Evolved from the dictionary")
    del release_dates["Halo: Combat Evolved"]
    print(release_dates)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("Demonstrating looking up missing key")

    print(f"Searching for release data of LOZ Ocarina of Time: {release_dates.get("LOZ Ocarina of Time")}")
    print("Updating the value of Portal results in inserting a new entry to the dictionary")
    release_dates["Portal"] = 2010
    print(release_dates)


if __name__ == "__main__":
    main()