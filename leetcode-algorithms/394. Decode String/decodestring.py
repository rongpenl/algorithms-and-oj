class parts:
    def __init__(self, num, string):
        # build a stack of parts and aggregates reversely
        self.num = num
        self.string = string


class Solution:
    def decodeString(self, s):
        stack = []
        stack.append(parts(1, ""))
        count = 0
        for char in s:
            if char in "0123456789":
                count = count + \
                    int(char) if count == 0 else count*10 + int(char)
            elif char == "[":
                stack.append(parts(count, ""))
                count = 0
            elif char == "]":
                part = stack.pop()
                # the previous one is always the one that should include the poped one, structurally.
                stack[-1].string += part.num * part.string
            else:
                stack[-1].string += char
        assert(len(stack) == 1)
        return stack[-1].string
