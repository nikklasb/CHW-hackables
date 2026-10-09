### Webpage navigation and URLs
A webpage URL is structured as follows:  
http://10.0.0.4:5001/page1?param1=value1  
  
It can be broken up as follows:  
http://  &nbsp;&nbsp;(1) 10.0.0.4  &nbsp;&nbsp;(2) :5001  &nbsp;&nbsp;(3) /page  &nbsp;&nbsp;(4) ?param1=value1  

1. (1) is the computer hosting the website, in this case it has IP address 10.0.0.4.
2. (2) is the port, specifying which website on the computer is being accessed.
3. (3) is the path. It tells you the part of the website you are on (after the /). You can type paths into the browser manually to access a site's pages.
4. (4) is the url parameters. These pairs of keys and values (key=value) can change behavior of pages. They can be modified by changing the URL!

### robots.txt

Many web pages have a special path at /robots.txt. It is located at url + /robots.txt:  
For the website Amazon, https://www.amazon.com  -->  https://www.amazon.com/robots.txt  
Keep in mind everything before the third / (counting ```http://``` as the first two) is the base url.

It specifies what pages web crawling robots can access, but it also gives you information about what pages exist on a site!

### HTML

HTML is the programming language that defines the structure of a website. The core part of HTML is tags.Examples include &lt;html&gt;, &lt;body&gt;, &lt;p&gt;. Tags also have closing tags, which are like tags, but they start with &lt;/ instead of &lt;: &lt;/html&gt;, &lt;/body&gt;, &lt;/p&gt;. The opening tag begin an html element, and the closing tag ends the element.

```html
<body attribute1 attribute2>
    <h1>...</h1>
    <p>...</p>
</body>
```

In the above example, the &lt;body&gt; element contains &lt;h1&gt; and &lt;p&gt; elements. HTML is hierarchical, so elements contain other elements. The body also contains two attributes, affecting how the body element looks. Some relevant tags for this exercise are &lt;form&gt; for submitting things like passwords, &lt;a&gt; for links, and &lt;p&gt; is for paragraphs.  

To view HTML code, you can enter cntrl + shift + i. This will open a side view that contains the HTML of the website. You can do two important things here:
1. You can click on the small black triangles left of elements to view what elements are contained within them.
2. You can edit the HTML code. *For example, you can click on attributes and remove them.* In fact, any aspect of the HTML can be changed.