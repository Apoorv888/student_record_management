class Node:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, name, roll_no, grade):
        new_node = Node(name, roll_no, grade)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def get_students(self):
        students = []
        current = self.head
        while current:
            students.append({
                'name': current.name,
                'roll_no': current.roll_no,
                'grade': current.grade
            })
            current = current.next
        return students

    def delete_student(self, roll_no):
        temp = self.head

        if temp is not None:
            if temp.roll_no == roll_no:
                self.head = temp.next
                return

        prev = None
        while temp is not None and temp.roll_no != roll_no:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def update_student(self, roll_no, new_grade):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.grade = new_grade
                return
            current = current.next
