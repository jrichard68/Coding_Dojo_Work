def scores_grades():
    for x in range(10):
        import random
        score = random.randint(60, 100)
        if score < 70:
            print "Score: ", score, "; Your grade is D"
        elif score < 80:
            print "Score: ", score, "; Your grade is C"
        elif score < 90:
            print "Score: ", score, "; Your grade is B"
        else:
            print "Score: ", score, "; Your grade is A"

scores_grades()