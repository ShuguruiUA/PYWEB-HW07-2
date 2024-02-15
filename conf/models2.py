from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base, mapped_column, Mapped

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    students: Mapped['Student'] = relationship('Student', back_populates='group', cascade='all, delete')

class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullname: Mapped[str] = mapped_column(String(150), nullable=False)
    group_id: Mapped[str] = mapped_column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group: Mapped['Group'] = relationship('Group', back_populates='students')


class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullname: Mapped[str] = mapped_column(String(150), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    teacher_id: Mapped[str] = mapped_column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher: Mapped['Teacher'] = relationship('Teacher', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    grade_date: Mapped[str] = mapped_column(Date, nullable=False)
    student_id: Mapped[int] = mapped_column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    student: Mapped['Student'] = relationship('Student', backref='grades')
    subject_id: Mapped[int] = mapped_column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE'))
    subject: Mapped['Subject'] = relationship('Subject', backref='grades')
