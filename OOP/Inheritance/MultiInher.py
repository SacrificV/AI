class Student:
    def __init__(self, sid: int, deptid: int):
        self.sid = sid
        self.deptid = deptid
    def get_info(self) -> str:
        return f"StudentID:{self.sid} DepartmentID:{self.deptid}"
class Faculty:
    def __init__(self, eid: int, deptid: int):
        self.eid = eid
        self.deptid = deptid

    def get_info(self) -> str:
        return f"EmployeeID:{self.eid} DepartmentID:{self.deptid}"

class PhDStudent(Student, Faculty):
    def __init__(self, sid: int, eid: int, deptid: int):
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)

    def get_info(self) -> str:
        return (
            f"StudentID:{self.sid} "
            f"EmployeeID:{self.eid} "
            f"DepartmentID:{self.deptid}"
        )

p = PhDStudent(101, 555, 42)
print(p.get_info())
