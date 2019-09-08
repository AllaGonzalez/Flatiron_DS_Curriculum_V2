
# Separating Content and Presentation

## Introduction
You now know what HTML is and how to create a properly-formatted HTML document. That said, if you look at the HTML pages thus far, you can't help but notice that they look a little plain. To make them more attractive (and responsive), you can use Cascading Style Sheets or CSS!

## Objectives
You will be able to:
* Identify the separation of content and presentation
* Identify the role of CSS

## Identify the Separation of Content and Presentation

HTML lets you mark-up our content with semantic _structure_. It forms the skeleton of your web page. It would be great to be able to say, "Browser, when you see a `p` tag with `id` of `my-name`, make the first letter be huge!" Or, to get your readers' attention, you might say, "Browser, if you see _any_ tag with a `class` of `warning` surround it with a red box!" HTML authors believe that creating marked-up documents and styling marked-up documents are entirely separate tasks. They see a difference between writing _content_ (the data within the HTML document) and specifying _presentation_, the rules for displaying the rendered elements.

## Identify the Role of CSS

CSS, or "Cascading Style Sheets," tells you how to write rules that define how
browsers will present HTML. Rules in CSS won't look like HTML and they usually
live in a file apart from our HTML file.

CSS handles all of the ways you want to customize your content's look and feel
from margins and colors, to column-based layout!

## Additional Resources

* [CSS Guidelines: The Separation of Concerns](https://cssguidelin.es/#the-separation-of-concerns)
* [CSS Zen Garden](http://www.csszengarden.com/)

## Summary
Web developers separate the content of our HTML pages from their presentation, which they
style with CSS. By keeping the two separate, you not only utilize the best tools
for each job, but you can change code for one without disturbing the code for
the other.
