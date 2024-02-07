import json

from .constant import DATASETS_MAP
from .utils import jarvis_dataset_to_mp, make_validation


def main():
    for k, v in DATASETS_MAP.items():
        with open(v['path']) as f:
            dataset = json.load(f)
        _ = jarvis_dataset_to_mp(dataset, v['label'], v['structure'], k, save=True)

    _ = make_validation(random_seed=114514, save=True)

    metadata = {
        'version': 'v1.0.1',
        'random_seed': 114514,
        'author': 'Hongyi Wang',
    }

    with open('metadata_jarvisbench.json', 'w+') as f:
        json.dump(metadata, f)


if __name__ == '__main__':
    main()
