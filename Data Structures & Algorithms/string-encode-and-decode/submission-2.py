class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        delimiter = ";;"
        for i in range(len(strs)):
            output += strs[i]
            if i < len(strs) -1: output += delimiter

        if len(strs) == 0: output = "None"
        return output

    def decode(self, s: str) -> List[str]:
        if s is "None": return [] 
        return s.split(";;")
