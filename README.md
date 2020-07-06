
find() is a method to search the document tree, it can return the first matched element. 
Its complete parameter form is: find( name, attrs, recursive, string, **kwargs ). 
The parameter name retrieves the string by tag name, 
the parameter attrs retrieves the string by tag attribute value, 
whether the parameter recursive retrieves all descendants, the default is True, 
and the parameter string is the non-attribute character string in the retrieval tag.

children is a property that traverses down the label. 
There are three traversal forms for tags, which are downlink traversal, uplink traversal and parallel traversal.

- Downstream traversal has the following three attributes:
.children is looping through the son node
.descendants loops through all descendant nodes
.contents is to store all the son nodes in the tag into the list

- The upstream traversal has the following two attributes:
.parent is the parent node label to access the node
.parents is to loop through all ancestor nodes

- The parallel traversal has the following four properties:]
.next_sibling returns the label of the next parallel node
.previous_sibling returns the label of the previous parallel node
.next_siblings is to return the labels of all subsequent parallel nodes
.previous_siblings is to return the labels of all previous parallel nodes

[
<td>901-1000</td>, 
<td class="align-left"><a href="World-University-Rankings/Zagazig-University.html" target="_blank">扎加齐克大学</a></td>, 

<td><a href="World-University-Rankings-2019/Egypt.html" target="_blank" title="查看埃及大学排名"><img src="image/flag/Egypt.png"/></a></td>, 

<td class="hidden-xs">5</td>, <td></td>, 
<td class="hidden-xs need-hidden alumni">0</td>, 
<td class="hidden-xs need-hidden award" style="display:none;">0</td>, 
<td class="hidden-xs need-hidden hici" style="display:none;">0</td>, <td class="hidden-xs need-hidden ns" style="display:none;">1.5</td>, <td class="hidden-xs need-hidden pub" style="display:none;">23.7</td>, <td class="hidden-xs need-hidden pcp" style="display:none;">11.5</td>]