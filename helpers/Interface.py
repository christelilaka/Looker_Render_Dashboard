from abc import ABC, abstractclassmethod
import looker_sdk

class Interface(ABC):
    sdk = looker_sdk.init31()
    models = looker_sdk.sdk.api31.models

    @classmethod
    @abstractclassmethod
    def make_call(cls):
        pass