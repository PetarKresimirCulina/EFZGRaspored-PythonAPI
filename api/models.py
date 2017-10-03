# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, String, Table
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class TBBranch(db.Model):
	__tablename__ = 'TBBranch'

	Unique_Id = db.Column(db.String(40))
	Branch_Id = db.Column(db.Integer, primary_key=True)
	Program_Id = db.Column(db.Integer, nullable=False)
	Name = db.Column(db.String(100), nullable=False)
	Translation = db.Column(db.String(100))
	Code = db.Column(db.String(40), nullable=False)
	Year = db.Column(db.Integer, nullable=False)
	Students_Num = db.Column(db.Integer, nullable=False)
	Seq_Num = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Color = db.Column(db.Integer)
	Points = db.Column(db.Integer)
	Misc_Flags = db.Column(db.String(256))
	Flags = db.Column(db.Integer)


class TBBuilding(db.Model):
	__tablename__ = 'TBBuilding'

	Unique_Id = db.Column(db.String(40))
	Building_Id = db.Column(db.Integer, primary_key=True)
	City_Id = db.Column(db.Integer, nullable=False)
	Name = db.Column(db.String(60), nullable=False)


t_TBBuilding_Dist = db.Table(
	'TBBuilding_Dist',
	db.Column('Parent_Id', db.Integer, nullable=False),
	db.Column('Building_Id', db.Integer, nullable=False),
	db.Column('Distance', db.Integer, nullable=False)
)


class TBCity(db.Model):
	__tablename__ = 'TBCity'

	Unique_Id = db.Column(db.String(40))
	City_Id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(60), nullable=False)
	Time_Zone = db.Column(db.Integer, nullable=False)
	Use_DST = db.Column(db.Integer, nullable=False)


t_TBCity_Dist = db.Table(
	'TBCity_Dist',
	db.Column('Parent_Id', db.Integer, nullable=False),
	db.Column('City_Id', db.Integer, nullable=False),
	db.Column('Distance', db.Integer, nullable=False)
)


class TBCourse(db.Model):
	__tablename__ = 'TBCourse'

	Unique_Id = db.Column(db.String(40))
	Course_Id = db.Column(db.Integer, primary_key=True)
	Execution_Type = db.Column(db.Integer, nullable=False)
	Name = db.Column(db.String(100), nullable=False)
	Translation = db.Column(db.String(100))
	Code = db.Column(db.String(40), nullable=False)
	Preferred_Time = db.Column(db.Integer, nullable=False)
	Seq_Num = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Color = db.Column(db.Integer)
	PushNote = db.Column(db.String(512))
	Filter_Aid = db.Column(db.String(16))
	Points = db.Column(db.Integer)
	Misc_Flags = db.Column(db.String(256))
	ChiefTeacher_Id = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer, nullable=False)


class TBCoursePart(db.Model):
	__tablename__ = 'TBCoursePart'

	Unique_Id = db.Column(db.String(40))
	CoursePart_Id = db.Column(db.Integer, primary_key=True)
	Course_Id = db.Column(db.Integer, nullable=False, index=True)
	CourseType_Id = db.Column(db.Integer, nullable=False)
	ChiefTeacher_Id = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer, nullable=False)


t_TBCoursePart_RProp = db.Table(
	'TBCoursePart_RProp',
	db.Column('CoursePart_Id', db.Integer, nullable=False, index=True),
	db.Column('RProp_Id', db.Integer, nullable=False, index=True)
)


t_TBCoursePart_Tutor = db.Table(
	'TBCoursePart_Tutor',
	db.Column('CoursePart_Id', db.Integer, nullable=False, index=True),
	db.Column('Tutor_Id', db.Integer, nullable=False, index=True)
)


class TBCourseType(db.Model):
	__tablename__ = 'TBCourseType'

	Unique_Id = db.Column(db.String(40))
	CourseType_Id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(100), nullable=False)
	Code = db.Column(db.String(40), nullable=False)
	Color = db.Column(db.Integer)
	Misc_Flags = db.Column(db.String(256))


t_TBCourse_Branch = db.Table(
	'TBCourse_Branch',
	db.Column('Course_Id', db.Integer, nullable=False, index=True),
	db.Column('Branch_Id', db.Integer, nullable=False, index=True)
)


