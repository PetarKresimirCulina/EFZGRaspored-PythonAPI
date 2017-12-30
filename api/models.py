# -*- coding: utf-8 -*-
from sqlalchemy import Column, Date, DateTime, Integer, String, Table, MetaData, create_engine, ForeignKey
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import backref, relationship, configure_mappers, deferred
from api import Base, metadata

class TBBranch(Base):
    __tablename__ = 'TBBranch'

    Unique_Id = deferred(Column(String(40)))
    Branch_Id = Column(Integer, primary_key=True)
    Program_Id = Column(Integer, nullable=False)
    Name = Column(String(100), nullable=False)
    Translation = deferred(Column(String(100)))
    Code = deferred(Column(String(40), nullable=False))
    Year = Column(Integer, nullable=False)
    Students_Num = deferred(Column(Integer, nullable=False))
    Seq_Num = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    Color = deferred(Column(Integer))
    Points = deferred(Column(Integer))
    Misc_Flags = deferred(Column(String(256)))
    Flags = deferred(Column(Integer))


class TBBuilding(Base):
    __tablename__ = 'TBBuilding'

    Unique_Id = deferred(Column(String(40)))
    Building_Id = Column(Integer, primary_key=True)
    City_Id = Column(Integer, nullable=False)
    Name = Column(String(60), nullable=False)


t_TBBuilding_Dist = Table(
    'TBBuilding_Dist', metadata,
    Column('Parent_Id', Integer, nullable=False),
    Column('Building_Id', Integer, nullable=False),
    Column('Distance', Integer, nullable=False)
)


class TBCity(Base):
    __tablename__ = 'TBCity'

    Unique_Id = deferred(Column(String(40)))
    City_Id = Column(Integer, primary_key=True)
    Name = Column(String(60), nullable=False)
    Time_Zone = Column(Integer, nullable=False)
    Use_DST = Column(Integer, nullable=False)


t_TBCity_Dist = Table(
    'TBCity_Dist', metadata,
    Column('Parent_Id', Integer, nullable=False),
    Column('City_Id', Integer, nullable=False),
    Column('Distance', Integer, nullable=False)
)


class TBCourse(Base):
    __tablename__ = 'TBCourse'

    Unique_Id = deferred(Column(String(40)))
    Course_Id = Column(Integer, primary_key=True)
    Execution_Type = Column(Integer, nullable=False)
    Name = Column(String(100), nullable=False)
    Translation = deferred(Column(String(100)))
    Code = deferred(Column(String(40), nullable=False))
    Preferred_Time = deferred(Column(Integer, nullable=False))
    Seq_Num = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    Color = deferred(Column(Integer))
    PushNote = deferred(Column(String(512)))
    Filter_Aid = deferred(Column(String(16)))
    Points = deferred(Column(Integer))
    Misc_Flags = deferred(Column(String(256)))
    ChiefTeacher_Id = deferred(Column(Integer, nullable=False))
    Flags = deferred(Column(Integer, nullable=False))


class TBCoursePart(Base):
    __tablename__ = 'TBCoursePart'

    Unique_Id = deferred(Column(String(40)))
    CoursePart_Id = Column(Integer, primary_key=True)
    Course_Id = Column(Integer, ForeignKey('TBCourse.Course_Id'), nullable=False, index=True)
    CourseType_Id = Column(Integer, nullable=False)
    ChiefTeacher_Id = deferred(Column(Integer, nullable=False))
    Flags = deferred(Column(Integer, nullable=False))
    
    '''
    course = relationship('TBCourse', lazy='joined', backref='coursePart')
    '''


t_TBCoursePart_RProp = Table(
    'TBCoursePart_RProp', metadata,
    Column('CoursePart_Id', Integer, nullable=False, index=True),
    Column('RProp_Id', Integer, nullable=False, index=True)
)

class TBCoursePart_Tutor:
    __tablename__ = 'TBCoursePart_Tutor'
    
    CoursePart_Id = Column(Integer, nullable=False, index=True)
    Tutor_Id = Column(Integer, nullable=False, index=True)

'''
t_TBCoursePart_Tutor = Table(
    'TBCoursePart_Tutor', metadata,
    Column('CoursePart_Id', Integer, nullable=False, index=True),
    Column('Tutor_Id', Integer, nullable=False, index=True)
)
'''

