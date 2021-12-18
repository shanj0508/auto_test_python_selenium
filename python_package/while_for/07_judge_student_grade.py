# -*- coding: utf-8 -*-
'''
判断学生成绩：成绩等级A~E。
其中，
    90分以上为A
    80-89分为B
    70-90分为C
    60-69分为D
    60分以下为E
'''


def judge_student_grade():
    score = int(input('请输入您的考试分数：'))
    grade = None
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('您的考试分数是{}分,最终评定等级为{}'.format(score, grade))


if __name__ == '__main__':
    judge_student_grade()
