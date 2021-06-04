#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        # DP[i][j] saves the lcs length b/w text1[:i+1] and text2[:j+1]
        DP = [ [ "" for j in range(len2) ] for i in range(len1) ]

        res = 0
        for i in range(len1):
            for j in range(len2):
                #print("i="+ str(i) + ",j=" + str(j))
                prevd = ""; previ = ""; prevj = ""
                # upper 
                if (i > 0):
                    previ = DP[i-1][j]
                # left
                if (j > 0):
                    prevj = DP[i][j-1]
                # upper-left diagnal
                if (i > 0 and j > 0):
                    prevd = DP[i-1][j-1]
                if (text1[i] == text2[j]):
                    DP[i][j] = prevd + text2[j]
                    if(len(DP[i][j])>res): 
                        res = len(DP[i][j])
                else: 
                    DP[i][j] = previ if (len(previ) > len(prevj)) else prevj
                    #print("DP[" + str(i) + "]["+str(j)+"]=" + DP[i][j])
                j += 1
            i += 1    
        return res  
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        text1 = str1; text2 = str2
        len1 = len(text1)
        len2 = len(text2)
        
        # DP[i][j] saves the csc between text1[:i+1] and text2[:j+1]
        DP = [ [ "" for j in range(len2) ] for i in range(len1) ]
        # DPLastI[i][j], store the index of last character of text1[:i+1] for the LCS between text1[:i+1] and text2[:j+1]
        DPLastI = [ [ -1 for j in range(len2) ] for i in range(len1) ]
        # DPLastJ[i][j], store the index of last character of text2[:j+1] for the LCS between text1[:i+1] and text2[:j+1]
        DPLastJ = [ [ -1 for j in range(len2) ] for i in range(len1) ]

        LCSLen = 0; LCSLasti = -1; LCSLastj = -1
        for i in range(len1):
            for j in range(len2):
                prevRow = ""; prevRowLastI = -1; prevRowLastJ = -1
                prevCol = ""; prevColLastI = -1; prevColLastJ = -1
                prevDiag = ""; prevDiagLastI = -1; prevDiagLastJ = -1
                if (i > 0):
                    prevRow = DP[i-1][j]
                    prevRowLastI = DPLastI[i-1][j]
                    prevRowLastJ = DPLastJ[i-1][j]
                if (j > 0):
                    prevCol = DP[i][j-1]
                    prevColLastI = DPLastI[i][j-1]
                    prevColLastJ = DPLastJ[i][j-1]
                if (i > 0 and j > 0):
                    prevDiag = DP[i-1][j-1]
                    prevDiagLastI = DPLastI[i-1][j-1]
                    prevDiagLastJ = DPLastJ[i-1][j-1]
                if (text1[i] == text2[j]):
                    # when there is a match, use the last found LCS plus all the characters scanned so far
                    DP[i][j] = prevDiag + text1[prevDiagLastI+1:i] + text2[prevDiagLastJ+1:j] + text1[i]
                    DPLastI[i][j] = i;
                    DPLastJ[i][j] = j;
                    # need to calculate the current LCS length, if we find a longer LCS
                    # we need to replace the LCS index
                    # we need the index because DP[i][j] stores the Shortest Common Supersequence 
                    curLCSLen = (i+1) + (j+1) - len(DP[i][j])
                    if(curLCSLen > LCSLen):
                        LCSLen = curLCSLen
                        LCSLasti = i;
                        LCSLastj = j;
                else:
                    # compare the row above with the column to the left
                    # copy that with longer LCS
                    # calculate the LCS with the formula that leni + lenj - len supersequence
                    if (prevRowLastI+1+prevRowLastJ+1-len(prevRow) > prevColLastI+1+prevColLastJ+1-len(prevCol)): 
                        DP[i][j] = prevRow
                        DPLastI[i][j] = prevRowLastI
                        DPLastJ[i][j] = prevRowLastJ
                    else:
                        DP[i][j] = prevCol 
                        DPLastI[i][j] = prevColLastI
                        DPLastJ[i][j] = prevColLastJ
                j += 1
            i += 1    
        if(LCSLasti < 0): res = "";
        else: res = DP[LCSLasti][LCSLastj]
        #print("Lasti="+str(LCSLasti)+", Lastj="+str(LCSLastj)+",DP="+res)
        # if there are characters not matched after the LCS, need to append them at the end
        if(LCSLasti < len1-1): res += text1[LCSLasti+1:]
        if(LCSLastj < len2-1): res += text2[LCSLastj+1:]

        return res


# In[18]:


s = Solution()

text1 = "abced"
text2 = "ace"
print(s.longestCommonSubsequence(text1,text2))