class TBCourseType(Base):
    __tablename__ = 'TBCourseType'

    Unique_Id = deferred(Column(String(40)))
    CourseType_Id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    Code = Column(String(40), nullable=False)
    Color = Column(Integer)
    Misc_Flags = Column(String(256))


t_TBCourse_Branch = Table(
    'TBCourse_Branch', metadata,
    Column('Course_Id', Integer, nullable=False, index=True),
    Column('Branch_Id', Integer, nullable=False, index=True)
)


class TBGroup(Base):
    __tablename__ = 'TBGroups'

    Unique_Id = deferred(Column(String(40)))
    Groups_Id = Column(Integer, primary_key=True)
    Branch_Id = Column(Integer, nullable=False, index=True)
    Name = Column(String(40), nullable=False)
    Students_Num = deferred(Column(Integer, nullable=False))
    Note = deferred(Column(String(200), nullable=False))
    Password = deferred(Column(String(20), nullable=False))
    Email = deferred(Column(String(256), nullable=False))
    Flags = deferred(Column(Integer, nullable=False))
    Parent_Group_Id = Column(Integer, nullable=False, index=True)
    Group_Class = deferred(Column(Integer, nullable=False))
    City_Id = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    Color = deferred(Column(Integer))
    PushNote = deferred(Column(String(512)))
    Misc_Flags = deferred(Column(String(256)))
    
    def json(self):
        return ({
           'id': self.Groups_Id,
            'name': self.Name,
            'parent_id': self.Parent_Group_Id,
        })
    


class TBHistoryLog(Base):
    __tablename__ = 'TBHistoryLog'

    HistoryLog_Id = Column(Integer, primary_key=True)
    ChangeDate = Column(DateTime, nullable=False, server_default=FetchedValue())
    Username = Column(String(100), nullable=False)
    Description = Column(String(250), nullable=False)
    EventType = Column(Integer, index=True, server_default=FetchedValue())
    Misc_Id = Column(Integer, server_default=FetchedValue())


t_TBHoliday = Table(
    'TBHoliday', metadata,
    Column('Value', String(40), nullable=False),
    Column('D', Integer),
    Column('M', Integer),
    Column('Begins_At', Integer),
    Column('Duration', Integer)
)


class TBProgram(Base):
    __tablename__ = 'TBProgram'

    Unique_Id = deferred(Column(String(40)))
    Program_Id = Column(Integer, primary_key=True)
    Name = Column(String(150), nullable=False)
    Translation = Column(String(150))
    Code = deferred(Column(String(40), nullable=False))
    Years = Column(Integer, nullable=False)
    City_Id = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    Color = deferred(Column(Integer))
    Points = deferred(Column(Integer))
    Misc_Flags = deferred(Column(String(256)))
    Seq_Num = deferred(Column(Integer, nullable=False))
    Flags = deferred(Column(Integer))
    
    def json(self):
        return ({
            'id': self.Program_Id,
            'name': self.Name,
            'years': self.Years,
        })   


class TBRProp(Base):
    __tablename__ = 'TBRProp'

    Unique_Id = deferred(Column(String(40)))
    RProp_Id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)


class TBReservation(Base):
    __tablename__ = 'TBReservation'

    Unique_Id = deferred(Column(String(40)))
    Reservation_Id = Column(Integer, primary_key=True)
    Type = Column(Integer, nullable=False)
    Note = Column(String(512), nullable=False)
    Owner_Id = Column(Integer, nullable=False)
    From_Week = Column(Integer, nullable=False)
    To_Week = Column(Integer, nullable=False)
    From_Day = Column(Integer, nullable=False)
    To_Day = Column(Integer, nullable=False)
    Begins_At = Column(Integer, nullable=False)
    Duration = Column(Integer, nullable=False)
    Merge_Id = Column(Integer, nullable=False)
    Participants_Num = Column(Integer)
    Flags = Column(Integer)
    Status = Column(Integer)


t_TBReservation_Groups = Table(
    'TBReservation_Groups', metadata,
    Column('Reservation_Id', Integer, nullable=False),
    Column('Groups_Id', Integer, nullable=False)
)


class TBReservationGroupsJournal(Base):
    __tablename__ = 'TBReservation_Groups_Journal'

    Journal_Id = Column(Integer, primary_key=True)
    Journal_Date = Column(DateTime, nullable=False, server_default=FetchedValue())
    Reservation_Id = Column(Integer, nullable=False)
    Groups_Id = Column(Integer, nullable=False)


