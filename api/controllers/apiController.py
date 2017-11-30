# -*- coding: utf-8 -*-
import time
import datetime

from flask import Blueprint, current_app, request, jsonify
from sqlalchemy import asc, desc, and_, or_
from sqlalchemy.orm import joinedload, load_only
from api.models import TBBranch, TBProgram, TBGroup, TBSchedule, TBCourse, TBTutor, TBRoom, TBTurnPart_Group, TBTurn_Tutor, TBTurn, TBTurnPart, TBCoursePart, t_TBSettings
from api import db_session

api = Blueprint('api', __name__)

@api.route('/programs', methods = ['POST'])
def programs():
    programs = TBProgram.query.all()
    response = []
    for program in programs:
        response.append({
            'id': program.Program_Id,
            'name': program.Name,
            'years': program.Years,
        })
    return jsonify(response)

@api.route('/groups', methods = ['POST'])
def groups():
    programId = int(request.form.get('programId'))
    year = int(request.form.get('year'))
    
    groups = TBGroup.query.join(TBBranch, TBGroup.Branch_Id == TBBranch.Branch_Id)\
                            .filter(and_(TBBranch.Program_Id == programId, TBBranch.Year == year))\
                            .order_by(TBGroup.Name.asc())\
                            .all()
    
    response = []
    for g in groups:
        response.append({
            'id': g.Groups_Id,
            'name': g.Name,
            'parent_id': g.Parent_Group_Id,
        })
    return jsonify(response)
    
@api.route('/schedules', methods = ['POST'])
def schedules():

    groupId = int(request.form.get('groupid'))
    groupChildren = TBGroup.query.filter(TBGroup.Parent_Group_Id == groupId)\
                            .options(load_only("Groups_Id",))\
                            .all()

    groupName = TBGroup.query.filter(TBGroup.Groups_Id == groupId)\
                            .options(load_only("Name"))\
                            .first()
    
    terms = [groupId]
    [terms.append(g.Groups_Id) for g in groupChildren]
    
    clauses = or_( * [TBTurnPart_Group.Groups_Id == x for x in terms] )
    groupSchedule = TBTurnPart_Group.query.filter(clauses).all()
    
    response = []    
    
    for t in groupSchedule:
        schedule = t.schedule
        group = t.group
        tutor = t.turnPart.turn.turnTutor.tutor
        coursePart = t.turnPart.turn.coursePart
        
        if schedule:
            response.append({
                'day': schedule.Day_Id,
                'unitsInDay': schedule.Time_Id,
                'duration': schedule.Duration,
                'roomId': schedule.Room_Id,
                'groupId': group.Groups_Id,
                'courseName': schedule.course.Name,
                'executionType': coursePart.CourseType_Id,
                'tutorName': tutor.First_Name,
                'tutorLastName': tutor.Last_Name,
                'tutorCode': tutor.Code,
                'roomName': schedule.room.Name,
                'groupName': group.Name,
            })
    '''
    for t in groupSchedule:
        response.append({
            'day': t.turnPart.schedule.Day_Id,
            'unitsInDay': t.turnPart.schedule.Time_Id,
            'duration': t.turnPart.schedule.Duration,
            'roomId': t.turnPart.schedule.Room_Id,
            'groupId': groupId,
            'courseName': t.turnPart.schedule.course.Name,
            'executionType': t.turnPart.turn.coursePart.CourseType_Id,
            'tutorName': t.turnPart.turn.turnTutor.tutor.First_Name,
            'tutorLastName': t.turnPart.turn.turnTutor.tutor.Last_Name,
            'tutorCode': t.turnPart.turn.turnTutor.tutor.Code,
            'roomName': t.turnPart.schedule.room.Name,
            'groupName': groupName.Name,
        })
       ''' 
    return jsonify(response)
    
    '''
        SELECT * FROM `TBTurnPart_Groups`
        JOIN `TBSchedule` ON `TBSchedule`.`TurnPart_Id` = `TBTurnPart_Groups`.`TurnPart_Id`
        JOIN `TBTurnPart` ON `TBTurnPart`.`TurnPart_Id` = `TBTurnPart_Groups`.`TurnPart_Id`
        JOIN `TBTurn` ON `TBTurnPart`.`Turn_Id` = `TBTurn`.`Turn_Id`
        JOIN `TBTurn_Tutor` ON `TBTurn_Tutor`.`Turn_Id` = `TBTurn`.`Turn_Id`
        JOIN `TBTutor` ON `TBTurn_Tutor`.`Tutor_Id` = `TBTutor`.`Tutor_Id`
        JOIN `TBCoursePart` ON `TBCoursePart`.`CoursePart_Id` = `TBTurn`.`CoursePart_Id`
        JOIN `TBCourse` ON `TBCourse`.`Course_Id` = `TBCoursePart`.`Course_Id`
        JOIN `TBRoom` ON `TBRoom`.`Room_Id` = `TBSchedule`.`Room_Id`
        JOIN `TBGroups` ON `TBTurnPart_Groups`.`Groups_Id` = `TBGroups`.`Groups_Id`
        WHERE `TBTurnPart_Groups`.`Groups_Id` = 46 OR `TBTurnPart_Groups`.`Groups_Id` = 61 OR `TBTurnPart_Groups`.`Groups_Id` = 62
    '''
    