text1 = "bsbininm"
text2 = "jmjkbkjkv"
print(s.longestCommonSubsequence(text1,text2))

text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"
print(s.longestCommonSubsequence(text1,text2))

text1 = "uvirivwbkdijstyjgdahmtutav"
text2 = "apazcdspcnolsvmlorqxazglyjq"
print(s.longestCommonSubsequence(text1,text2))

text1 = "atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllqmvptwammerobtgmkpowndejvbuwbporfyroknrjoekdgqqlgzxiisweeegxajqlradgcciavbpgqjzwtdetmtallzyukdztoxysggrqkliixnagwzmassthjecvfzmyonglocmvjnxkcwqqvgrzpsswnigjthtkuawirecfuzrbifgwolpnhcapzxwmfhvpfmqapdxgmddsdlhteugqoyepbztspgojbrmpjmwmhnldunskpvwprzrudbmtwdvgyghgprqcdgqjjbyfsujnnssfqvjhnvcotynidziswpzhkdszbblustoxwtlhkowpatbypvkmajumsxqqunlxxvfezayrolwezfzfyzmmneepwshpemynwzyunsxgjflnqmfghsvwpknqhclhrlmnrljwabwpxomwhuhffpfinhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdipldofyvfdurbsoxdurlofkqnrjomszjimrxbqzyazakkizojwkuzcacnbdifesoiesmkbyffcxhqgqyhwyubtsrqarqagogrnaxuzyggknksrfdrmnoxrctntngdxxechxrsbyhtlbmzgmcqopyixdomhnmvnsafphpkdgndcscbwyhueytaeodlhlzczmpqqmnilliydwtxtpedbncvsqauopbvygqdtcwehffagxmyoalogetacehnbfxlqhklvxfzmrjqofaesvuzfczeuqegwpcmahhpzodsmpvrvkzxxtsdsxwixiraphjlqawxinlwfspdlscdswtgjpoiixbvmpzilxrnpdvigpccnngxmlzoentslzyjjpkxemyiemoluhqifyonbnizcjrlmuylezdkkztcphlmwhnkdguhelqzjgvjtrzofmtpuhifoqnokonhqtzxmimp"
text2 = "xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhfafiervrsyuiseumzmymtvsdsowmovagekhevyqhifwevpepgmyhnagjtsciaecswebcuvxoavfgejqrxuvnhvkmolclecqsnsrjmxyokbkesaugbydfsupuqanetgunlqmundxvduqmzidatemaqmzzzfjpgmhyoktbdgpgbmjkhmfjtsxjqbfspedhzrxavhngtnuykpapwluameeqlutkyzyeffmqdsjyklmrxtioawcrvmsthbebdqqrpphncthosljfaeidboyekxezqtzlizqcvvxehrcskstshupglzgmbretpyehtavxegmbtznhpbczdjlzibnouxlxkeiedzoohoxhnhzqqaxdwetyudhyqvdhrggrszqeqkqqnunxqyyagyoptfkolieayokryidtctemtesuhbzczzvhlbbhnufjjocporuzuevofbuevuxhgexmckifntngaohfwqdakyobcooubdvypxjjxeugzdmapyamuwqtnqspsznyszhwqdqjxsmhdlkwkvlkdbjngvdmhvbllqqlcemkqxxdlldcfthjdqkyjrrjqqqpnmmelrwhtyugieuppqqtwychtpjmloxsckhzyitomjzypisxzztdwxhddvtvpleqdwamfnhhkszsfgfcdvakyqmmusdvihobdktesudmgmuaoovskvcapucntotdqxkrovzrtrrfvoczkfexwxujizcfiqflpbuuoyfuoovypstrtrxjuuecpjimbutnvqtiqvesaxrvzyxcwslttrgknbdcvvtkfqfzwudspeposxrfkkeqmdvlpazzjnywxjyaquirqpinaennweuobqvxnomuejansapnsrqivcateqngychblywxtdwntancarldwnloqyywrxrganyehkglbdeyshpodpmdchbcc"
print(s.longestCommonSubsequence(text1,text2))


# In[19]:


text1 = "abced"
text2 = "ace"
lcslength = s.longestCommonSubsequence(text1,text2)
scs = s.shortestCommonSupersequence(text1,text2)
print("len1={}, len2={},LCS len={}, SCS len={}".format(len(text1),len(text2), lcslength, len(scs)))

text1 = "abcab"
text2 = "cbab"
lcslength = s.longestCommonSubsequence(text1,text2)
scs = s.shortestCommonSupersequence(text1,text2)
print("len1={}, len2={},LCS len={}, SCS len={}".format(len(text1),len(text2), lcslength, len(scs)))

