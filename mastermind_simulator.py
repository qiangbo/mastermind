"""

MasterMind simulator.

Bo Qiang

"""
# ==========  IMPORTS  ====================================================== #
import sys
import datetime
import random

# ==========  CONSTANTS  ==================================================== #
CODE_PEGS = ["black","white","red","green","blue","yellow"]
CODE_LENGTH = 4

# ==========  FUNC: GENERATE A RANDOM CODE  ================================= #
def random_code():
    code = [random.choice(CODE_PEGS) for i in range(CODE_LENGTH)]
    return(code)

# ==========  FUNC: GENERATE KEY PEG  ======================================= #
def evaluate_attempt(code,attempt):

    outcome = [None]*CODE_LENGTH
    black = 0
    leftover_code = []
    leftover_attempt = []
    for i in range(CODE_LENGTH):
        if(attempt[i]==code[i]):
            black += 1
        else:
            leftover_code.append(code[i])
            leftover_attempt.append(attempt[i])
    white = 0
    for i in range(len(leftover_code)):
        if(leftover_attempt[i] in leftover_code):
            white += 1
            leftover_code.remove(leftover_attempt[i])

    return({"black":black,"white":white})

# ==========  CLASS: CODE MAKER  ============================================ #
class CodeMaker():

    def __init__(self,code=None):
        if(code is None):
            code = random_code()
        self.code = code
    
    def key_peg(self,attempt):
        return(evaluate_attempt(self.code,attempt))

# ==========  CLASS: CODE BREAKER  ========================================== #
class CodeBreaker():

    def __init__(self):
        attempts = []
        candidates = []
        for this_code_0 in CODE_PEGS:
            for this_code_1 in CODE_PEGS:
                for this_code_2 in CODE_PEGS:
                    for this_code_3 in CODE_PEGS:
                        candidates.append({"code":[this_code_0,this_code_1,this_code_2,this_code_3],"valid":True})
        self.attempts = attempts
        self.candidates = candidates

    def generate_attempt(self):
        valid_candidates = []
        for this_candidate in self.candidates:
            if(this_candidate["valid"]==True):
                valid_candidates.append(this_candidate["code"])
        attempt = random.choice(valid_candidates)
        return(attempt)
    
    def validate_candidates(self,code,key_peg):
        candidates = self.candidates
        candidates_new = []
        for this_candidate in candidates:
            key_peg_ = evaluate_attempt(code,this_candidate["code"])
            if((key_peg_["black"]!=key_peg["black"]) or (key_peg_["white"]!=key_peg["white"])):
                candidates_new.append({"code":this_candidate["code"],"valid":False})
            else:
                candidates_new.append(this_candidate)
        self.candidates = candidates_new

# ==========  PROCESS  ====================================================== #
if (__name__ == "__main__"):

    # ----------  parameters  ----------------------------------------------- #
    # both | breaker
    role = "both"

    # ----------  parse input arguments  ------------------------------------ #
    if(len(sys.argv)>=2):
        role = sys.argv[1]

    # ----------  initialize random seed  ----------------------------------- #
    random_seed = datetime.datetime.utcnow()
    random.seed(random_seed)

    # ----------  simulate both sides  -------------------------------------- #
    if(role=="both"):
        code = random_code()
        print("code maker set to: %s"%(str(code)))
        code_maker = CodeMaker(code)
        code_breaker = CodeBreaker()
        print("code breaker start cracking:")
        for i in range(10):
            attempt = code_breaker.generate_attempt()
            key_peg = code_maker.key_peg(attempt)
            code_breaker.validate_candidates(attempt,key_peg)
            if(key_peg["black"]==CODE_LENGTH):
                print("attempt %d: %s, key pegs: %s"%(i+1,str(attempt),str(key_peg)))
                print("solution reached after %dth attempt"%(i+1))
                break
            else:
                print("attempt %d: %s, key pegs: %s"%(i+1,str(attempt),str(key_peg)))
    # ----------  role = breaker  ------------------------------------------- #
    elif(role=="breaker"):
        code_breaker = CodeBreaker()
        for i in range(10):
            attempt = code_breaker.generate_attempt()
            print("attempt %d: %s"%(i+1,str(attempt)))
            black_pegs = input("num of black pegs:")
            white_pegs = input("num of white pegs:")
            code_breaker.validate_candidates(attempt,{"black":int(black_pegs),"white":int(white_pegs)})
            if(black_pegs==CODE_LENGTH):
                print("solution reached after %dth attempt"%(i+1))
                break
    # ----------  unrecognized role  ---------------------------------------- #
    else:
        print("unrecognized role (%s)"%(role))
