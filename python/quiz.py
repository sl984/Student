import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 3
correct = 0

def print_result(rsp, expected):
    if rsp == expected:
        print(rsp + " is correct!")
        correct += 1
    else:
        print(rsp + " is incorrect!")

print("Hello, " + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_with_response("Are you ready to take a test?")

rsp = question_with_response("What command is used to include other functions that were previously developed?")
print_result(rsp, "import")

rsp = question_with_response("What command is used to evaluate correct or incorrect responses in this example?")
print_result(rsp, "if")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
print_result(rsp, "expression")

print(getpass.getuser() + " you scored " + str(correct) + "/" + str(questions))