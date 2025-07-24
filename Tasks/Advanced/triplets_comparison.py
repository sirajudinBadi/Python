
def triplet_comparison(str_of_rating):
    list_of_rating = str_of_rating.strip().splitlines()

    a_rating = list_of_rating[0].split()
    b_rating = list_of_rating[1].split()

    a_score = 0
    b_score = 0

    for i in range(3):
        if int(a_rating[i]) > int(b_rating[i]):
            a_score += 1
        elif int(a_rating[i]) < int(b_rating[i]):
            b_score += 1


    return f"{a_score} {b_score}"

print(triplet_comparison("""
5 6 7
3 6 10
"""))