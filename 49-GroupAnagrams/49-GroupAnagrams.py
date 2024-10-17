class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        idea: make a map of each group. eg: aet:[ate, eat, tea] where the keys are the ana sorted.
        initiate a map:
        for word in strs:
            if sorted(word) in map.keys: 
                add word to the accorded keys
                map[sorted(word)].append(word)
            else:
                set new sorted value to map
        '''
        ana_groups = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in ana_groups: 
                ana_groups[sorted_word].append(word)
            else:
                ana_groups[sorted_word] = [word]

        return list(ana_groups.values())

        ''' 
        Time: O(n*mlogm) (m for length of words)
        Space: O(2(n*m)) ->linear space: O(n*m)'''
