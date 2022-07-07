from flask import Blueprint, request
from models.member import MemberSchema
from helpers.successResponse import successResponse
import data.member as memberService

memberBP = Blueprint('member', __name__)

@memberBP.route('/', methods=['GET'])
def getmembers():
    schema = MemberSchema(many=True)

    return schema.dumps(memberService.getMembers())

@memberBP.route('/', methods=['POST'])
def createmember():
    schema = MemberSchema()
    member = schema.load(request.form)
    memberService.createMember(member)

    return successResponse()

@memberBP.route('/<int:id>', methods=['GET'])
def getmember(id: int):
    schema = MemberSchema()

    return schema.dump(memberService.getMember(id))

@memberBP.route('/<int:id>', methods=['PUT'])
def updatemember(id: int):
    print(id)
    schema = MemberSchema()
    member = schema.load(request.form)
    memberService.updateMember(id, member)

    return successResponse()

@memberBP.route('/<int:id>', methods=['DELETE'])
def deleteTicket(id: int):
    memberService.deleteMember(id)

    return successResponse()
