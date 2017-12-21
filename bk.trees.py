def Levenshteind(a, b):
	# Generate the length of both strings, which would be relevant in calculating the Levenshtein distance
	lena, lenb = len(a), len(b)
  
	# Create a table for storing the solutions as done in dynamic programming
	storage = [[0 for x in range(lenb+1)] for x in range(lena+1)]
  
	#Use dynamic programming to solve the problem in a bottom up fashion, by solving sub-problems
	for i in range(lena+1):
    	for j in range(lenb+1):
	
		#fill up the base cases where either the first string or second string has length 0
        #if the first string has a length of 0, then insertions equal to the length
        #of the second string were done to get from the first string to the second.
        	if i == 0:
        		storage[i][j] = j
		
        #if the second string has a length of 0, then deletions equal in number to the
        # length of the first string were done on the first string to get to the second string
      		elif j == 0:
        		storage[i][j] = i
		
        #if both strings have the same last characters, then no change was done on the last character
        # of the first string to get to the last character of the second string. Therefore, the number
        #of changes would be equal to the changes done on the remaining characters of the first string
        #to get to the remaining characters of the second
        	elif a[i-1] == b[j-1]:
        		storage[i][j] = storage[i-1][j-1]
		
        #if both strings have different last characters, then a change was done to get from the first
        # string to the second string. This change could either be an insertion, deletion or mutation,
        # but never three of them at the same time. The change done will be 1 plus the previous record
        # state of insertion, deletion or mutation
      		else:
        		storage[i][j] = 1 + min(storage[i][j - 1], storage[i - 1][j], storage[i - 1][j - 1])
		
    return storage[lena][lenb]
  
Levenshteind(“aaaasss”, “as”)

class BkTree:
	#An implementation of a BKTree. This tree allows
	# operations such as insertion, building up the
	# tree and querying the tree, or finding elements
	# of the tree which are within a specified difference
	# from a given string
	def __init__ ( self , list, distancefunction):
		#The initializer takes the list used in building
		# the tree and the distance function
		#The distance function in this case would
		# be the Levenshtein distance
		#The initializer also assigns the first element
		# in the list as the parent node, and adds
		#it to the discionary used for storage.
		self .df = distancefunction
		self .root = list[ 0 ]
		self .tree = (list[ 0 ], {})
		
	def builder( self , list):
		#This part of the code builds the tree by adding
		# words from the input list to the dictionary
		#storage using the class insert method
		for word in list[ 1 :]:
		self .tree = self .insert( self .tree, word)
		
	def insert( self , node, word):
		#This method is used for inserting a word into the tree.
		# As shown in the main article, it first
		#takes the distance between the word and the parent node.
		# If the distance isn't already the weight
		#of an edge of the parent, it attaches it to the parent
		# node. Else, it recursively attempts this with
		#the children of the parent, and their children
		d = self .df(word, node[ 0 ])
		if d not in node[ 1 ]:
			node[ 1 ][d] = (word, {})
		else :
			self .insert(node[ 1 ][d], word)
		return node
		
	def tester( self , testword, n):
		#This method performs the actual querying of the bk
		# tree to search for elements in the tree that have a
		#specified number of distance from the given string.
		# It does using another function, search function which
		#first tests for the distance between the parent of the
		# bk tree and the given string. It also appends
		#the parent string to the output list if it satisfies the
		# criteria. If not, it applies the triangle inequality,
		#checking on edges with weights that don't immediately disobey
		# the triangle inequality and adding them to the
		#Output list.
		def search(node):
			d = self.df(testword, node[ 0 ])
			output = []
			if d <= n:
				output.append(node[ 0 ])
			for i in range (d - n, d + n + 1 ):
				child = node[ 1 ]
				if i in child:
					output.extend(search(node[ 1 ][i]))
			return output
		root = self .tree
		return search(root)
		
#This part of the code is a test function , that just tests a sample case
if __name__ == '__main__' :
	list = [ "min" , "food" , "nyash" , "dog" , "life" ]
	tree = BkTree(list, Levenshteind)
	tree.builder(list)
	print tree.tester( 'man' , 2 )
	#Output: min
