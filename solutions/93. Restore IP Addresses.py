class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def valid(current_add: str) -> bool:
            if current_add.count('.') != 3:
                return False
            splited = current_add.split('.')
            if len(splited) != 4:
                return False
            for dstr in splited:
                if len(dstr) == 0:
                    return False
                val = int(dstr)
                if str(val) != dstr:
                    return False
                if val < 0 or val > 255:
                    return False
            return True
        def backtrack(insert_idx: int, current_add: str) -> None:
            # insert_idx : insert a dot after insert_idx
            if valid(current_add):
                result.append(current_add)
                return
            if current_add.count('.') >= 3:
                return
            if insert_idx >= len(current_add)-1:
                return
            inserted = current_add[:insert_idx+1] + '.' + current_add[insert_idx+1:]
            backtrack(insert_idx+2, inserted)
            backtrack(insert_idx+1, current_add)

        backtrack(0, s)
        return result
