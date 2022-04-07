def BinaryTree():
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def setRightChild(self, obj):
        self.rightChild = obj

    def setLeftChild(self, obj):
        self.leftChild = obj

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

