import datetime


# Life Trap Number Key
# 0 Abandonment
# 1 Mistrust and Abuse
# 2 Vulnerability
# 3 Dependence
# 4 Emotional Deprivation
# 5 Social Exclusion
# 6 Defectiveness
# 7 Failure
# 8 Subjugation
# 9 Unrelenting Standards
# 10 Entitlement


class LifeTrapProfile:
    life_trap = {0: "Abandonment",
                 1: "Mistrust and Abuse",
                 2: "Vulnerability",
                 3: "Dependence",
                 4: "Emotional Deprivation",
                 5: "Social Exclusion",
                 6: "Defectiveness",
                 7: "Failure",
                 8: "Subjugation",
                 9: "Unrelenting Standards",
                 10: "Entitlement"
                 }

    def __init__(self, number, name, life_trap_score=None, test_date=None, history=None, question_score=None):
        self.number = number
        self.name = name
        self.life_trap_score = [0 for j in range(11)] if life_trap_score is None else life_trap_score
        self.test_date = "00000000" if test_date is None else test_date
        self.history = ":\n" if history is None else history
        self.question_score = [[0 for j in range(10)] for i in range(11)] if question_score is None else question_score


prompts = [
    # Abandonment
    ('1. I worry a lot that the people I love will die or leave me.',
     '2. I cling to people because I am afraid they will leave me.',
     '3. I do not have a stable base of support.',
     '4. I keep falling in love with people who cannot be there for me in a committed way.',
     '5. People have always come and gone in my life.',
     '6. I get desperate when someone I love pulls away.',
     '7. I get so obsessed with the idea that my lovers will leave me that I drive them away.',
     '8. The people closest to me are unpredictable. One minute they are there for me and the next minute they '
     'are gone.',
     '9. I need other people too much.',
     '10. In the end, I will be alone.'),
    # Mistrust and Abuse
    ('1. I expect people to hurt or use me',
     '2. Throughout my life people close to me have abused me',
     '3. It is only a matter of time before the people I love will betray me',
     '4. I have to protect myself and stay on my guard.',
     '5. If I am not careful, people will take advantage of me.',
     '6. I set up tests for people to see if they are really on my side.',
     '7. I try to hurt people before they hurt me.',
     '8. I am afraid to let people get close to me because I expect them to hurt me.',
     '9. I am angry about what people have done to me.',
     '10. I have been physically, verbally, mentally or sexually abused by people I should have been able to trust.'),
    # Vulnerability
    ('1. I cannot escape the feeling that something bad is about to happen.',
     '2. I feel that catastrophe can strike at any moment.',
     '3. I worry about becoming a street person or vagrant.',
     '4. I worry about being attacked by a criminal, mugger, thief, etc.',
     '5. I worry about getting a serious illness, even though nothing has been diagnosed by a physician.',
     '6. I am too anxious to travel alone on planes, trains, etc.',
     '7. I have anxiety attacks.',
     '8. I am very aware of physical sensations in my body and I worry about what they mean.',
     '9. I worry I will lose control of myself in public or go crazy.',
     '10. I worry a lot about losing all my money or going broke.'),
    # Dependence
    ('1. I feel more like a child than an adult when it comes to handling the responsibilities of daily life.',
     '2. I am not capable of getting by on my own.',
     '3. I cannot cope well by myself.',
     '4. Other people can take care of me better than I can take care of myself.',
     '5. I have trouble tackling new tasks unless I have someone to guide me.',
     '6. I can\'t do anything right.',
     '7. I am inept.',
     '8. I lack common sense.',
     '9. I cannot trust my own judgement.',
     '10. I find everyday life overwhelming.'),
    # Emotional Deprivation
    ('1. I need more love than I get.',
     '2. No one really understands me.',
     '3. I am often attracted to cold partners who can\'t meet my needs.',
     '4. I feel disconnected, even from the people who are closest to me.',
     '5. I have not had one special person I love who wants to share him/herself with me and cares deeply about what '
     'happens to me.',
     '6. No one is there to give me warmth, holding, and affection.',
     '7. I do not have someone who really listens and is tuned into my true needs and feelings.',
     '8. It is hard for me to let people guide or protect me, even though it is what I want inside.',
     '9. It is hard for me to let people love me.',
     '10. I am lonely a lot of the time.'),
    # Social Exclusion
    ('1. I feel very self-conscious in social situations.',
     '2. I feel dull and boring at parties or other gatherings. I never know what to say.',
     '3. The people I want as friends are above me in some way (e.g., looks, popularity, wealth, status, education, '
     'career).',
     '4. I would rather avoid than attend most social functions.',
     '5. I feel unattractive - too fat, thin, tall, short, ugly, etc.',
     '6. I feel fundamentally different from other people.',
     '7. I do not belong anywhere. I am a loner.',
     '8. I always feel on the outside of groups.',
     '9. My family was different from other families around us.',
     '10. I feel disconnected from the community at large.'),
    # Defectiveness
    ('1. No man or woman could love me if he/she really knew me.',
     '2. I am inherently flawed or defective. I am unworthy of love.',
     '3. I have secrets that I do not want to share, even with the people closest to me.',
     '4. It was my fault that my parents could not love me.',
     '5. I hide the real me. The real me is unacceptable. The self I show is a false self.',
     '6. I am often drawn to people - parents, friends, and lovers - who are critical and reject me.',
     '7. I am often critical and rejecting myself, especially of people who seem to love me.',
     '8. I devalue my positive qualities.',
     '9. I live with a great deal of shame about myself.',
     '10. One of my greatest fears is that my faults will be exposed.'),
    # Failure
    ('1. I feel I am less competent than other people in areas of achievement.',
     '2. I feel that I am a failure when it comes to achievement.',
     '3. Most people my age are more successful in their work than I am.',
     '4. I was a failure as a student.',
     '5. I feel I am not as intelligent as most of the people I associate with.',
     '6. I feel humiliated by my failures in the work sphere.',
     '7. I feel embarrassed around other people because I do not measure up in terms of my accomplishments.',
     '8. I often feel that people believe I am more competent.',
     '9. I feel that I do not have any special talents that really count in life.',
     '10. I am working below my potential.'),
    # Subjugation
    ('1. I let other people control me.',
     '2. I am afraid that if I do not give in to other people\'s wishes they will retaliate, get angry, or reject me.',
     '3. I feel the major decisions in my life were not really my own.',
     '4. I have a lot of trouble demanding that other people respect my right.',
     '5. I worry a lot about pleasing people and getting their approval.',
     '6. I go to great lengths to avoid confrontations.',
     '7. I give more to other people than I get back in return.',
     '8. I feel the pain of other people deeply, so I usually end up taking care of the people I\'m close to.',
     '9. I feel guilty when I put myself first',
     '10. I am a good person because I think of others more than of myself.'),
    # Unrelenting Standards
    ('1. I cannot accept second best. I have to be the best at most of what I do.',
     '2. Nothing I do is quite good enough.',
     '3. I strive to keep everything in perfect order.',
     '4. I must look my best at all times.',
     '5. I have so much to accomplish that I have no time to relax.',
     '6. My personal relationships suffer because I push myself so hard.',
     '7. My health suffers because I put myself under so much pressure.',
     '8. I deserve strong criticism when I make a mistake.',
     '9. I am very competitive.',
     '10. Wealth and status are very important to me.'),
    # Entitlement
    ('1. I have trouble accepting "no" as an answer.',
     '2. I get angry when I cannot get what I want.',
     '3. I am special and should not have to accept normal constraints.',
     '4. I put my needs first.',
     '5. I have a lot of difficulty getting myself to stop drinking, smoking, overeating, or other problem behaviours.',
     '6. I cannot discipline myself to complete boring or routine tasks.',
     '7. I act on impulses and emotions that get me into trouble later.',
     '8. If I cannot reach a goal, I become easily frustrated and give up.',
     '9. I insist that people do things my way.',
     '10. I have trouble giving up immediate gratification to reach a long-range goal.')
]


