import random

class Node:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None


class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0


	def insert(self, value, mode='recursive'):
		if self.root == None:
			self.root = Node(value)
			self.size += 1

		else:
			if mode == 'recursive':
				return self._insert(value, self.root)
			elif mode == 'iterative':
				return self._insertIterative(value, self.root)


	def _insert(self, value, current_node):
		if value < current_node.value:
			if current_node.left == None:
				current_node.left = Node(value)
				current_node.left.parent = current_node
				self.size += 1
		
			else:
				return self._insert(value, current_node.left)

		elif value > current_node.value:
			if current_node.right == None:
				current_node.right = Node(value)
				current_node.right.parent = current_node
				self.size += 1
				
			else:
				return self._insert(value, current_node.right)

		else:
			print('{} is already in tree.'.format(value))


	def _insertIterative(self, value, current_node):
		while True:
			if value < current_node.value:
				if current_node.left == None:
					current_node.left = Node(value)
					current_node.left.parent = current_node
					self.size += 1
					break

				else:
					current_node = current_node.left


			elif value > current_node.value:
				if current_node.right == None:
					current_node.right = Node(value)
					current_node.right.parent = current_node
					self.size += 1
					break

				else:
					current_node = current_node.right

			else:
				print('{} is already in tree.'.format(value))
				break


	def search(self, target, mode='recursive'):
		if self.root != None:
			if mode == 'recursive':		
				return self._search(target, self.root)
	
			elif mode == 'iterative':
				return self._searchIterative(target, self.root)

		else:
			print('Tree is empty.')


	def _search(self, target, current_node):
		if current_node.value == target:
			print('{} is in tree.'.format(target))

		elif target < current_node.value and current_node.left != None:
			return self._search(target, current_node.left)

		elif target > current_node.value and current_node.right != None:
			return self._search(target, current_node.right)

		else:
			print('{} is not in tree.'.format(target))


	def _searchIterative(self, target, current_node):
		while True:
			if current_node.value == target:
				print('{} is in tree.'.format(target))
				break

			elif current_node.value < target:
				if current_node.right != None:
					current_node = current_node.right
				
				else:
					print('{} is not in tree.'.format(target))
					break

			else:
				if current_node.left != None:
					current_node = current_node.left

				else:
					print('{} is not in tree.'.format(target))
					break


	def smallestKey(self, mode='recursive'):
		if self.root != None:
			if mode == 'recursive':
				return self._smallestKey(self.root)
			
			elif mode == 'iterative':
				return self._smallestKeyIterative(self.root)
	
		else:
			print('Tree is empty.')


	def _smallestKey(self, current_node):
		if current_node.left != None:
			return self._smallestKey(current_node.left)
		return current_node.value


	def _smallestKeyIterative(self, current_node):
		while current_node.left != None:
			current_node = current_node.left
		return current_node.value


	def largestKey(self, mode='recursive'):
		if self.root != None:
			if mode == 'recursive':
				return self._largestKey(self.root)
			
			elif mode == 'iterative':
				return self._largestKeyIterative(self.root)
		
		else:
			print('Tree is empty.')


	def _largestKey(self, current_node):
		if current_node.right != None:
			return self._largestKey(current_node.right)
		return current_node.value


	def _largestKeyIterative(self, current_node):
		while current_node.right != None:
			current_node = current_node.right
		return current_node.value


	def delete(self, key, mode='recursive'):
		if self.root != None:
			if mode == 'recursive':
				return self._delete(self.root, key)
			elif mode == 'iterative':
				return self._deleteIterative(self.root, key)

		else:
			print('Tree is empty')


	def _delete(self, current_node, key):
		if current_node.value == key:
			if current_node.left != None and current_node.right != None:
				max_val = self._largestKey(current_node.left)
				self.delete(max_val)
				current_node.value = max_val

				# min_val = self._smallestKey(current_node.right)
				# self.delete(min_val)
				# current_node.value = min_val

			elif current_node.left != None:
				if current_node == self.root:
					self.root = self.root.left

				elif current_node.parent.left.value == key:
					current_node.left.parent = current_node.parent
					current_node.parent.left = current_node.left

				else:
					current_node.right.parent = current_node.parent
					current_node.parent.right = current_node.left

				self.size -= 1

			elif current_node.right != None:
				if current_node == self.root:
					self.root = self.root.right

				elif current_node.parent.left.value == key:
					current_node.right.parent = current_node.parent
					current_node.parent.left = current_node.right

				else:
					current_node.right.parent = current_node.parent
					current_node.parent.right = current_node.right

				self.size -= 1
			else:
				if current_node == self.root:
					self.root = None

				elif current_node.parent.left.value == key:
					current_node.parent.left = None

				else:
					current_node.parent.right = None

				self.size -= 1


		elif current_node.value < key:
			if current_node.right != None:
				return self._delete(current_node.right, key)

			else:
				print('{} not in tree.'.format(key))

		else:
			if current_node.left != None:
				return self._delete(current_node.left, key)

			else:
				print('{} not in tree.'.format(key))


	def _deleteIterative(self, current_node, key):
		while True:
			if current_node.value == key:
				if current_node.left != None and current_node.right != None:
					max_val = self._largestKey(current_node.left)
					current_node.value = max_val
					key = max_val
					current_node = current_node.left

					# min_val = self._smallestKey(current_node.right)
					# current_node.value = min_val
					# key = min_val
					# current_node = current_node.right

				elif current_node.left != None:
					if current_node == self.root:
						self.root = self.root.left

					elif current_node.parent.left.value == key:
						current_node.left.parent = current_node.parent
						current_node.parent.left = current_node.left
						print('x')

					else:
						current_node.right.parent = current_node.parent
						current_node.parent.right = current_node.left

					self.size -= 1
					break

				elif current_node.right != None:
					if current_node == self.root:
						self.root = self.root.right

					elif current_node.parent.left.value == key:
						current_node.right.parent = current_node.parent
						current_node.parent.left = current_node.right

					else:
						current_node.right.parent = current_node.parent
						current_node.parent.right = current_node.right

					self.size -= 1
					break
				else:
					if current_node == self.root:
						self.root = None

					elif current_node.parent.left.value == key:
						current_node.parent.left = None

					else:
						current_node.parent.right = None
					self.size -= 1
					break

			elif current_node.value < key:
				if current_node.right != None:
					current_node = current_node.right

				else:
					print('{} not in tree.'.format(key))
					break

			else:
				if current_node.left != None:
					current_node = current_node.left
					
				else:
					print('{} not in tree.'.format(key))
					break


	def traverse(self, order='pre', mode='recursive'):
		if self.root != None:
			if mode == 'recursive':
				if order == "pre":
					return self._preorderTraverse(self.root)
				elif order == 'in':
					return self._inorderTraverse(self.root)
				elif order == 'post':
					return self._postorderTraverse(self.root)

			elif mode == 'iterative':
				if order == "pre":
					return self._preorderTraverseIterative(self.root)
				elif order == 'in':
					return self._inorderTraverseIterative(self.root)
				elif order == 'post':
					return self._postorderTraverseIterative(self.root)


	def _inorderTraverse(self, current_node):
		if current_node != None:
			self._inorderTraverse(current_node.left)
			print(current_node.value)
			self._inorderTraverse(current_node.right)


	def _inorderTraverseIterative(self, current_node):
		traversed = list()
		while True:
			if current_node.left != None and current_node.left.value not in traversed:
				current_node = current_node.left
				continue
			if current_node.value not in traversed:
				print(current_node.value)
				traversed.append(current_node.value)

				if len(traversed) == self.size:
					break

			if current_node.right != None and current_node.right.value not in traversed:
				current_node = current_node.right
			else:
				current_node = current_node.parent
			

	def _preorderTraverse(self, current_node):
		if current_node != None:
			print(current_node.value)
			self._preorderTraverse(current_node.left)
			self._preorderTraverse(current_node.right)


	def _preorderTraverseIterative(self, current_node):
		traversed = list()
		while True:
			if current_node.value not in traversed:
				print(current_node.value)
				traversed.append(current_node.value)

				if len(traversed) == self.size:
					break

			if current_node.left != None and current_node.left.value not in traversed:
				current_node = current_node.left
				continue

			if current_node.right != None and current_node.right.value not in traversed:
				current_node = current_node.right
			else:
				current_node = current_node.parent					


	def _postorderTraverse(self, current_node):
		if current_node != None:
			self._postorderTraverse(current_node.left)
			self._postorderTraverse(current_node.right)
			print(current_node.value)


	def _postorderTraverseIterative(self, current_node):
		traversed = list()
		while True:
			if current_node.left != None and current_node.left.value not in traversed:
				current_node = current_node.left
				continue

			if current_node.right != None and current_node.right.value not in traversed:
				current_node = current_node.right
				continue

			if current_node.value not in traversed:
				print(current_node.value)
				traversed.append(current_node.value)

				if len(traversed) == self.size:
					break

			current_node = current_node.parent


if __name__ == '__main__':
	array = random.sample(range(1, 101), 10)
	print('array = {} \n'.format(array))
	bt = BinarySearchTree()

	for i in array:
		# Insert Modes: recursive (default), iterative
		bt.insert(i, mode='recursive')

	# Search Modes: recursive (default), iterative
	# bt.search(5)

	# Smallest key Modes: recursive (default), iterative
	# bt.smallestKey()

	# Largest Key Modes: recursive (default), iterative
	# bt.largestKey()

	# Delete Modes: recursive (default), iterative
	# bt.delete(5, mode='recursive')
	
	# Traverse Orders: pre (default), in, post
	# Traverse Modes: recursive (default), iterative
	bt.traverse(order='pre', mode='recursive')
