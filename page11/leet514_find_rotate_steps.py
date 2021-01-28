class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_pos_dict = {}
        for i, char in enumerate(ring):
            if char in char_pos_dict:
                char_pos_dict[char].append(i)
            else:
                char_pos_dict[char] = [i]

        LEN = len(ring)
        states = [-1] * LEN
        states[0] = 0
        for char in key:
            poses = char_pos_dict[char]
            new_states = [-1] * LEN
            for i, state in enumerate(states):
                if state == -1:
                    continue
                else:
                    for pos in poses:
                        transfer = min(abs(pos - i), (LEN - abs(pos - i))) + 1
                        if state + transfer < new_states[pos] or new_states[pos] == -1:
                            new_states[pos] = state + transfer
            states = new_states
        min_state = max(states)
        for state in states:
            if state == -1:
                continue
            if state < min_state:
                min_state = state
        return min_state

if __name__ == "__main__":
    solution = Solution()
    print(solution.findRotateSteps("pqwcx","cpqwx"))