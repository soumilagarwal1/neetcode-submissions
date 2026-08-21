class Solution:

    def encode(self, strs: List[str]) -> str:
        bigwrd = ""
        for word in strs:
            bigwrd += str(len(word)) + "#" + word
        return bigwrd

    def decode(self, s: str) -> List[str]:
        bigwrd = list(s)
        ln = ""
        output = []
        c = 0
        i = 0
        while i < len(s):
            if s[i] != "#":
                ln += s[i]
                i += 1
            else:
                ln = int(ln)
                smwrd = bigwrd[i+1:1+i+ln]
                output.append("".join(smwrd))
                i += 1+ln
                ln = ""
                
        return output
                