class TBGroup(db.Model):
	__tablename__ = 'TBGroups'

	Unique_Id = db.Column(db.String(40))
	Groups_Id = db.Column(db.Integer, primary_key=True)
	Branch_Id = db.Column(db.Integer, nullable=False, index=True)
	Name = db.Column(db.String(40), nullable=False)
	Students_Num = db.Column(db.Integer, nullable=False)
	Note = db.Column(db.String(200), nullable=False)
	Password = db.Column(db.String(20), nullable=False)
	Email = db.Column(db.String(256), nullable=False)
	Flags = db.Column(db.Integer, nullable=False)
	Parent_Group_Id = db.Column(db.Integer, nullable=False, index=True)
	Group_Class = db.Column(db.Integer, nullable=False)
	City_Id = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Color = db.Column(db.Integer)
	PushNote = db.Column(db.String(512))
	Misc_Flags = db.Column(db.String(256))


class TBHistoryLog(db.Model):
	__tablename__ = 'TBHistoryLog'

	HistoryLog_Id = db.Column(db.Integer, primary_key=True)
	ChangeDate = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
	Username = db.Column(db.String(100), nullable=False)
	Description = db.Column(db.String(250), nullable=False)
	EventType = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
	Misc_Id = db.Column(db.Integer, server_default=db.FetchedValue())


t_TBHoliday = db.Table(
	'TBHoliday',
	db.Column('Value', db.String(40), nullable=False),
	db.Column('D', db.Integer),
	db.Column('M', db.Integer),
	db.Column('Begins_At', db.Integer),
	db.Column('Duration', db.Integer)
)


class TBProgram(db.Model):
	__tablename__ = 'TBProgram'

	Unique_Id = db.Column(db.String(40))
	Program_Id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(150), nullable=False)
	Translation = db.Column(db.String(150))
	Code = db.Column(db.String(40), nullable=False)
	Years = db.Column(db.Integer, nullable=False)
	City_Id = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Color = db.Column(db.Integer)
	Points = db.Column(db.Integer)
	Misc_Flags = db.Column(db.String(256))
	Seq_Num = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer)


class TBRProp(db.Model):
	__tablename__ = 'TBRProp'

	Unique_Id = db.Column(db.String(40))
	RProp_Id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(50), nullable=False)


class TBReservation(db.Model):
	__tablename__ = 'TBReservation'

	Unique_Id = db.Column(db.String(40))
	Reservation_Id = db.Column(db.Integer, primary_key=True)
	Type = db.Column(db.Integer, nullable=False)
	Note = db.Column(db.String(512), nullable=False)
	Owner_Id = db.Column(db.Integer, nullable=False)
	From_Week = db.Column(db.Integer, nullable=False)
	To_Week = db.Column(db.Integer, nullable=False)
	From_Day = db.Column(db.Integer, nullable=False)
	To_Day = db.Column(db.Integer, nullable=False)
	Begins_At = db.Column(db.Integer, nullable=False)
	Duration = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Participants_Num = db.Column(db.Integer)
	Flags = db.Column(db.Integer)
	Status = db.Column(db.Integer)


t_TBReservation_Groups = db.Table(
	'TBReservation_Groups',
	db.Column('Reservation_Id', db.Integer, nullable=False),
	db.Column('Groups_Id', db.Integer, nullable=False)
)


class TBReservationGroupsJournal(db.Model):
	__tablename__ = 'TBReservation_Groups_Journal'

	Journal_Id = db.Column(db.Integer, primary_key=True)
	Journal_Date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
	Reservation_Id = db.Column(db.Integer, nullable=False)
	Groups_Id = db.Column(db.Integer, nullable=False)


class TBReservationJournal(db.Model):
	__tablename__ = 'TBReservation_Journal'

	Journal_Id = db.Column(db.Integer, primary_key=True)
	Journal_Date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
	Reservation_Id = db.Column(db.Integer, nullable=False)
	Type = db.Column(db.Integer, nullable=False)
	Note = db.Column(db.String(512), nullable=False)
	Owner_Id = db.Column(db.Integer, nullable=False)
	From_Week = db.Column(db.Integer, nullable=False)
	To_Week = db.Column(db.Integer, nullable=False)
	From_Day = db.Column(db.Integer, nullable=False)
	To_Day = db.Column(db.Integer, nullable=False)
	Begins_At = db.Column(db.Integer, nullable=False)
	Duration = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Status = db.Column(db.Integer)


