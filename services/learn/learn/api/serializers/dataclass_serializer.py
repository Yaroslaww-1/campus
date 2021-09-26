import dataclasses


class DataclassSerializer:
    @staticmethod
    def from_json(data, Dataclass):
        return Dataclass(**data)

    @staticmethod
    def to_dict(data, many=False):
        if many:
            return list(map(dataclasses.asdict, data))
        return dataclasses.asdict(data)
