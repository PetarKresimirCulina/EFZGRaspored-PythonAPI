# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, request, jsonify, request
from sqlalchemy import asc, desc, and_
from api.models import TBBranch, TBProgram, TBGroup

api = Blueprint('api', __name__)

'''
fetch_data.php - OK
get_groups.php - OK
get_duration.php - NOK
get_all_for_search.php - NOK
get_schedules.php - NOK
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
                            .filter(and_(TBBranch.Program_Id == programId), TBBranch.Year == year)\
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
    #to-do