class Solution:
    def isPalindrome(self, s: str) -> bool:
        sorted_str = ''.join(s.split()).lower()
        clean_text = re.sub(r'\W+', '', sorted_str)
        if clean_text == clean_text[::-1]:
            return True
        else:
            return False
        