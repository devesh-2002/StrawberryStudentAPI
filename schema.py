import typing
import strawberry

@strawberry.type
class Student:
    name:str
    roll_no:int
    div:str

@strawberry.type
class Query:
    students:typing.List[Student]

def get_students():
    return [
        Student(
            name="DR",
            roll_no="56",
            div="D20A"
        ),
        Student(
            name="SL",
            roll_no="36",
            div="D20A"
        ),
                Student(
            name="MK",
            roll_no="28",
            div="D20A"
        ),
                Student(
            name="SK",
            roll_no="24",
            div="D20A"
        ),
    ]

@strawberry.type
class Query:
    students: typing.List[Student] = strawberry.field(resolver=get_students)


schema = strawberry.Schema(query=Query)
