import sys

input = sys.stdin.readline
N = int(input())

def preorder(root): #전위 순회
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])#왼쪽 자식
        preorder(tree[root][1])#오른쪽 자식

def inorder(root): #중위 순회
    if root!='.':
        inorder(tree[root][0])#왼쪽 자식
        print(root,end='')
        inorder(tree[root][1])#오른쪽 자식  

def postorder(root):#후위 순회
    if root!='.':
        postorder(tree[root][0])#왼쪽 자식
        postorder(tree[root][1])#오른쪽 자식
        print(root,end='')

tree={}
for _ in range(N):
    root, left, right = input().strip().split()
    tree[root]=[left, right]

preorder('A')
print("")
inorder('A')
print("")
postorder('A')