def findWords(board,words):
    class TrieNode:
        def __init__(self):
            self.children={}
            self.word=None
    def build_trie(words):
        root=TrieNode()
        for word in words:
            node=root
            for char in word:
                if char not in node.children:
                    node.children[char]=TrieNode()
                node=node.children[char]
            node.word=word
        return root
    def dfs(i,j,node):
        char=board[i][j]
        if char not in node.children:
            return
        node=node.children[char]
        if node.word:
            result.append(node.word)
            node.word=None
        board[i][j]='#'
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x,y=i+dx,j+dy
            if 0<=x<m and 0<=y<n and board[x][y]!='#':
                dfs(x,y,node)
        board[i][j]=char
    root=build_trie(words)
    m,n=len(board),len(board[0])
    result=[]
    for i in range(m):
        for j in range(n):
            dfs(i,j,root)
    return result