t_TBReservation_Room = db.Table(
	'TBReservation_Room',
	db.Column('Reservation_Id', db.Integer, nullable=False),
	db.Column('Room_Id', db.Integer, nullable=False)
)


class TBReservationRoomJournal(db.Model):
	__tablename__ = 'TBReservation_Room_Journal'

	Journal_Id = db.Column(db.Integer, primary_key=True)
	Journal_Date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
	Reservation_Id = db.Column(db.Integer, nullable=False)
	Room_Id = db.Column(db.Integer, nullable=False)


t_TBReservation_Tutor = db.Table(
	'TBReservation_Tutor',
	db.Column('Reservation_Id', db.Integer, nullable=False),
	db.Column('Tutor_Id', db.Integer, nullable=False)
)


class TBReservationTutorJournal(db.Model):
	__tablename__ = 'TBReservation_Tutor_Journal'

	Journal_Id = db.Column(db.Integer, primary_key=True)
	Journal_Date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
	Reservation_Id = db.Column(db.Integer, nullable=False)
	Tutor_Id = db.Column(db.Integer, nullable=False)


class TBRoom(db.Model):
	__tablename__ = 'TBRoom'

	Unique_Id = db.Column(db.String(40))
	Room_Id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(100), nullable=False)
	Seats_Num = db.Column(db.Integer, nullable=False)
	Strict = db.Column(db.Integer, nullable=False)
	Program_Id = db.Column(db.Integer, nullable=False)
	City_Id = db.Column(db.Integer, nullable=False)
	Building_Id = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Reservation_Roles = db.Column(db.String(32), nullable=False)
	Color = db.Column(db.Integer)
	Misc_Flags = db.Column(db.String(256))
	Priority = db.Column(db.Integer)
	Meeting_Room = db.Column(db.Integer, nullable=False)
	Conference_Hall = db.Column(db.Integer, nullable=False)
	Exam_Hall = db.Column(db.Integer, nullable=False)
	Seat_Num_X = db.Column(db.Integer, nullable=False)
	Seat_Num_Y = db.Column(db.Integer, nullable=False)
	Show_On_Web = db.Column(db.Integer)
	Seq_Num = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer)


t_TBRoom_RProp = db.Table(
	'TBRoom_RProp',
	db.Column('Room_Id', db.Integer, nullable=False),
	db.Column('RProp_Id', db.Integer, nullable=False)
)


class TBSchedule(db.Model):
	__tablename__ = 'TBSchedule'

	Schedule_Id = db.Column(db.Integer, primary_key=True)
	Course_Id = db.Column(db.Integer, nullable=False)
	TurnPart_Id = db.Column(db.Integer, nullable=False, index=True)
	Room_Id = db.Column(db.Integer, nullable=False, index=True)
	Day_Id = db.Column(db.Integer, nullable=False)
	Time_Id = db.Column(db.Integer, nullable=False)
	Duration = db.Column(db.Integer, nullable=False)
	Valid_From = db.Column(db.Integer, nullable=False)
	Valid_To = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer, nullable=False)
	Week_Flags = db.Column(db.String(64))
	Misc_Flags = db.Column(db.String(256))
	Misc_Id = db.Column(db.Integer, nullable=False)


t_TBSettings = db.Table(
	'TBSettings',
	db.Column('Name', db.String(40), nullable=False),
	db.Column('Value', db.String(2048), nullable=False)
)


class TBStudent(db.Model):
	__tablename__ = 'TBStudent'

	Unique_Id = db.Column(db.String(40))
	Student_Id = db.Column(db.Integer, primary_key=True)
	First_Name = db.Column(db.String(40), nullable=False)
	Last_Name = db.Column(db.String(40), nullable=False)
	Email = db.Column(db.String(256), nullable=False)
	Student_Num = db.Column(db.String(16), nullable=False)
	Branch_Code = db.Column(db.String(40), nullable=False)
	Year = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer, nullable=False)


t_TBStudent_Course = db.Table(
	'TBStudent_Course',
	db.Column('Student_Id', db.Integer, nullable=False),
	db.Column('Course_Id', db.Integer, nullable=False),
	db.Column('ExecType_Id', db.Integer, nullable=False)
)


t_TBStudent_Groups = db.Table(
	'TBStudent_Groups',
	db.Column('Student_Id', db.Integer, nullable=False),
	db.Column('Groups_Id', db.Integer, nullable=False)
)


