from sqlalchemy import Column, Date, DateTime, Integer, String, Table, MetaData, create_engine
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from api import app

#mysql://test:root@localhost/wise?charset=utf8
engine = create_engine(app.config['DATABASE'])
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class TBBranch(Base):
	__tablename__ = 'TBBranch'

	Unique_Id = Column(String(40))
	Branch_Id = Column(Integer, primary_key=True)
	Program_Id = Column(Integer, nullable=False)
	Name = Column(String(100), nullable=False)
	Translation = Column(String(100))
	Code = Column(String(40), nullable=False)
	Year = Column(Integer, nullable=False)
	Students_Num = Column(Integer, nullable=False)
	Seq_Num = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	Color = Column(Integer)
	Points = Column(Integer)
	Misc_Flags = Column(String(256))
	Flags = Column(Integer)


class TBBuilding(Base):
	__tablename__ = 'TBBuilding'

	Unique_Id = Column(String(40))
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

	Unique_Id = Column(String(40))
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

	Unique_Id = Column(String(40))
	Course_Id = Column(Integer, primary_key=True)
	Execution_Type = Column(Integer, nullable=False)
	Name = Column(String(100), nullable=False)
	Translation = Column(String(100))
	Code = Column(String(40), nullable=False)
	Preferred_Time = Column(Integer, nullable=False)
	Seq_Num = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	Color = Column(Integer)
	PushNote = Column(String(512))
	Filter_Aid = Column(String(16))
	Points = Column(Integer)
	Misc_Flags = Column(String(256))
	ChiefTeacher_Id = Column(Integer, nullable=False)
	Flags = Column(Integer, nullable=False)


class TBCoursePart(Base):
	__tablename__ = 'TBCoursePart'

	Unique_Id = Column(String(40))
	CoursePart_Id = Column(Integer, primary_key=True)
	Course_Id = Column(Integer, nullable=False, index=True)
	CourseType_Id = Column(Integer, nullable=False)
	ChiefTeacher_Id = Column(Integer, nullable=False)
	Flags = Column(Integer, nullable=False)


t_TBCoursePart_RProp = Table(
	'TBCoursePart_RProp', metadata,
	Column('CoursePart_Id', Integer, nullable=False, index=True),
	Column('RProp_Id', Integer, nullable=False, index=True)
)


t_TBCoursePart_Tutor = Table(
	'TBCoursePart_Tutor', metadata,
	Column('CoursePart_Id', Integer, nullable=False, index=True),
	Column('Tutor_Id', Integer, nullable=False, index=True)
)


class TBCourseType(Base):
	__tablename__ = 'TBCourseType'

	Unique_Id = Column(String(40))
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

	Unique_Id = Column(String(40))
	Groups_Id = Column(Integer, primary_key=True)
	Branch_Id = Column(Integer, nullable=False, index=True)
	Name = Column(String(40), nullable=False)
	Students_Num = Column(Integer, nullable=False)
	Note = Column(String(200), nullable=False)
	Password = Column(String(20), nullable=False)
	Email = Column(String(256), nullable=False)
	Flags = Column(Integer, nullable=False)
	Parent_Group_Id = Column(Integer, nullable=False, index=True)
	Group_Class = Column(Integer, nullable=False)
	City_Id = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	Color = Column(Integer)
	PushNote = Column(String(512))
	Misc_Flags = Column(String(256))


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

	Unique_Id = Column(String(40))
	Program_Id = Column(Integer, primary_key=True)
	Name = Column(String(150), nullable=False)
	Translation = Column(String(150))
	Code = Column(String(40), nullable=False)
	Years = Column(Integer, nullable=False)
	City_Id = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	Color = Column(Integer)
	Points = Column(Integer)
	Misc_Flags = Column(String(256))
	Seq_Num = Column(Integer, nullable=False)
	Flags = Column(Integer)


class TBRProp(Base):
	__tablename__ = 'TBRProp'

	Unique_Id = Column(String(40))
	RProp_Id = Column(Integer, primary_key=True)
	Name = Column(String(50), nullable=False)


