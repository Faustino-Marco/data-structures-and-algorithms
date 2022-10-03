from data_structures.stack import Stack

def multi_bracket_validation(string):
    open_stack = Stack()
    openers = ["{","[","("]
    closers = ["}","]",")"]
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    chars = list(string)
    for char in chars:
        if char in openers:
            open_stack.push(char)

        if char in closers:
            if open_stack.is_empty():
                return False

            if pairs.get(char) == open_stack.peek():
                open_stack.pop()
            else:
                return False

    return True


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
            
        


