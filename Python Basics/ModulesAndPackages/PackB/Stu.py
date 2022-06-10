class Student:
    def __init__(self, sid, sname, sgrade):
        self.sid = sid
        self.sname = sname
        self.sgrade = sgrade

    def displayStu(self):
        print(self.sid, self.sname, self.sgrade)
