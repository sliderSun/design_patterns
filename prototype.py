import copy
"""
原型模式
模式特点：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。

程序实例：从简历原型，生成新的简历

代码特点：简历类Resume提供的Clone()方法其实并不是真正的Clone，只是为已存在对象增加了一次引用。

　　　　　Python为对象提供的copy模块中的copy方法和deepcopy方法已经实现了原型模式，但由于例子的层次较浅，二者看不出区别。
"""


class WorkExperience:
    def __init__(self):
        self.company = ""
        self.time_area = ""


class Resume:
    def __init__(self, n):
        self.name = n
        self.work_experience = WorkExperience()

    def set_personal_info(self, s, a):
        self.sex = s
        self.age = a

    def set_work_experience(self, c, ta):
        self.work_experience.company = c
        self.work_experience.time_area = ta

    def print_resume(self):
        print self.name + ", " + self.sex + ", " + self.age + ", " \
              + self.work_experience.company + " : " + self.work_experience.time_area

    def clone(self):
        new_resume = copy.deepcopy(self)
        new_resume.work_experience = copy.deepcopy(self.work_experience)
        return new_resume


if __name__ == "__main__":
    resume1 = Resume("Bob")
    resume1.set_personal_info("M", "24")
    resume1.set_work_experience("Google", "2015")
    resume2 = resume1
    resume2.set_personal_info("F", "22")
    resume2.set_work_experience("Twitter", "2015")
    resume1.print_resume()
    resume2.print_resume()

    resume1 = Resume("Bob")
    resume1.set_personal_info("M", "24")
    resume1.set_work_experience("Google", "2015")
    resume2 = copy.copy(resume1)
    resume2.set_personal_info("F", "22")
    resume2.set_work_experience("Twitter", "2015")
    resume1.print_resume()
    resume2.print_resume()

    resume1 = Resume("Bob")
    resume1.set_personal_info("M", "24")
    resume1.set_work_experience("Google", "2015")
    resume2 = copy.deepcopy(resume1)
    resume2.set_personal_info("F", "22")
    resume2.set_work_experience("Twitter", "2015")
    resume1.print_resume()
    resume2.print_resume()

    resume1 = Resume("Bob")
    resume1.set_personal_info("M", "24")
    resume1.set_work_experience("Google", "2015")
    resume2 = resume1.clone()
    resume2.set_personal_info("F", "22")
    resume2.set_work_experience("Twitter", "2015")
    resume1.print_resume()
    resume2.print_resume()
