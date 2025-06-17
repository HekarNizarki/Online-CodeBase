def findLadders(beginWord,endWord,wordList):
    from collections import defaultdict,deque
    wordList=set(wordList)
    if endWord not in wordList:
        return []
    graph=defaultdict(list)
    queue=deque([beginWord])
    found=False
    while queue and not found:
        level_size=len(queue)
        visited=set()
        for _ in range(level_size):
            word=queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word=word[:i]+c+word[i+1:]
                    if new_word==endWord:
                        found=True
                    if new_word in wordList:
                        visited.add(new_word)
                        graph[word].append(new_word)
        for word in visited:
            wordList.remove(word)
            queue.append(word)
    result=[]
    def backtrack(word,path):
        if word==endWord:
            result.append(path)
            return
        for neighbor in graph[word]:
            backtrack(neighbor,path+[neighbor])
    backtrack(beginWord,[beginWord])
    return result