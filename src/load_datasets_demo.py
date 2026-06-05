from datasets import load_dataset

datasets_to_load = [
    ("imdb", None),
    ("tweet_eval", "sentiment"),
    ("dbpedia_14", None)
]

for dataset_name, config in datasets_to_load:
    print("\n" + "=" * 80)

    try:
        if config:
            dataset = load_dataset(dataset_name, config)
            print(f"DATASET: {dataset_name} ({config})")
        else:
            dataset = load_dataset(dataset_name)
            print(f"DATASET: {dataset_name}")

        print("=" * 80)

        print("Available Splits:")
        print(list(dataset.keys()))

        for split_name in dataset.keys():
            split = dataset[split_name]

            print(f"\nSplit: {split_name}")
            print(f"Number of Samples: {len(split)}")
            print(f"Column Names: {split.column_names}")

        features = dataset[list(dataset.keys())[0]].features

        if "label" in features:
            print("\nLabel Names:")
            print(features["label"].names)

    except Exception as e:
        print(f"Failed to load {dataset_name}")
        print(e)