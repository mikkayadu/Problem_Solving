class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        mylist = []
        rem = maxWidth
        #[this is an]
        for word in words:
            if len(word) <= rem:
                rem = rem - len(word)-1
                mylist.append(word)
            else:
                sofar = "".join(mylist)
                left = maxWidth-len(sofar)
                
                if len(mylist) == 1:
                     temp = mylist[0] + " "*(maxWidth - len(mylist[0]))
                     ans.append(temp)
                else:
                    while left:
                        for i in range(len(mylist) -1):
                            mylist[i] = mylist[i] + " "
                            left -=1

                            if left == 0:
                                break
                
                    ans.append("".join(mylist))

                mylist = []
                mylist.append(word)
                rem = maxWidth - len(word) -1
        # last line:
        if len(mylist) == 1:
                     temp = mylist[0] + " "*(maxWidth - len(mylist[0]))
                     ans.append(temp)
        else:
            for i in range(len(mylist) -1):
                 mylist[i] = mylist[i] + " "
                 sentence = "".join(mylist)
            
            remaining = maxWidth - len(sentence)
            ans.append("".join(mylist) + " " * remaining)

        
        return ans



            
