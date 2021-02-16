def remove_conflicts(courses):
    final = courses.copy()
    for i in range(0, len(courses)):
        for j in range(0, len(courses)):
            if courses[i] != courses[j]:
                if courses[i].day1 == courses[j].day1:
                    if courses[j].end1 > courses[i].start1 and courses[j].end1 <= courses[i].end1:
                        final.pop(j)
                        final.insert(j, None)
                        continue
                    if courses[j].start1 >= courses[i].start1 and courses[j].start1 < courses[i].end1:
                        final.pop(j)
                        final.insert(j, None)
                        continue
                if courses[i].day2 == courses[j].day1:
                    if courses[j].end1 > courses[i].start2 and courses[j].end1 <= courses[i].end2:
                        final.pop(j)
                        final.insert(j, None)
                        continue
                    if courses[j].start1 >= courses[i].start2 and courses[j].start1 < courses[i].end2:
                        final.pop(j)
                        final.insert(j, None)
                        continue
                if courses[i].day1 == courses[j].day2:
                    if courses[j].end2 > courses[i].start1 and courses[j].end2 <= courses[i].end1:
                        final.pop(j)
                        final.insert(j, None)
                        continue
                    if courses[j].start2 >= courses[i].start1 and courses[j].start2 < courses[i].end1:
                        final.pop(j)
                        final.insert(j, None)
                        continue
                if courses[i].day2 == courses[j].day2:
                    if courses[j].end2 > courses[i].start2 and courses[j].end2 <= courses[i].end2:
                        final.pop(j)
                        final.insert(j, None)
                        continue
                    if courses[j].start2 >= courses[i].start2 and courses[j].start2 < courses[i].end2:
                        final.pop(j)
                        final.insert(j, None)
                        continue
    final = [n for n in final if n is not None]
    return final

def check_conflicts(courses):
    final = courses.copy()
    for i in range(0, len(courses)):
        for j in range(0, len(courses)):
            if courses[i] != courses[j]:
                if courses[i].day1 == courses[j].day1:
                    if courses[j].end1 > courses[i].start1 and courses[j].end1 <= courses[i].end1:
                        return False
                    if courses[j].start1 >= courses[i].start1 and courses[j].start1 < courses[i].end1:
                        return False
                if courses[i].day2 == courses[j].day1:
                    if courses[j].end1 > courses[i].start2 and courses[j].end1 <= courses[i].end2:
                        return False
                    if courses[j].start1 >= courses[i].start2 and courses[j].start1 < courses[i].end2:
                        return False
                if courses[i].day1 == courses[j].day2:
                    if courses[j].end2 > courses[i].start1 and courses[j].end2 <= courses[i].end1:
                        return False
                    if courses[j].start2 >= courses[i].start1 and courses[j].start2 < courses[i].end1:
                        return False
                if courses[i].day2 == courses[j].day2:
                    if courses[j].end2 > courses[i].start2 and courses[j].end2 <= courses[i].end2:
                        return False
                    if courses[j].start2 >= courses[i].start2 and courses[j].start2 < courses[i].end2:
                        return False
    return True

def find_schedules(courses, fixed):
    final = [fixed]
    to_join = [n for n in courses if not n in fixed]
    pivot = final.copy()
    
    for joined in to_join:
        #print(joined)
        for i in final:
            #print(i)
            #print("*****************")
            a = i.copy()
            a.append(joined)
            if check_conflicts(a):
                pivot.append(a)
                #print(a)
                #print("--------")
        if check_conflicts(a):
            final = pivot.copy()
    #print(len(final))
    return final