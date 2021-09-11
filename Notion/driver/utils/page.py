from typing import Dict
import pandas as pd
from .property import Property
from .block import BlockObject


class PageProperties:
    def __init__(self, properties: Dict):
        self.raw = properties

    def __getitem__(self, key):
        return Property(self.raw[key]).extract()

    def __setitem__(self, key, value):
        return Property(self.raw[key]).insert(value)

    def get(self) -> pd.Series:
        data = {key: self[key] for key in self.raw.keys()}
        return pd.Series(data)

    def __repr__(self) -> str:
        return f"{self.get()}"


class PageContent:
    def __init__(self, blocks) -> None:
        self.raw = [block for block in blocks]

    def __getitem__(self, index):
        return BlockObject(self.raw[index]).extract()

    def __setitem__(self, index, value):
        return BlockObject(self.raw[index]).insert(value)

    def get(self) -> pd.DataFrame:
        result = []
        for block in self.raw:
            block = BlockObject(block)
            result.append(
                {
                    "type": block.type,
                    "content": block.extract(),
                    "id": block.id,
                }
            )
        return pd.DataFrame(result)

    def __repr__(self) -> str:
        return f"{self.get()}"

    def _repr_html_(self):
        return self.get().to_html()
