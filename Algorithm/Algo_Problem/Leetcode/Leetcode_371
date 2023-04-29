class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        carry, b = ((a & b) << 1) & mask, (a ^ b) & mask
        while carry:
            b, carry = (b ^ carry) & mask, ((b & carry) << 1) & mask
        return ~(b ^ mask) if b >> 31 else b