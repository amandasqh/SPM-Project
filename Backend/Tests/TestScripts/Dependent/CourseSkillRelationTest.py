from HelperFunctionForTest import *

# ======================Test cases======================
courseToSkill = "courseskillrelations"


def addSkillsToCourse():
    print("User Story: Assign Skill To course")
    triggerTestCase("Both role and skill exist", True, courseToSkill,
                    {
                        "Course_ID": "COR001",
                        "Skills": [1, 2, 3]
                    }, "addRelation"
                    )
def updateSkillsOfCourse():
    print("Update skills of role")
    triggerTestCase("Update skills of role,", True, courseToSkill,
                    {
                        "Skills": [10,11,12]
                    }, "updateById","FIN001"
                    )


def viewSkillsRelatedToCourse():
    print("View skills related to course")
    triggerTestCase("View skills related to course", True, courseToSkill,
                    None, "readById","COR001")


def testAllCourseSkillRelationCases():
    addSkillsToCourse()
    viewSkillsRelatedToCourse()
    updateSkillsOfCourse()