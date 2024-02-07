from .jarvisbench_tasks import DATASETS_TASKS


class MatbenchBenchmark:
    def __init__(self, **kwargs):
        for k in DATASETS_TASKS.keys():
            setattr(self, k, DATASETS_TASKS[k])
            print()

    @property
    def tasks(self):
        return DATASETS_TASKS.values()

    def from_preset(self, name, **kwargs):
        return self

    def add_metadata(self, metadata, **kwargs):
        return 0

    def from_file(self):
        return 0

    def to_file(self, path, load_history=True, **kwargs):
        return 0
