# 0x01. Caching

<h2>Background Context</h2>

<p>In this project, you learn different caching algorithms.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
	<li><a href="https://intranet.alxswe.com/rltoken/fjhr6EvFeF3mWwsPQXUKdQ" target="_blank" title="Cache replacement policies - FIFO">Cache replacement policies - FIFO</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/-gpAdRQTx1Rb-amaz9JZhQ" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
	<li>What a caching system is</li>
	<li>What FIFO means</li>
	<li>What LIFO means</li>
	<li>What LRU means</li>
	<li>What MRU means</li>
	<li>What LFU means</li>
	<li>What the purpose of a caching system</li>
	<li>What limits a caching system have</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
	<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using&nbsp;<code>python3</code>&nbsp;(version 3.7)</li>
	<li>All your files should end with a new line</li>
	<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/env python3</code></li>
	<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
	<li>Your code should use the&nbsp;<code>pycodestyle</code>&nbsp;style (version 2.5)</li>
	<li>All your files must be executable</li>
	<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
	<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
	<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
	<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code>&nbsp;and&nbsp;<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
	<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h2>More Info</h2>

<h3>Parent class&nbsp;<code>BaseCaching</code></h3>

<p>All your classes must inherit from&nbsp;<code>BaseCaching</code>&nbsp;defined below:</p>

<pre>
<code>$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
</code></pre>

<h2>Tasks</h2>

<h3>0. Basic dictionary</h3>

<p>mandatory</p>

<p>Create a class&nbsp;<code>BasicCache</code>&nbsp;that inherits from&nbsp;<code>BaseCaching</code>&nbsp;and is a caching system:</p>

<ul>
	<li>You must use&nbsp;<code>self.cache_data</code>&nbsp;- dictionary from the parent class&nbsp;<code>BaseCaching</code></li>
	<li>This caching system doesn&rsquo;t have limit</li>
	<li><code>def put(self, key, item):</code>
	<ul>
		<li>Must assign to the dictionary&nbsp;<code>self.cache_data</code>&nbsp;the&nbsp;<code>item</code>&nbsp;value for the key&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;or&nbsp;<code>item</code>&nbsp;is&nbsp;<code>None</code>, this method should not do anything.</li>
	</ul>
	</li>
	<li><code>def get(self, key):</code>
	<ul>
		<li>Must return the value in&nbsp;<code>self.cache_data</code>&nbsp;linked to&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;is&nbsp;<code>None</code>&nbsp;or if the&nbsp;<code>key</code>&nbsp;doesn&rsquo;t exist in&nbsp;<code>self.cache_data</code>, return&nbsp;<code>None</code>.</li>
	</ul>
	</li>
</ul>

<pre>
<code>guillaume@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
</code></pre>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend</code></li>
	<li>Directory:&nbsp;<code>0x01-caching</code></li>
	<li>File:&nbsp;<code>0-basic_cache.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Get a sandbox</p>

<h3>1. FIFO caching</h3>

<p>mandatory</p>

<p>Create a class&nbsp;<code>FIFOCache</code>&nbsp;that inherits from&nbsp;<code>BaseCaching</code>&nbsp;and is a caching system:</p>

<ul>
	<li>You must use&nbsp;<code>self.cache_data</code>&nbsp;- dictionary from the parent class&nbsp;<code>BaseCaching</code></li>
	<li>You can overload&nbsp;<code>def __init__(self):</code>&nbsp;but don&rsquo;t forget to call the parent init:&nbsp;<code>super().__init__()</code></li>
	<li><code>def put(self, key, item):</code>
	<ul>
		<li>Must assign to the dictionary&nbsp;<code>self.cache_data</code>&nbsp;the&nbsp;<code>item</code>&nbsp;value for the key&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;or&nbsp;<code>item</code>&nbsp;is&nbsp;<code>None</code>, this method should not do anything.</li>
		<li>If the number of items in&nbsp;<code>self.cache_data</code>&nbsp;is higher that&nbsp;<code>BaseCaching.MAX_ITEMS</code>:
		<ul>
			<li>you must discard the first item put in cache (FIFO algorithm)</li>
			<li>you must print&nbsp;<code>DISCARD:</code>&nbsp;with the&nbsp;<code>key</code>&nbsp;discarded and following by a new line</li>
		</ul>
		</li>
	</ul>
	</li>
	<li><code>def get(self, key):</code>
	<ul>
		<li>Must return the value in&nbsp;<code>self.cache_data</code>&nbsp;linked to&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;is&nbsp;<code>None</code>&nbsp;or if the&nbsp;<code>key</code>&nbsp;doesn&rsquo;t exist in&nbsp;<code>self.cache_data</code>, return&nbsp;<code>None</code>.</li>
	</ul>
	</li>
</ul>

<pre>
<code>guillaume@ubuntu:~/0x01$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$ 
</code></pre>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend</code></li>
	<li>Directory:&nbsp;<code>0x01-caching</code></li>
	<li>File:&nbsp;<code>1-fifo_cache.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Get a sandbox</p>

<h3>2. LIFO Caching</h3>

<p>mandatory</p>

<p>Create a class&nbsp;<code>LIFOCache</code>&nbsp;that inherits from&nbsp;<code>BaseCaching</code>&nbsp;and is a caching system:</p>