text1 = "bsbininm"
text2 = "jmjkbkjkv"
lcslength = s.longestCommonSubsequence(text1,text2)
scs = s.shortestCommonSupersequence(text1,text2)
print("len1={}, len2={},LCS len={}, SCS len={}".format(len(text1),len(text2), lcslength, len(scs)))

text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"
lcslength = s.longestCommonSubsequence(text1,text2)
scs = s.shortestCommonSupersequence(text1,text2)
print("len1={}, len2={},LCS len={}, SCS len={}".format(len(text1),len(text2), lcslength, len(scs)))

text1 = "uvirivwbkdijstyjgdahmtutav"
text2 = "apazcdspcnolsvmlorqxazglyjq"
lcslength = s.longestCommonSubsequence(text1,text2)
scs = s.shortestCommonSupersequence(text1,text2)
print("len1={}, len2={},LCS len={}, SCS len={}".format(len(text1),len(text2), lcslength, len(scs)))

text1 = "atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllqmvptwammerobtgmkpowndejvbuwbporfyroknrjoekdgqqlgzxiisweeegxajqlradgcciavbpgqjzwtdetmtallzyukdztoxysggrqkliixnagwzmassthjecvfzmyonglocmvjnxkcwqqvgrzpsswnigjthtkuawirecfuzrbifgwolpnhcapzxwmfhvpfmqapdxgmddsdlhteugqoyepbztspgojbrmpjmwmhnldunskpvwprzrudbmtwdvgyghgprqcdgqjjbyfsujnnssfqvjhnvcotynidziswpzhkdszbblustoxwtlhkowpatbypvkmajumsxqqunlxxvfezayrolwezfzfyzmmneepwshpemynwzyunsxgjflnqmfghsvwpknqhclhrlmnrljwabwpxomwhuhffpfinhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdipldofyvfdurbsoxdurlofkqnrjomszjimrxbqzyazakkizojwkuzcacnbdifesoiesmkbyffcxhqgqyhwyubtsrqarqagogrnaxuzyggknksrfdrmnoxrctntngdxxechxrsbyhtlbmzgmcqopyixdomhnmvnsafphpkdgndcscbwyhueytaeodlhlzczmpqqmnilliydwtxtpedbncvsqauopbvygqdtcwehffagxmyoalogetacehnbfxlqhklvxfzmrjqofaesvuzfczeuqegwpcmahhpzodsmpvrvkzxxtsdsxwixiraphjlqawxinlwfspdlscdswtgjpoiixbvmpzilxrnpdvigpccnngxmlzoentslzyjjpkxemyiemoluhqifyonbnizcjrlmuylezdkkztcphlmwhnkdguhelqzjgvjtrzofmtpuhifoqnokonhqtzxmimp"
text2 = "xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhfafiervrsyuiseumzmymtvsdsowmovagekhevyqhifwevpepgmyhnagjtsciaecswebcuvxoavfgejqrxuvnhvkmolclecqsnsrjmxyokbkesaugbydfsupuqanetgunlqmundxvduqmzidatemaqmzzzfjpgmhyoktbdgpgbmjkhmfjtsxjqbfspedhzrxavhngtnuykpapwluameeqlutkyzyeffmqdsjyklmrxtioawcrvmsthbebdqqrpphncthosljfaeidboyekxezqtzlizqcvvxehrcskstshupglzgmbretpyehtavxegmbtznhpbczdjlzibnouxlxkeiedzoohoxhnhzqqaxdwetyudhyqvdhrggrszqeqkqqnunxqyyagyoptfkolieayokryidtctemtesuhbzczzvhlbbhnufjjocporuzuevofbuevuxhgexmckifntngaohfwqdakyobcooubdvypxjjxeugzdmapyamuwqtnqspsznyszhwqdqjxsmhdlkwkvlkdbjngvdmhvbllqqlcemkqxxdlldcfthjdqkyjrrjqqqpnmmelrwhtyugieuppqqtwychtpjmloxsckhzyitomjzypisxzztdwxhddvtvpleqdwamfnhhkszsfgfcdvakyqmmusdvihobdktesudmgmuaoovskvcapucntotdqxkrovzrtrrfvoczkfexwxujizcfiqflpbuuoyfuoovypstrtrxjuuecpjimbutnvqtiqvesaxrvzyxcwslttrgknbdcvvtkfqfzwudspeposxrfkkeqmdvlpazzjnywxjyaquirqpinaennweuobqvxnomuejansapnsrqivcateqngychblywxtdwntancarldwnloqyywrxrganyehkglbdeyshpodpmdchbcc"
lcslength = s.longestCommonSubsequence(text1,text2)
scs = s.shortestCommonSupersequence(text1,text2)
print("len1={}, len2={},LCS len={}, SCS len={}".format(len(text1),len(text2), lcslength, len(scs)))


# In[ ]:




