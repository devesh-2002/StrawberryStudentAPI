import typing
import strawberry
import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-south-1')
table_name = 'studentTable'
@strawberry.type
class Student:
    name:str
    roll_no:int
    div:str

@strawberry.type
class Query:
    students:typing.List[Student]

def get_students():
    response = dynamodb.scan(TableName=table_name)
    items = response.get('Items', [])
    students = []
    for item in items:
        name = item.get('name', {}).get('S', '')  
        roll_no = int(item.get('roll_no', {}).get('N', '0'))  
        div = item.get('div', {}).get('S', '') 
        student = Student(name=name, roll_no=roll_no, div=div)
        students.append(student)
    return students


@strawberry.type
class Query:
    students: typing.List[Student] = strawberry.field(resolver=get_students)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_student(self, name: str, roll_no: int, div:str) -> Student:
        print(f"Adding Name : {name}, Roll No : {roll_no}, Div : {div}")
        item = {'name': {'S':name}, 'roll_no': {'N':str(roll_no)}, 'div': {'S':div}}
        dynamodb.put_item(TableName=table_name,Item=item)
        return Student(name=name, roll_no=roll_no, div=div)

schema = strawberry.Schema(query=Query,mutation=Mutation)
