import json

def verify(data):

    user_questions=data["data"]["submissionList"]["submissions"]

    solved=set()

    actual=load_ques()

    for question in user_questions:

        title=question["title"]

        status=question["statusDisplay"]

        time=int(question["timestamp"])

        if title in solved:
            continue
        else:
            if(status=="Accepted" and title in actual):
                print(title)
                start=actual[title]
                end=actual[title]+86400
                if(time>=start and time<=end):
                    solved.add(title)


    return len(solved)

def load_ques():

    startQues={
        "Jump Game": 1766892600,
        "Minimum Penalty for a Shop": 1766806200,
        "Count Unguarded Cells in the Grid":1766719800,
        "Gas Station" : 1766633400,
        "Maximum Sum of Three Numbers Divisible by Three" : 1766547000,
        "Minimum Number of Operations to Have Distinct Elements":1766460600
    }

    return startQues
