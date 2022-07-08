from flask import Blueprint, request
from helpers.authMiddleware import tokenRequired
from models.member import MemberSchema
from helpers.successResponse import successResponse
import data.member as memberService

memberBP = Blueprint('member', __name__)

@memberBP.route('/', methods=['GET'])
@tokenRequired
def getmembers():
    schema = MemberSchema(many=True)

    return schema.dumps(memberService.getMembers())

@memberBP.route('/', methods=['POST'])
@tokenRequired
def createmember():
    schema = MemberSchema()
    member = schema.load(request.form)
    memberService.createMember(member)

    return successResponse()

@memberBP.route('/<int:id>', methods=['GET'])
@tokenRequired
def getmember(id: int):
    schema = MemberSchema()

    return schema.dump(memberService.getMember(id))

@memberBP.route('/<int:id>', methods=['PUT'])
@tokenRequired
def updatemember(id: int):
    print(id)
    schema = MemberSchema()
    member = schema.load(request.form)
    memberService.updateMember(id, member)

    return successResponse()

@memberBP.route('/<int:id>', methods=['DELETE'])
@tokenRequired
def deleteTicket(id: int):
    memberService.deleteMember(id)

    return successResponse()
