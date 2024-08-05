# import the ObjectID class
from ..object import ObjectID


# define a vector base class
class VectorBase:
    def __init__(self, model_name) -> None:
        self.model_name = model_name

    async def insert(self, vector: [float], id: ObjectID):
        pass

    async def query(self, vector: [float], top_k: int) -> [ObjectID]:
        pass

    async def delete(self, id: ObjectID):
        pass