class TBTime(db.Model):
	__tablename__ = 'TBTime'

	Time_Id = db.Column(db.Integer, primary_key=True)
	Start_Hour = db.Column(db.String(20), nullable=False)
	End_Hour = db.Column(db.String(20), nullable=False)


class TBTurn(db.Model):
	__tablename__ = 'TBTurn'

	Unique_Id = db.Column(db.String(40))
	Turn_Id = db.Column(db.Integer, primary_key=True)
	CoursePart_Id = db.Column(db.Integer, nullable=False, index=True)
	Seq_Num = db.Column(db.Integer, nullable=False)
	Room_Id = db.Column(db.Integer, nullable=False)
	Duration = db.Column(db.String(512), nullable=False)
	Web_Note = db.Column(db.String(64))
	No_Pauses = db.Column(db.Integer, nullable=False)
	Start_Hour = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	All_Hours = db.Column(db.Integer)
	Valid_From = db.Column(db.Integer, nullable=False)
	Valid_To = db.Column(db.Integer, nullable=False)


class TBTurnPart(db.Model):
	__tablename__ = 'TBTurnPart'

	Unique_Id = db.Column(db.String(40))
	TurnPart_Id = db.Column(db.Integer, primary_key=True)
	Turn_Id = db.Column(db.Integer, nullable=False, index=True)
	Display_Name = db.Column(db.String(80), nullable=False)
	Code = db.Column(db.String(40))
	Use_Custom_Stud_Num = db.Column(db.Integer, nullable=False)
	Actual_Stud_Num = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)


t_TBTurnPart_Groups = db.Table(
	'TBTurnPart_Groups',
	db.Column('TurnPart_Id', db.Integer, nullable=False, index=True),
	db.Column('Groups_Id', db.Integer, nullable=False, index=True)
)


t_TBTurn_Tutor = db.Table(
	'TBTurn_Tutor',
	db.Column('Turn_Id', db.Integer, nullable=False, index=True),
	db.Column('Tutor_Id', db.Integer, nullable=False, index=True)
)


class TBTutor(db.Model):
	__tablename__ = 'TBTutor'

	Unique_Id = db.Column(db.String(40))
	Tutor_Id = db.Column(db.Integer, primary_key=True)
	First_Name = db.Column(db.String(40), nullable=False)
	Last_Name = db.Column(db.String(40), nullable=False)
	Password = db.Column(db.String(20), nullable=False)
	Note = db.Column(db.String(255), nullable=False)
	Code = db.Column(db.String(40), nullable=False)
	Email = db.Column(db.String(1024), nullable=False)
	Room_Id = db.Column(db.Integer, nullable=False)
	Program_Id = db.Column(db.Integer, nullable=False)
	City_Id = db.Column(db.Integer, nullable=False)
	Flags = db.Column(db.Integer, nullable=False)
	Merge_Id = db.Column(db.Integer, nullable=False)
	Role = db.Column(db.String(32), nullable=False)
	Color = db.Column(db.Integer)
	Employee_Number = db.Column(db.Integer)
	PushNote = db.Column(db.String(512))
	AA_Queue = db.Column(db.String(32))
	EV_Cert = db.Column(db.String(32))
	BL_Cert = db.Column(db.String(32))
	OL_Cert = db.Column(db.String(32))
	State_Country = db.Column(db.String(32))
	FACD = db.Column(db.String(64))
	Misc_Flags = db.Column(db.String(256))


t_TBWeb_Settings = db.Table(
	'TBWeb_Settings',
	db.Column('Name', db.String(40), nullable=False),
	db.Column('Value', db.String(1000), nullable=False),
	db.Column('Type', db.String(1), nullable=False)
)


class TBWeek(db.Model):
	__tablename__ = 'TBWeek'

	Week_Id = db.Column(db.Integer, primary_key=True)
	First_Day = db.Column(db.Date, nullable=False)
	Last_Day = db.Column(db.Date, nullable=False)
	Label = db.Column(db.String(30))


t_VWHistoryLog = db.Table(
	'VWHistoryLog',
	db.Column('ChangeDate', db.String(19)),
	db.Column('Username', db.String(100)),
	db.Column('Description', db.String(250)),
	db.Column('EventType', db.Integer, server_default=db.FetchedValue())
)