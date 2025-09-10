class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        m = len(languages)
        
        lang_sets = [set(l) for l in languages]
        
       
        non_communicating = []
        for u, v in friendships:
            u -= 1  
            v -= 1
            if lang_sets[u].intersection(lang_sets[v]):
                continue
            non_communicating.append((u, v))
        
        if not non_communicating:
            return 0 
        
       
        users_to_consider = set()
        for u, v in non_communicating:
            users_to_consider.add(u)
            users_to_consider.add(v)
        
        
        min_teach = float('inf')
        for lang in range(1, n + 1):
            teach_count = 0
            for user in users_to_consider:
                if lang not in lang_sets[user]:
                    teach_count += 1
            min_teach = min(min_teach, teach_count)
        
        return min_teach