class TBReservation(Base):
	__tablename__ = 'TBReservation'

	Unique_Id = Column(String(40))
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

	Unique_Id = Column(String(40))
	Room_Id = Column(Integer, primary_key=True)
	Name = Column(String(100), nullable=False)
	Seats_Num = Column(Integer, nullable=False)
	Strict = Column(Integer, nullable=False)
	Program_Id = Column(Integer, nullable=False)
	City_Id = Column(Integer, nullable=False)
	Building_Id = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	Reservation_Roles = Column(String(32), nullable=False)
	Color = Column(Integer)
	Misc_Flags = Column(String(256))
	Priority = Column(Integer)
	Meeting_Room = Column(Integer, nullable=False)
	Conference_Hall = Column(Integer, nullable=False)
	Exam_Hall = Column(Integer, nullable=False)
	Seat_Num_X = Column(Integer, nullable=False)
	Seat_Num_Y = Column(Integer, nullable=False)
	Show_On_Web = Column(Integer)
	Seq_Num = Column(Integer, nullable=False)
	Flags = Column(Integer)


t_TBRoom_RProp = Table(
	'TBRoom_RProp', metadata,
	Column('Room_Id', Integer, nullable=False),
	Column('RProp_Id', Integer, nullable=False)
)


class TBSchedule(Base):
	__tablename__ = 'TBSchedule'

	Schedule_Id = Column(Integer, primary_key=True)
	Course_Id = Column(Integer, nullable=False)
	TurnPart_Id = Column(Integer, nullable=False, index=True)
	Room_Id = Column(Integer, nullable=False, index=True)
	Day_Id = Column(Integer, nullable=False)
	Time_Id = Column(Integer, nullable=False)
	Duration = Column(Integer, nullable=False)
	Valid_From = Column(Integer, nullable=False)
	Valid_To = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	Flags = Column(Integer, nullable=False)
	Week_Flags = Column(String(64))
	Misc_Flags = Column(String(256))
	Misc_Id = Column(Integer, nullable=False)


t_TBSettings = Table(
	'TBSettings', metadata,
	Column('Name', String(40), nullable=False),
	Column('Value', String(2048), nullable=False)
)


class TBStudent(Base):
	__tablename__ = 'TBStudent'

	Unique_Id = Column(String(40))
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

	Unique_Id = Column(String(40))
	Turn_Id = Column(Integer, primary_key=True)
	CoursePart_Id = Column(Integer, nullable=False, index=True)
	Seq_Num = Column(Integer, nullable=False)
	Room_Id = Column(Integer, nullable=False)
	Duration = Column(String(512), nullable=False)
	Web_Note = Column(String(64))
	No_Pauses = Column(Integer, nullable=False)
	Start_Hour = Column(Integer, nullable=False)
	Flags = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	All_Hours = Column(Integer)
	Valid_From = Column(Integer, nullable=False)
	Valid_To = Column(Integer, nullable=False)


class TBTurnPart(Base):
	__tablename__ = 'TBTurnPart'

	Unique_Id = Column(String(40))
	TurnPart_Id = Column(Integer, primary_key=True)
	Turn_Id = Column(Integer, nullable=False, index=True)
	Display_Name = Column(String(80), nullable=False)
	Code = Column(String(40))
	Use_Custom_Stud_Num = Column(Integer, nullable=False)
	Actual_Stud_Num = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)


t_TBTurnPart_Groups = Table(
	'TBTurnPart_Groups', metadata,
	Column('TurnPart_Id', Integer, nullable=False, index=True),
	Column('Groups_Id', Integer, nullable=False, index=True)
)


t_TBTurn_Tutor = Table(
	'TBTurn_Tutor', metadata,
	Column('Turn_Id', Integer, nullable=False, index=True),
	Column('Tutor_Id', Integer, nullable=False, index=True)
)


class TBTutor(Base):
	__tablename__ = 'TBTutor'

	Unique_Id = Column(String(40))
	Tutor_Id = Column(Integer, primary_key=True)
	First_Name = Column(String(40), nullable=False)
	Last_Name = Column(String(40), nullable=False)
	Password = Column(String(20), nullable=False)
	Note = Column(String(255), nullable=False)
	Code = Column(String(40), nullable=False)
	Email = Column(String(1024), nullable=False)
	Room_Id = Column(Integer, nullable=False)
	Program_Id = Column(Integer, nullable=False)
	City_Id = Column(Integer, nullable=False)
	Flags = Column(Integer, nullable=False)
	Merge_Id = Column(Integer, nullable=False)
	Role = Column(String(32), nullable=False)
	Color = Column(Integer)
	Employee_Number = Column(Integer)
	PushNote = Column(String(512))
	AA_Queue = Column(String(32))
	EV_Cert = Column(String(32))
	BL_Cert = Column(String(32))
	OL_Cert = Column(String(32))
	State_Country = Column(String(32))
	FACD = Column(String(64))
	Misc_Flags = Column(String(256))


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