def find_element_indices(phrase, element):
    index = []
    for i in range(len(phrase)):
        if phrase[i] == element:
            index.append(i)
    return index


def make_date_str():
    current_date_str = ""
    if len(str(datetime.datetime.now().day)) == 1:
        current_date_str = "0"
    current_date_str += str(datetime.datetime.now().day)
    if len(str(datetime.datetime.now().month)) == 1:
        current_date_str += "0"
    current_date_str += str(datetime.datetime.now().month)
    current_date_str += str(datetime.datetime.now().year)
    return current_date_str


def extract_user_file(file):
    user_list = []
    user_file = open(file, "r")
    for user in user_file:
        comma_index = find_element_indices(user, ",")
        user_number = int(user[0:comma_index[0]])
        user_name = user[comma_index[0] + 1:comma_index[1]]
        lt_score = [0] * 11
        lt_score_str = user[comma_index[1] + 1:]
        hyphen_index = find_element_indices(lt_score_str, "-")
        for i in range(11):
            lt_score[i] = int(lt_score_str[hyphen_index[i] + 1: hyphen_index[i + 1]])
        period_index = find_element_indices(user, ".")
        latest_date = user[period_index[0] + 1: user.index(":")]
        user_history = user[user.index(":"):]
        user_list.append(LifeTrapProfile(user_number, user_name, lt_score, latest_date, user_history))
    user_file.close()
    return user_list