class TBReservationJournal(Base):
    __tablename__ = 'TBReservation_Journal'

    Journal_Id = Column(Integer, primary_key=True)
    Journal_Date = Column(DateTime, nullable=False, server_default=FetchedValue())
    Reservation_Id = Column(Integer, nullable=False)
    Type = Column(Integer, nullable=False)
    Note = Column(String(512), nullable=False)
    Owner_Id = Column(Integer, nullable=False)
    From_Week = Column(Integer, nullable=False)
    To_Week = Column(Integer, nullable=False)
    From_Day = Column(Integer, nullable=False)
    To_Day = Column(Integer, nullable=False)
    Begins_At = Column(Integer, nullable=False)
    Duration = Column(Integer, nullable=False)
    Merge_Id = Column(Integer, nullable=False)
    Status = Column(Integer)


t_TBReservation_Room = Table(
    'TBReservation_Room', metadata,
    Column('Reservation_Id', Integer, nullable=False),
    Column('Room_Id', Integer, nullable=False)
)


class TBReservationRoomJournal(Base):
    __tablename__ = 'TBReservation_Room_Journal'

    Journal_Id = Column(Integer, primary_key=True)
    Journal_Date = Column(DateTime, nullable=False, server_default=FetchedValue())
    Reservation_Id = Column(Integer, nullable=False)
    Room_Id = Column(Integer, nullable=False)


t_TBReservation_Tutor = Table(
    'TBReservation_Tutor', metadata,
    Column('Reservation_Id', Integer, nullable=False),
    Column('Tutor_Id', Integer, nullable=False)
)


class TBReservationTutorJournal(Base):
    __tablename__ = 'TBReservation_Tutor_Journal'

    Journal_Id = Column(Integer, primary_key=True)
    Journal_Date = Column(DateTime, nullable=False, server_default=FetchedValue())
    Reservation_Id = Column(Integer, nullable=False)
    Tutor_Id = Column(Integer, nullable=False)


class TBRoom(Base):
    __tablename__ = 'TBRoom'

    Unique_Id = deferred(Column(String(40)))
    Room_Id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    Seats_Num = deferred(Column(Integer, nullable=False))
    Strict = deferred(Column(Integer, nullable=False))
    Program_Id = deferred(Column(Integer, nullable=False))
    City_Id = deferred(Column(Integer, nullable=False))
    Building_Id = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    Reservation_Roles = deferred(Column(String(32), nullable=False))
    Color = deferred(Column(Integer))
    Misc_Flags = deferred(Column(String(256)))
    Priority = deferred(Column(Integer))
    Meeting_Room = deferred(Column(Integer, nullable=False))
    Conference_Hall = deferred(Column(Integer, nullable=False))
    Exam_Hall = deferred(Column(Integer, nullable=False))
    Seat_Num_X = deferred(Column(Integer, nullable=False))
    Seat_Num_Y = deferred(Column(Integer, nullable=False))
    Show_On_Web = deferred(Column(Integer))
    Seq_Num = deferred(Column(Integer, nullable=False))
    Flags = deferred(Column(Integer))


t_TBRoom_RProp = Table(
    'TBRoom_RProp', metadata,
    Column('Room_Id', Integer, nullable=False),
    Column('RProp_Id', Integer, nullable=False)
)


class TBSchedule(Base):
    __tablename__ = 'TBSchedule'

    Schedule_Id = Column(Integer, primary_key=True)
    Course_Id = Column(Integer, ForeignKey('TBCourse.Course_Id'), nullable=False, index=True)
    TurnPart_Id = Column(Integer, ForeignKey('TBTurnPart.TurnPart_Id'), nullable=False, index=True)
    Room_Id = Column(Integer, ForeignKey('TBRoom.Room_Id'), nullable=False, index=True)
    Day_Id = Column(Integer, nullable=False)
    Time_Id = Column(Integer, nullable=False)
    Duration = Column(Integer, nullable=False)
    Valid_From = Column(Integer, nullable=False)
    Valid_To = Column(Integer, nullable=False)
    Merge_Id = deferred(Column(Integer, nullable=False))
    Flags = deferred(Column(Integer, nullable=False))
    Week_Flags = deferred(Column(String(64)))
    Misc_Flags = deferred(Column(String(256)))
    Misc_Id = deferred(Column(Integer, nullable=False))

    course = relationship('TBCourse', lazy='joined', backref='schedule')
    turnPart = relationship('TBTurnPart',  lazy='joined', backref=backref('schedule', uselist=False))
    room = relationship('TBRoom', lazy='joined', backref='schedule')
    
