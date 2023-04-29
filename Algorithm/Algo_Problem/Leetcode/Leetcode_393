class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        utf_mask = [(0, 128), (192, 32), (224, 16), (240, 8)]

        def valid_utf(idx):
            n_byte = 0
            for i in range(4):
                if data[idx] ^ utf_mask[i][0] < utf_mask[i][1]:
                    n_byte = i + 1
                    break

            if n_byte:
                for i in range(idx + 1, idx + n_byte):
                    if i == len(data) or data[i] ^ 128 >= 64:
                        return False, idx + n_byte
                else:
                    return True, idx + n_byte
            else:
                return False, idx + n_byte

        answer, idx = True, 0
        while answer and idx < len(data):
            answer, idx = valid_utf(idx)

        return answer
