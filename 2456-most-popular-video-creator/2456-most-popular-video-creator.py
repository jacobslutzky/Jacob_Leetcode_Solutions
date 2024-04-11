class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = {}
        num_videos = len(creators)
        output = []
        max_pop = -1
        for i in range(num_videos):
            if creators[i] in d:
                d[creators[i]][0] += views[i]
                if views[i] > d[creators[i]][1]:
                    d[creators[i]][1] = views[i]
                    d[creators[i]][2] = ids[i]
                elif views[i] == d[creators[i]][1] and ids[i] < d[creators[i]][2]:
                    d[creators[i]][2] = ids[i]
            else:
                d[creators[i]] = [views[i], views[i], ids[i]]
            if d[creators[i]][0] > max_pop:
                max_pop =  d[creators[i]][0]
                output = [[creators[i],d[creators[i]][2]]]
            elif d[creators[i]][0] == max_pop and (views[i]!=0 or views[i]==d[creators[i]][0]):
                output.append([creators[i],d[creators[i]][2]])
        return output