from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint

# Create database connection
# Using SQLite for demonstration since MySQL may not be set up
engine = create_engine('sqlite:///student.db')

# Create metadata
metadata = MetaData()

# Define students table
students = Table('students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('age', Integer, nullable=False),
    Column('city', String(50), nullable=True),
    CheckConstraint('age >= 18', name='age_check')
)

# Create the table
metadata.create_all(engine)

# Insert 3 student records
with engine.connect() as conn:
    # Insert records
    conn.execute(students.insert().values([
        {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'},
        {'name': 'Amit', 'age': 19, 'city': 'Delhi'},
        {'name': 'Priya', 'age': 22, 'city': None},
        {'name': 'Sneha', 'age': 18, 'city': 'Bangalore'} 
    ]))
    conn.commit()

    # Fetch all students
    print("All students after insertion:")
    result = conn.execute(students.select())
    for row in result:
        print(row)

    # Update city of student whose name = "Rahul"
    conn.execute(students.update().where(students.c.name == 'Rahul').values(city='Pune'))
    conn.commit()

    # Fetch all students after update
    print("\nAll students after updating Rahul's city:")
    result = conn.execute(students.select())
    for row in result:
        print(row)

    # Delete student whose age < 20
    conn.execute(students.delete().where(students.c.age < 20))
    conn.commit()

    # Fetch all students after delete
    print("\nAll students after deleting age < 20:")
    result = conn.execute(students.select())
    for row in result:
        print(row)