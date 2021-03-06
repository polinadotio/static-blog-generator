import collections

class SortedDict(collections.MutableMapping):
	def __init__(self, items = None, key=None, reverse=False):
		self._items = {}
		self._keys = []
		if key:
			self._key_fn = lambda k: key(self._items[k])
		else:
			self._key_fn = lambda k: self._items[k]
		self._reverse = reverse 
		if items is not None:
			self.update(items)

	def __getitem__(self, key):
		return self._items[key]

	def __setitem__(self, key, value):
		self._items[key] = value
		if key not in self._keys:
			self._keys.append(key)
			self._keys.sort(key = self._key_fn, reverse = self._reverse)

	def __delitem__(self, key):
		self._items.pop(key)
		self._keys.remove(key)

	def __len__(self):
		return len(self._keys)

	def __iter__(self):
		for key in self._keys:
			yield key 

	def __repr__(self):
		  return '%s(%s)' % (self.__class__.__name__, self._items)