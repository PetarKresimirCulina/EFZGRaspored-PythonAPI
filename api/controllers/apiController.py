# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, request, jsonify
from sqlalchemy import asc, desc, and_, or_
from sqlalchemy.orm import joinedload, load_only
from api.models import TBBranch, TBProgram, TBGroup, TBSchedule, TBCourse, TBTutor, TBRoom, TBTurnPart_Group, TBTurn_Tutor, TBTurn, TBTurnPart, TBCoursePart

api = Blueprint('api', __name__)

'''
fetch_data.php - OK
get_groups.php - OK
get_duration.php - NOK
get_all_for_search.php - NOK
get_schedules.php - OK
'''

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
    '''
    SELECT * FROM branches, groups WHERE groups.branch_id=branches.id 
    AND branches.program_id=$program_id 
    AND (branches.year=3 
    OR branches.year=4) 
    AND 
    EXISTS(SELECT * FROM courses 
    WHERE courses.branch_id=branches.id) 
    ORDER BY groups.name ASC"
    
    uzmi sve grupe čiji branchevi imaju trazene program id i year parametre - valjda - grupe su npr 1_1 ABC-DEF, 1_2, DEF-GHI itd.
    '''
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
    '''
    SELECT * FROM schedules, courses, tutors, rooms 
    WHERE schedules.turn_part_id=courses.turn_part_id 
    AND schedules.parent_id = $groups 
    AND courses.groups_parent = $groups 
    AND courses.tutors = tutors.id 
    AND schedules.room_id=rooms.id"
    '''
    groupId = int(request.form.get('groupid'))
    # // day | units in day | duration | roomid | period | group id | course name | execution type | tutor name | tutor last name | tutor code | room name | group name
    
    
    # LOGIKA - ide schedules -> turn part id -> turn id -> course part id i na kraju course id da se dobije naziv
    
    #1
    '''
    group = TBGroup.query.filter(TBGroup.Parent_Group_Id == groupId).all()
    
    terms = [groupId]
    for g in group:
        terms.append(g.Groups_Id)
    
    clauses = or_( * [TBTurnPart_Group.Groups_Id == x for x in terms] )
    tbtpg = TBTurnPart_Group.query.filter(clauses).all()
    
    response = []
    for t in tbtpg:
        schedule = t.turnPart.schedule
        turn =  t.turnPart.turn
        tutor = turn.turnTutor.tutor
    
        response.append({
            'day': schedule.Day_Id,
            'unitsInDay': schedule.Time_Id,
            'duration': schedule.Duration,
            'roomId': schedule.Room_Id,
            'groupId': groupId,
            'courseName': schedule.course.Name,
            'executionType': turn.coursePart.CourseType_Id,
            'tutorName': tutor.First_Name,
            'tutorLastName': tutor.Last_Name,
            'tutorCode': tutor.Code,
            'roomName': schedule.room.Name,
        })
    return jsonify(response)
    
    '''
    # 2
    groupChildren = TBGroup.query.filter(TBGroup.Parent_Group_Id == groupId)\
                            .options(load_only("Groups_Id",))\
                            .all()

    groupName = TBGroup.query.filter(TBGroup.Groups_Id == groupId)\
                            .options(load_only("Name"))\
                            .first()
    
    terms = [groupId]
    for g in groupChildren:
        terms.append(g.Groups_Id)
    
    clauses = or_( * [TBTurnPart_Group.Groups_Id == x for x in terms] )
    tbtpg = TBTurnPart_Group.query.join(TBTurnPart, TBTurnPart_Group.TurnPart_Id == TBTurnPart.TurnPart_Id)\
                                    .join(TBSchedule, TBTurnPart.TurnPart_Id == TBSchedule.TurnPart_Id)\
                                    .join(TBTurn, TBTurnPart.Turn_Id == TBTurn.Turn_Id)\
                                    .join(TBTurn_Tutor, TBTurn.Turn_Id == TBTurn_Tutor.Turn_Id)\
                                    .join(TBTutor, TBTurn_Tutor.Tutor_Id == TBTutor.Tutor_Id)\
                                    .filter(clauses)\
                                    .all()
    
    response = []    
    for t in tbtpg:
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
    return jsonify(response)
    