def extract_user_history(user):
    # :-0-0-15-0-0-0-0-0-0-0-0-.12042020:
    user_history = {}
    colon_index = find_element_indices(user.history, ":")
    if len(colon_index) > 1:
        for colon in colon_index:
            trap_history = user.history[colon + 1:]
            hyphen_index = find_element_indices(trap_history, "-")
            if not hyphen_index:
                break
            else:
                score_list = [0] * 11
                for i in range(11):
                    score_list[i] = int(trap_history[hyphen_index[i] + 1: hyphen_index[i + 1]])
                period = trap_history.index(".")
                score_list.insert(0, trap_history[period + 1: period + 9])
                user_history[len(user_history) + 1] = score_list
    return user_history


def update_user_file(file, user_list):
    user_file = open(file, "w")
    for user in user_list:
        user_file.write(str(user.number) + ",")
        user_file.write(user.name + ",")
        for score in user.life_trap_score:
            user_file.write("-" + str(score))
        user_file.write("-")
        user_file.write("." + user.test_date + user.history)
    user_file.close()


def CONSOLE_run_lt(user_profile, trap_no):
    print("\n" + user_profile.life_trap[trap_no] + "---------------------------------------------------")
    question = 0
    quiz_length = len(prompts[trap_no])
    test_run = True
    while question < quiz_length and test_run:
        print("\n" + prompts[trap_no][question].upper())
        print("(Enter 'b' to go back or 'q' to quit)")
        command = input("Your Answer (1-6): ")
        if command.lower() == 'b':
            if question > 0:
                question -= 1
        elif command.lower() == 'q':
            test_run = False
        else:
            try:
                user_profile.question_score[trap_no][question] = int(command)
                if user_profile.question_score[trap_no][question] < 1 or \
                        user_profile.question_score[trap_no][question] > 6:
                    raise ValueError
                else:
                    question += 1
            except ValueError:
                print("Answer must be a number between 1 and 6.\n")
    if test_run:
        if make_date_str() != user_profile.test_date:
            if user_profile.test_date == "00000000":
                new_history_str = ":\n"
            else:
                new_history_str = ":-"
                for score in user_profile.life_trap_score:
                    new_history_str += str(score)
                    new_history_str += "-"
                new_history_str += "."
                new_history_str += user_profile.test_date
                new_history_str += user_profile.history
            for score in range(len(user_profile.life_trap_score)):
                user_profile.life_trap_score[score] = 0
            user_profile.history = new_history_str
            user_profile.test_date = make_date_str()

        user_profile.life_trap_score[trap_no] = 0
        for q_score in user_profile.question_score[trap_no]:
            user_profile.life_trap_score[trap_no] += q_score

# Main Function variables -------------------------------------------------
menu_prompt = "1. Take Life Trap test\n" \
              "2. View Life Trap score\n" \
              "3. View Life Trap rank\n" \
              "4. Change Current User\n" \
              "5. See Life Trap History\n" \
              "6. Quit"

"""
               10-19: (V. LOW) Probably Does not apply
               20-29: (Fairly LOW) May only apply occasionally 
               30-39: (MODERATE) Is an issue
               40-49: (HIGH) Important Life trap
               50-60: (VERY HIGH) Core life trap
               """
lt_severity = {
    0: "NOT SCORED",
    1: "VERY LOW (Probably does not apply to you)",
    2: "FAIRLY LOW (May only apply occasionally to you)",
    3: "MODERATE (Is an issue)",
    4: "HIGH (Is an important Life Trap)",
    5: "VERY HIGH (Is a core Life Trap)",
    6: "VERY HIGH (Is a core Life Trap)"
}
USER_DATA_FILE = "LifeTrapUserData.txt" # <---------------------------------------------------------------------LINK USER DATA TEXT FILE HERE
default_user = LifeTrapProfile(9999, "Donkey Kong")
user0 = default_user
run = True
# Main Function -----------------------------------------------------------
lt_user_list = extract_user_file(USER_DATA_FILE)
user_not_selected = True
users_not_displayed = True


