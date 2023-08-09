from pydantic import BaseModel

class User(BaseModel):
    title: str
    description: int
    count: str

    @classmethod
    def validate_title(cls, title):
        if len(title) > 128:
            raise ValueError("ValueError")
        return title

    @classmethod
    def validate_descr(cls, description):
        if len(description) > 4096:
            raise ValueError("ValueError")
        return description

    @classmethod
    def validate_count(cls, count):
        if count == int:
            True
        return count