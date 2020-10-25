class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = self.plusone_helper(0, digits)
        if carry > 0:
            digits = [carry] + digits        
        
        return digits
        
    def plusone_helper(self, index, digits):
        if index == len(digits)-1:
            k = digits[index] + 1
            if k > 9:
                digits[index] = 0
                return 1
            else:
                digits[index] = k
                return 0
            
        carry_over = self.plusone_helper(index + 1, digits)
        k = carry_over + digits[index]
        if k > 9:
            digits[index] = 0
            return 1
        else:
            digits[index] = k
            return 0