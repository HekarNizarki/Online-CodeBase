def alienOrder(words):
    from collections import defaultdict,deque
    graph=defaultdict(set)
    in_degree={char:0 for word in words for char in word}
    for i in range(len(words)-1):
        word1,word2=words[i],words[i+1]
        for j in range(min(len(word1),len(word2))):
            if word1[j]!=word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]]+=1
                break
        else:
            if len(word1)>len(word2):
                return ''
    queue=deque([char for char in in_degree if in_degree[char]==0])
    result=''
    while queue:
        char=queue.popleft()
        result+=char
        for neighbor in graph[char]:
            in_degree[neighbor]-=1
            if in_degree[neighbor]==0:
                queue.append(neighbor)
    return result if len(result)==len(in_degree) else ''