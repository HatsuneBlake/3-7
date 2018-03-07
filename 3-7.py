class ListInstance(object):
	def __str__(self):
		 return '[Instance of %s]\n[Address]:%s\n%s' % (
				self.__class__.__name__,
				id(self),
				self.__attrinfo())
	def __attrinfo(self):
		r = 'Info:\n'
		for attr in self.__dict__:
			r += '\t%s=%s \n' % (attr,self.__dict__[attr])
		return r



if __name__ == '__main__':
	class TestClass(ListInstance):
		def __init__(self,value):
			self.value1 = value
			self.value2 = 's'
		def method(self):
			pass

	x = TestClass(1)
	print x