t_TBSettings = Table(
    'TBSettings', metadata,
    Column('Name', String(40), nullable=False),
    Column('Value', String(2048), nullable=False)
)


class TBStudent(Base):
    __tablename__ = 'TBStudent'

    Unique_Id = deferred(Column(String(40)))
    Student_Id = Column(Integer, primary_key=True)
    First_Name = Column(String(40), nullable=False)
    Last_Name = Column(String(40), nullable=False)
    Email = Column(String(256), nullable=False)
    Student_Num = Column(String(16), nullable=False)
    Branch_Code = Column(String(40), nullable=False)
    Year = Column(Integer, nullable=False)
    Merge_Id = Column(Integer, nullable=False)
    Flags = Column(Integer, nullable=False)


t_TBStudent_Course = Table(
    'TBStudent_Course', metadata,
    Column('Student_Id', Integer, nullable=False),
    Column('Course_Id', Integer, nullable=False),
    Column('ExecType_Id', Integer, nullable=False)
)


t_TBStudent_Groups = Table(
    'TBStudent_Groups', metadata,
    Column('Student_Id', Integer, nullable=False),
    Column('Groups_Id', Integer, nullable=False)
)


class TBTime(Base):
    __tablename__ = 'TBTime'

    Time_Id = Column(Integer, primary_key=True)
    Start_Hour = Column(String(20), nullable=False)
    End_Hour = Column(String(20), nullable=False)


class TBTurn(Base):
    __tablename__ = 'TBTurn'

    Unique_Id = deferred(Column(String(40)))
    Turn_Id = Column(Integer, primary_key=True)
    CoursePart_Id = Column(Integer, ForeignKey('TBCoursePart.CoursePart_Id'), nullable=False, index=True)
    Seq_Num = deferred(Column(Integer, nullable=False))
    Room_Id = Column(Integer, nullable=False)
    Duration = deferred(Column(String(512), nullable=False))
    Web_Note = deferred(Column(String(64)))
    No_Pauses = deferred(Column(Integer, nullable=False))
    Start_Hour = deferred(Column(Integer, nullable=False))
    Flags = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    All_Hours = deferred(Column(Integer))
    Valid_From = Column(Integer, nullable=False)
    Valid_To = Column(Integer, nullable=False)
    
    coursePart = relationship('TBCoursePart', lazy='joined', backref='turn')
    #turn = relationship('TBTurn', lazy='joined', backref=backref('turnTutor', uselist=False))
    turnTutor = relationship('TBTurn_Tutor',
        lazy='joined',
        foreign_keys=[Turn_Id],
        primaryjoin='TBTurn.Turn_Id == TBTurn_Tutor.Turn_Id',
        backref='tutorTurn'
    )

class TBTurnPart(Base):
    __tablename__ = 'TBTurnPart'

    Unique_Id = deferred(Column(String(40)))
    TurnPart_Id = Column(Integer, primary_key=True)
    Turn_Id = Column(Integer, ForeignKey('TBTurn.Turn_Id'), nullable=False, index=True)
    Display_Name = deferred(Column(String(80), nullable=False))
    Code = deferred(Column(String(40)))
    Use_Custom_Stud_Num = deferred(Column(Integer, nullable=False))
    Actual_Stud_Num = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    

    turn = relationship('TBTurn', lazy='joined', backref='turnPart')


