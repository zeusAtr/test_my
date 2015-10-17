workers = set(['Joel','Ken','Pit'])
salary = set(['Joel','Bob','Sam'])
contracts = set(['Bob','Ken','Pit'])
name = raw_input('Enter name of the employee')

if name in workers & salary - contracts :
    print "Yes salary to be paid"
else:
    print "No he shouldn't be paid salary"



