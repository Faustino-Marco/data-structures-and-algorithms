# from data_structures.stack_and_queue.queue import Queue

# square_queue_open = []
# square_queue_closed = []
# round_queue_open = []
# round_queue_closed = []
# curly_queue_open = []
# curly_queue_closed = []

open_bracks = Stack()
openers = ["(", "[", "{"]
closers = [")", "]", "}"]
matches = ["()", "[]", "{}"]

def multi_bracket_validation(bracks):
    if len(bracks) // 2 != 0:
        return False
    elif bracks[0] in closers:
        return False
    else:
        for x in len(bracks):
            if bracks[x] in openers:
                open_bracks.push(x)
                continue
            else:
                print("hello world")
                match_combo = (bracks[0] + open_bracks.peek())
                print(match_combo)
                if (bracks[0] + open_bracks.peek()) in matches:
                    open_bracks.pop()
                    continue
                else:
                    return False

            

multi_bracket_validation("[[{}]]")


        # for let in bracks:
        #     if let == "[":
        #         square_queue_open.append(let)
        #     elif let == "]":
        #         square_queue_closed.append(let)
        #     elif let == "(":
        #         round_queue_open.append(let)
        #     elif let == ")":
        #         round_queue_closed.append(let)
        #     elif let == "{":
        #         curly_queue_open.append(let)
        #     elif let == "}":
        #         curly_queue_closed.append(let)
        # if len(square_queue_open) == len(square_queue_closed) and len(round_queue_open) == len(round_queue_closed) and len(curly_queue_open) == len(curly_queue_closed):
        #     return True
            
        

multi_bracket_validation("[[{}]]")

