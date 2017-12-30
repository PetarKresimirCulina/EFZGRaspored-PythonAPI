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
    [response.append(p.json()) for p in programs]

    return jsonify(response)

@api.route('/groups', methods = ['POST'])
def groups():
    programId = int(request.form.get('program_id'))
    year = int(request.form.get('year'))
    
    groups = TBGroup.query.join(TBBranch, TBGroup.Branch_Id == TBBranch.Branch_Id)\
                            .filter(and_(TBBranch.Program_Id == programId, TBBranch.Year == year))\
                            .order_by(TBGroup.Name.asc())\
                            .all()
    
    response = []
    [response.append(g.json()) for g in groups]

    return jsonify(response)
    
@api.route('/schedule', methods = ['POST'])
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
    [response.append(t.json()) for t in groupSchedule]
    
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
    
    semesterType = TBSchedule.query.filter(TBSchedule.Valid_From > 15).limit(22).all()
    semesterType = 0 if len(semesterType) < 20 else 1
    
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
        summer[0] = '{0}{1}'.format(summer[0], year + 1)
        summer[1] = '{0}{1}'.format(summer[1], year + 1)
        
        start = time.mktime(datetime.datetime.strptime(summer[0], "%d.%m.%Y").timetuple())
        end = time.mktime(datetime.datetime.strptime(summer[1], "%d.%m.%Y").timetuple())
    
    return jsonify([{
            'year': year,
            'start': start,
            'end': end
        }]
    )

@api.route('/all', methods = ['POST'])
def allSchedules():

    groupSchedule = TBTurnPart_Group.query.join(TBTurnPart_Group.schedule).all()
    
    response = []
    [response.append(t.json()) for t in groupSchedule]
    
    return jsonify(response)
    