@api.route('/duration', methods = ['POST'])
def duration():
    year = winter = summer = None
    
    settings = db_session.query(t_TBSettings).all()
    
    semesterType = TBSchedule.query.filter(TBSchedule.Valid_From > 1).limit(22).all()
    semesterType = 0 if len(semesterType) > 20 else 1
    
    for s in settings:
        if s.Name == 'year':
            year = int(s.Value.strip())
        if s.Name == 'winter_semester':
            winter = s.Value.strip()
        if s.Name == 'summer_semester':
            summer = s.Value.strip()
    
    if semesterType == 0:
        winter = winter.split(' - ')
        winter[0] = '{0}{1}'.format(winter[0], year)
        winter[1] = '{0}{1}'.format(winter[1], year + 1)
        
        start = time.mktime(datetime.datetime.strptime(winter[0], "%d.%m.%Y").timetuple())
        end = time.mktime(datetime.datetime.strptime(winter[1], "%d.%m.%Y").timetuple())
    else:
        summer = summer.split(' - ')
        summer[0] = '{0}{1}'.format(summer[0], year)
        summer[1] = '{0}{1}'.format(summer[1], year + 1)
        
        start = time.mktime(datetime.datetime.strptime(summer[0], "%d.%m.%Y").timetuple())
        end = time.mktime(datetime.datetime.strptime(summer[0], "%d.%m.%Y").timetuple())
    
    response = [
        {
            'year': year,
            'start': start,
            'ends': end
        }
    ]
    return jsonify(response)

@api.route('/search', methods = ['POST'])
def search():
    '''
    $result = $connection->query("SELECT * FROM schedules, courses, tutors, rooms, groups, branches WHERE schedules.turn_part_id=courses.turn_part_id AND courses.tutors = tutors.id AND schedules.room_id=rooms.id AND schedules.group_id = groups.id AND groups.branch_id = branches.id");
		if($result->num_rows > 0)
		{
			while($row = mysqli_fetch_array($result))
			{
				$parent_id = $row[10];
				$group_id = $row[9];
				$group_name = "null";
				
				
				// day | units in day | duration | roomid | period | group id | course name | execution type | tutor name | tutor last name | tutor code | room name | group name | year
				echo $row[4] . '&' . $row[5] . '&' . $row[6] . '&' . $row[7] . '&' . $row[8] . '&' . $row[9] . '&' . $row[13] . '&' . $row[15] . '&' . $row[22] . '&' . $row[23] . '&' . $row[24] . '&' . $row[26] . '&' . $row[30] . '&' . $row[36] . '<>';
			}
		}
		else { return 0; }
    '''
    semesterType = TBSchedule.query.filter(TBSchedule.Valid_From > 1).limit(22).all()
    semesterType = 0 if len(semesterType) > 20 else 1

    groupSchedule = TBTurnPart_Group.query.all()
    
    
    response = []
    for t in groupSchedule:
        schedule = t.schedule
        group = t.group
        tutor = t.turnPart.turn.turnTutor.tutor
        coursePart = t.turnPart.turn.coursePart
        
        if schedule:
            response.append({
                'day': schedule.Day_Id,
                'unitsInDay': schedule.Time_Id,
                'duration': schedule.Duration,
                'roomId': schedule.Room_Id,
                'groupId': group.Groups_Id,
                'courseName': schedule.course.Name,
                'executionType': coursePart.CourseType_Id,
                'tutorName': tutor.First_Name,
                'tutorLastName': tutor.Last_Name,
                'tutorCode': tutor.Code,
                'roomName': schedule.room.Name,
                'groupName': group.Name,
            })


    return jsonify(response)
    