class TBTurnPart_Group(Base):
    __tablename__ = 'TBTurnPart_Groups'
    TurnPart_Id = Column(Integer, ForeignKey('TBTurnPart.TurnPart_Id'), nullable=False, index=True, primary_key=True)
    Groups_Id = Column(Integer, ForeignKey('TBGroups.Groups_Id'), nullable=False, index=True)
    
    
    turnPart = relationship('TBTurnPart', lazy='joined', backref='turnPartGroup')
    group = relationship('TBGroup', lazy='joined', backref='turnPartGroup')
    #schedule = relationship('TBSchedule', primaryjoin='TBSchedule.TurnPart_Id', lazy='joined', backref='turnPartGroup')
    schedule = relationship('TBSchedule',
        lazy='joined',
        foreign_keys=[TurnPart_Id],
        primaryjoin='TBTurnPart_Group.TurnPart_Id == TBSchedule.TurnPart_Id',
        backref='turnPartGroup'
    )

    def json(self):
        return ({
            'day': self.schedule.Day_Id,
            'unitsInDay': self.schedule.Time_Id,
            'duration': self.schedule.Duration,
            'roomId': self.schedule.Room_Id,
            'groupId': self.group.Groups_Id,
            'courseName': self.schedule.course.Name,
            'executionType': self.turnPart.turn.coursePart.CourseType_Id,
            'tutorName': self.turnPart.turn.turnTutor.tutor.First_Name,
            'tutorLastName': self.turnPart.turn.turnTutor.tutor.Last_Name,
            'tutorCode': self.turnPart.turn.turnTutor.tutor.Code,
            'roomName': self.schedule.room.Name,
            'groupName': self.group.Name,
            'validFrom': self.schedule.Valid_From,
            'validTo': self.schedule.Valid_To,
        })
    

class TBTurn_Tutor(Base):
    __tablename__ = 'TBTurn_Tutor'
    Turn_Id = Column(Integer, ForeignKey('TBTurn.Turn_Id'), nullable=False, index=True, primary_key=True)
    Tutor_Id = Column(Integer, ForeignKey('TBTutor.Tutor_Id'), nullable=False, index=True)

    tutor = relationship('TBTutor', lazy='joined', backref='turnTutor')
    #turn = relationship('TBTurn', lazy='joined', backref=backref('turnTutor', uselist=False))

    
'''
t_TBTurnPart_Groups = Table(
    'TBTurnPart_Groups', metadata,
    Column('TurnPart_Id', Integer, nullable=False, index=True),
    Column('Groups_Id', Integer, nullable=False, index=True)
)
'''
'''
t_TBTurn_Tutor = Table(
    'TBTurn_Tutor', metadata,
    Column('Turn_Id', Integer, nullable=False, index=True),
    Column('Tutor_Id', Integer, nullable=False, index=True)
)
'''

class TBTutor(Base):
    __tablename__ = 'TBTutor'

    Unique_Id = deferred(Column(String(40)))
    Tutor_Id = Column(Integer, primary_key=True)
    First_Name = Column(String(40), nullable=False)
    Last_Name = Column(String(40), nullable=False)
    Password = deferred(Column(String(20), nullable=False))
    Note = deferred(Column(String(255), nullable=False))
    Code = Column(String(40), nullable=False)
    Email = deferred(Column(String(1024), nullable=False))
    Room_Id = Column(Integer, nullable=False)
    Program_Id = Column(Integer, nullable=False)
    City_Id = deferred(Column(Integer, nullable=False))
    Flags = deferred(Column(Integer, nullable=False))
    Merge_Id = deferred(Column(Integer, nullable=False))
    Role = deferred(Column(String(32), nullable=False))
    Color = deferred(Column(Integer))
    Employee_Number = deferred(Column(Integer))
    PushNote = deferred(Column(String(512)))
    AA_Queue = deferred(Column(String(32)))
    EV_Cert = deferred(Column(String(32)))
    BL_Cert = deferred(Column(String(32)))
    OL_Cert = deferred(Column(String(32)))
    State_Country = deferred(Column(String(32)))
    FACD = deferred(Column(String(64)))
    Misc_Flags = deferred(Column(String(256)))


t_TBWeb_Settings = Table(
    'TBWeb_Settings', metadata,
    Column('Name', String(40), nullable=False),
    Column('Value', String(1000), nullable=False),
    Column('Type', String(1), nullable=False)
)


class TBWeek(Base):
    __tablename__ = 'TBWeek'

    Week_Id = Column(Integer, primary_key=True)
    First_Day = Column(Date, nullable=False)
    Last_Day = Column(Date, nullable=False)
    Label = Column(String(30))


t_VWHistoryLog = Table(
    'VWHistoryLog', metadata,
    Column('ChangeDate', String(19)),
    Column('Username', String(100)),
    Column('Description', String(250)),
    Column('EventType', Integer, server_default=FetchedValue())
)
# test - TBSchedule.turnPart.turn = relationship(TBTurn, lazy='joined', backref='schedule')