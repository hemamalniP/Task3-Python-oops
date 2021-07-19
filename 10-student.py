def stud(stud_id,**arg):
    print('\nStudent id: {stud_id}')
    if 'name'in arg:
        print("Student name: {arg[name]}")
        
    if 'name' and 'stud_class' in arg:
        print("Student name: {arg[name]}")
        print("Student class: {arg[stud_class]}")
        
stud(stud_id='SAT12',name='Hema')        
stud(stud_id='SAT12',name='Hema',stud_class="A")        