<ul>
	<li>You must use&nbsp;<code>self.cache_data</code>&nbsp;- dictionary from the parent class&nbsp;<code>BaseCaching</code></li>
	<li>You can overload&nbsp;<code>def __init__(self):</code>&nbsp;but don&rsquo;t forget to call the parent init:&nbsp;<code>super().__init__()</code></li>
	<li><code>def put(self, key, item):</code>
	<ul>
		<li>Must assign to the dictionary&nbsp;<code>self.cache_data</code>&nbsp;the&nbsp;<code>item</code>&nbsp;value for the key&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;or&nbsp;<code>item</code>&nbsp;is&nbsp;<code>None</code>, this method should not do anything.</li>
		<li>If the number of items in&nbsp;<code>self.cache_data</code>&nbsp;is higher that&nbsp;<code>BaseCaching.MAX_ITEMS</code>:
		<ul>
			<li>you must discard the last item put in cache (LIFO algorithm)</li>
			<li>you must print&nbsp;<code>DISCARD:</code>&nbsp;with the&nbsp;<code>key</code>&nbsp;discarded and following by a new line</li>
		</ul>
		</li>
	</ul>
	</li>
	<li><code>def get(self, key):</code>
	<ul>
		<li>Must return the value in&nbsp;<code>self.cache_data</code>&nbsp;linked to&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;is&nbsp;<code>None</code>&nbsp;or if the&nbsp;<code>key</code>&nbsp;doesn&rsquo;t exist in&nbsp;<code>self.cache_data</code>, return&nbsp;<code>None</code>.</li>
	</ul>
	</li>
</ul>

<pre>
<code>guillaume@ubuntu:~/0x01$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/0x01$ 
</code></pre>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend</code></li>
	<li>Directory:&nbsp;<code>0x01-caching</code></li>
	<li>File:&nbsp;<code>2-lifo_cache.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Get a sandbox</p>

<h3>3. LRU Caching</h3>

<p>mandatory</p>

<p>Create a class&nbsp;<code>LRUCache</code>&nbsp;that inherits from&nbsp;<code>BaseCaching</code>&nbsp;and is a caching system:</p>

<ul>
	<li>You must use&nbsp;<code>self.cache_data</code>&nbsp;- dictionary from the parent class&nbsp;<code>BaseCaching</code></li>
	<li>You can overload&nbsp;<code>def __init__(self):</code>&nbsp;but don&rsquo;t forget to call the parent init:&nbsp;<code>super().__init__()</code></li>
	<li><code>def put(self, key, item):</code>
	<ul>
		<li>Must assign to the dictionary&nbsp;<code>self.cache_data</code>&nbsp;the&nbsp;<code>item</code>&nbsp;value for the key&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;or&nbsp;<code>item</code>&nbsp;is&nbsp;<code>None</code>, this method should not do anything.</li>
		<li>If the number of items in&nbsp;<code>self.cache_data</code>&nbsp;is higher that&nbsp;<code>BaseCaching.MAX_ITEMS</code>:
		<ul>
			<li>you must discard the least recently used item (LRU algorithm)</li>
			<li>you must print&nbsp;<code>DISCARD:</code>&nbsp;with the&nbsp;<code>key</code>&nbsp;discarded and following by a new line</li>
		</ul>
		</li>
	</ul>
	</li>
	<li><code>def get(self, key):</code>
	<ul>
		<li>Must return the value in&nbsp;<code>self.cache_data</code>&nbsp;linked to&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;is&nbsp;<code>None</code>&nbsp;or if the&nbsp;<code>key</code>&nbsp;doesn&rsquo;t exist in&nbsp;<code>self.cache_data</code>, return&nbsp;<code>None</code>.</li>
	</ul>
	</li>
</ul>

<pre>
<code>guillaume@ubuntu:~/0x01$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/0x01$ 
</code></pre>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend</code></li>
	<li>Directory:&nbsp;<code>0x01-caching</code></li>
	<li>File:&nbsp;<code>3-lru_cache.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Get a sandbox</p>

<h3>4. MRU Caching</h3>

<p>mandatory</p>

<p>Create a class&nbsp;<code>MRUCache</code>&nbsp;that inherits from&nbsp;<code>BaseCaching</code>&nbsp;and is a caching system:</p>

<ul>
	<li>You must use&nbsp;<code>self.cache_data</code>&nbsp;- dictionary from the parent class&nbsp;<code>BaseCaching</code></li>
	<li>You can overload&nbsp;<code>def __init__(self):</code>&nbsp;but don&rsquo;t forget to call the parent init:&nbsp;<code>super().__init__()</code></li>
	<li><code>def put(self, key, item):</code>
	<ul>
		<li>Must assign to the dictionary&nbsp;<code>self.cache_data</code>&nbsp;the&nbsp;<code>item</code>&nbsp;value for the key&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;or&nbsp;<code>item</code>&nbsp;is&nbsp;<code>None</code>, this method should not do anything.</li>
		<li>If the number of items in&nbsp;<code>self.cache_data</code>&nbsp;is higher that&nbsp;<code>BaseCaching.MAX_ITEMS</code>:
		<ul>
			<li>you must discard the most recently used item (MRU algorithm)</li>
			<li>you must print&nbsp;<code>DISCARD:</code>&nbsp;with the&nbsp;<code>key</code>&nbsp;discarded and following by a new line</li>
		</ul>
		</li>
	</ul>
	</li>
	<li><code>def get(self, key):</code>
	<ul>
		<li>Must return the value in&nbsp;<code>self.cache_data</code>&nbsp;linked to&nbsp;<code>key</code>.</li>
		<li>If&nbsp;<code>key</code>&nbsp;is&nbsp;<code>None</code>&nbsp;or if the&nbsp;<code>key</code>&nbsp;doesn&rsquo;t exist in&nbsp;<code>self.cache_data</code>, return&nbsp;<code>None</code>.</li>
	</ul>
	</li>
</ul>

<pre>
<code>guillaume@ubuntu:~/0x01$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/0x01$ 
</code></pre>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend</code></li>
	<li>Directory:&nbsp;<code>0x01-caching</code></li>
	<li>File:&nbsp;<code>4-mru_cache.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Get a sandbox</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Copyright &copy; 2024 ALX, All rights reserved.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