while run:
    if user_not_selected:
        user_num_lim = lt_user_list[-1].number + 1
        user0 = default_user
        if users_not_displayed:
            for user in lt_user_list:
                print(str(user.number + 1) + ". " + user.name)
            print("N. Create New User")
            users_not_displayed = False

        usernum = input("\nPLEASE SELECT YOUR USER NUMBER, (or enter 'q' to quit): ")
        if usernum.lower() == 'q':
            run = False
        elif usernum.upper() == 'N':
            users_not_displayed = True
            new_user_name = input("Please enter your name, (or press ENTER to return): ")
            if new_user_name != "":
                lt_user_list.append(LifeTrapProfile(lt_user_list[-1].number + 1, new_user_name))
        else:
            try:
                usernum = int(usernum)
                if usernum > user_num_lim or usernum < 1:
                    raise ValueError
                else:
                    user0 = lt_user_list[usernum - 1]
                    user_not_selected = False
            except ValueError:
                print("Please choose a user number between 1 and ".upper() + str(user_num_lim))
    else:
        # In main menu
        print("\nMain Menu (" + user0.name + ")-----------------------------------------------")
        print(menu_prompt)
        mode = input("Please select an option: ")
        print("\n")

        # Take Life Trap test -----------------------------------------------------
        if mode == "1":
            mode_run = True
            while mode_run:
                print("Please select a Life Trap:--------------------------------------")
                for trap in user0.life_trap:
                    print(str(trap + 1) + ". " + user0.life_trap[trap])
                print("12. DO ALL TESTS")
                print("\nEnter 'q' to quit")
                trap_no = input("Life Trap: ")
                if trap_no == 'q':
                    mode_run = False
                else:
                    try:
                        trap_no = int(trap_no) - 1
                        if trap_no == 11:
                            for trap in range(trap_no):
                                CONSOLE_run_lt(user0, trap)
                        elif trap_no>11 or trap_no<1:
                            raise ValueError

                        else:
                            CONSOLE_run_lt(user0, trap_no)
                        mode_run = False
                        lt_user_list[user0.number] = user0
                        update_user_file(USER_DATA_FILE, lt_user_list)
                    except ValueError:
                        print("Invalid Input!")
        # View Life Trap Score ----------------------------------------------------
        elif mode == "2":
            mode_run = True
            while mode_run:
                print("Life Trap Scores (" + user0.name + "):----------------------------------------")
                print("Scores from: " + user0.test_date[0:2] + "/" + user0.test_date[2:4] + "/" + user0.test_date[4:])
                for trap in user0.life_trap:
                    print("- " + user0.life_trap[trap] + ": " + str(user0.life_trap_score[trap]))
                input("\nPress ENTER to return\n")
                mode_run = False
        # View Life Trap Rank -----------------------------------------------------
        elif mode == "3":
            mode_run = True
            while mode_run:
                
                # 10-19: (V. LOW) Probably Does not apply
                # 20-29: (Fairly LOW) May only apply occasionally 
                # 30-39: (MODERATE) Is an issue
                # 40-49: (HIGH) Important Life trap
                # 50-60: (VERY HIGH) Core life trap
                
                print("Ranked Life Traps (" + user0.name + ")-----------------------------------")
                print("Scores from: " + user0.test_date[0:2] + "/" + user0.test_date[2:4] + "/" + user0.test_date[4:])
                rank_traps = list(user0.life_trap.values())
                rank_scores = user0.life_trap_score.copy()
                severity = list(lt_severity.keys())[-1]
                for trap in user0.life_trap:
                    current_trap = rank_traps.pop(rank_scores.index(max(rank_scores)))
                    current_score_int = rank_scores.pop(rank_scores.index(max(rank_scores)))
                    if current_score_int // 10 < severity:
                        severity = current_score_int // 10
                        print("\n" + lt_severity[severity] + ":")
                    print("\t- " + current_trap + ": " + str(current_score_int))

                input("\nPress ENTER to return\n")
                mode_run = False
        # Change current user -----------------------------------------------------
        elif mode == "4":
            user_not_selected = True
            users_not_displayed = True
        # View Life Trap History --------------------------------------------------
        elif mode == "5":
            print("Life Trap History (" + user0.name + ")-----------------")
            past_score = extract_user_history(user0)
            # {1: ['12042020', 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0]}
            date_str = user0.test_date[0:2] + "/" + user0.test_date[2:4] + "/" + user0.test_date[4:]
            print('{:<10s} {:>23s}'.format('Life Trap', date_str), end="")
            for i in range(1, len(past_score)+1):
                date_str = past_score[i][0][0:2] + "/" + past_score[i][0][2:4] + "/" + past_score[i][0][4:]
                print('{:>12s}'.format(date_str), end="")
            print("")
            for trap in user0.life_trap:
                print('{:<23} {:^10s}'.format(user0.life_trap[trap], str(user0.life_trap_score[trap])), end="")
                for i in range(1, len(past_score)+1):
                    print('{:^12d}'.format(past_score[i][trap + 1]), end="")
                print("")
            input("\nPress ENTER to return")
        # Quit Program ------------------------------------------------------------
        elif mode == "6":
            run = False
        else:
            print("Invalid Input!\n")

