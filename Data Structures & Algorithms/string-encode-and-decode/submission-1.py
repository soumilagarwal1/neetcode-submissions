class Solution:

    def encode(self, strs: List[str]) -> str:
        bigstr = ""
        for s in strs:
            bigstr += str(len(s)) + "#" + s 
        return bigstr


    def decode(self, s: str) -> List[str]:
        strlist = []
        biglist = list(s)
        while biglist:
            lnth = ""
            for ltr in biglist:
                if ltr == "#":
                    break
                else:
                    lnth += ltr
            start = len(lnth)
            end = int(lnth)
            smlist = biglist[start+1:end+1+start]
            del biglist[0:end+start+1]
            strlist.append("".join(smlist))
        return strlist

