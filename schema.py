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

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_student(self, name: str, roll_no: int, div:str) -> Student:
        print(f"Adding Name : {name}, Roll No : {roll_no}, Div : {div}")
 
        return Student(name=name, roll_no=roll_no, div=div)

schema = strawberry.Schema(query=Query,mutation=Mutation)
