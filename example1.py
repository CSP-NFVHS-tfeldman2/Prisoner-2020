####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'GloryfulTomatoes'
strategy_name = 'Complex'
strategy_description = 'Tries to read the opposing team.'
    
def move(my_history, their_history, my_score, their_score):
    my_history = 'c'
    if my_history[-1] and their_history[-1] == 'b':
        return 'b'
    else:
        return 'c'
    if my_history[-1] and their_history[-1] == 'c':
        return 'b'
    if their_history[-1] and their_history[-2] == 'c':
        return 'b'
    if their_history[-1] == 'b':
        return 'c'