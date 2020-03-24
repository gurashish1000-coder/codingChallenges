<!DOCTYPE html>
<!-- saved from url=(0057)file:///C:/Users/guras/Downloads/Coding%20Challenges.html -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width initial-scale=1">
<title></title><link href="file://night/mermaid.dark.css" rel="stylesheet" type="text/css"><link href="file://night/codeblock.dark.css" rel="stylesheet" type="text/css"><link href="file://night/sourcemode.dark.css" rel="stylesheet" type="text/css"><style type="text/css">html {overflow-x: initial !important;}:root { --bg-color:#ffffff; --text-color:#333333; --select-text-bg-color:#B5D6FC; --select-text-font-color:auto; --monospace:"Lucida Console",Consolas,"Courier",monospace; }
html { font-size: 14px; background-color: var(--bg-color); color: var(--text-color); font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased; }
body { margin: 0px; padding: 0px; height: auto; bottom: 0px; top: 0px; left: 0px; right: 0px; font-size: 1rem; line-height: 1.42857; overflow-x: hidden; background: inherit; tab-size: 4; }
iframe { margin: auto; }
a.url { word-break: break-all; }
a:active, a:hover { outline: 0px; }
.in-text-selection, ::selection { text-shadow: none; background: var(--select-text-bg-color); color: var(--select-text-font-color); }
#write { margin: 0px auto; height: auto; width: inherit; word-break: normal; overflow-wrap: break-word; position: relative; white-space: normal; overflow-x: visible; padding-top: 40px; }
#write.first-line-indent p { text-indent: 2em; }
#write.first-line-indent li p, #write.first-line-indent p * { text-indent: 0px; }
#write.first-line-indent li { margin-left: 2em; }
.for-image #write { padding-left: 8px; padding-right: 8px; }
body.typora-export { padding-left: 30px; padding-right: 30px; }
.typora-export .footnote-line, .typora-export li, .typora-export p { white-space: pre-wrap; }
@media screen and (max-width: 500px) {
  body.typora-export { padding-left: 0px; padding-right: 0px; }
  #write { padding-left: 20px; padding-right: 20px; }
  .CodeMirror-sizer { margin-left: 0px !important; }
  .CodeMirror-gutters { display: none !important; }
}
#write li > figure:last-child { margin-bottom: 0.5rem; }
#write ol, #write ul { position: relative; }
img { max-width: 100%; vertical-align: middle; }
button, input, select, textarea { color: inherit; font: inherit; }
input[type="checkbox"], input[type="radio"] { line-height: normal; padding: 0px; }
*, ::after, ::before { box-sizing: border-box; }
#write h1, #write h2, #write h3, #write h4, #write h5, #write h6, #write p, #write pre { width: inherit; }
#write h1, #write h2, #write h3, #write h4, #write h5, #write h6, #write p { position: relative; }
p { line-height: inherit; }
h1, h2, h3, h4, h5, h6 { break-after: avoid-page; break-inside: avoid; orphans: 2; }
p { orphans: 4; }
h1 { font-size: 2rem; }
h2 { font-size: 1.8rem; }
h3 { font-size: 1.6rem; }
h4 { font-size: 1.4rem; }
h5 { font-size: 1.2rem; }
h6 { font-size: 1rem; }
.md-math-block, .md-rawblock, h1, h2, h3, h4, h5, h6, p { margin-top: 1rem; margin-bottom: 1rem; }
.hidden { display: none; }
.md-blockmeta { color: rgb(204, 204, 204); font-weight: 700; font-style: italic; }
a { cursor: pointer; }
sup.md-footnote { padding: 2px 4px; background-color: rgba(238, 238, 238, 0.7); color: rgb(85, 85, 85); border-radius: 4px; cursor: pointer; }
sup.md-footnote a, sup.md-footnote a:hover { color: inherit; text-transform: inherit; text-decoration: inherit; }
#write input[type="checkbox"] { cursor: pointer; width: inherit; height: inherit; }
figure { overflow-x: auto; margin: 1.2em 0px; max-width: calc(100% + 16px); padding: 0px; }
figure > table { margin: 0px !important; }
tr { break-inside: avoid; break-after: auto; }
thead { display: table-header-group; }
table { border-collapse: collapse; border-spacing: 0px; width: 100%; overflow: auto; break-inside: auto; text-align: left; }
table.md-table td { min-width: 32px; }
.CodeMirror-gutters { border-right: 0px; background-color: inherit; }
.CodeMirror-linenumber { user-select: none; }
.CodeMirror { text-align: left; }
.CodeMirror-placeholder { opacity: 0.3; }
.CodeMirror pre { padding: 0px 4px; }
.CodeMirror-lines { padding: 0px; }
div.hr:focus { cursor: none; }
#write pre { white-space: pre-wrap; }
#write.fences-no-line-wrapping pre { white-space: pre; }
#write pre.ty-contain-cm { white-space: normal; }
.CodeMirror-gutters { margin-right: 4px; }
.md-fences { font-size: 0.9rem; display: block; break-inside: avoid; text-align: left; overflow: visible; white-space: pre; background: inherit; position: relative !important; }
.md-diagram-panel { width: 100%; margin-top: 10px; text-align: center; padding-top: 0px; padding-bottom: 8px; overflow-x: auto; }
#write .md-fences.mock-cm { white-space: pre-wrap; }
.md-fences.md-fences-with-lineno { padding-left: 0px; }
#write.fences-no-line-wrapping .md-fences.mock-cm { white-space: pre; overflow-x: auto; }
.md-fences.mock-cm.md-fences-with-lineno { padding-left: 8px; }
.CodeMirror-line, twitterwidget { break-inside: avoid; }
.footnotes { opacity: 0.8; font-size: 0.9rem; margin-top: 1em; margin-bottom: 1em; }
.footnotes + .footnotes { margin-top: 0px; }
.md-reset { margin: 0px; padding: 0px; border: 0px; outline: 0px; vertical-align: top; background: 0px 0px; text-decoration: none; text-shadow: none; float: none; position: static; width: auto; height: auto; white-space: nowrap; cursor: inherit; -webkit-tap-highlight-color: transparent; line-height: normal; font-weight: 400; text-align: left; box-sizing: content-box; direction: ltr; }
li div { padding-top: 0px; }
blockquote { margin: 1rem 0px; }
li .mathjax-block, li p { margin: 0.5rem 0px; }
li { margin: 0px; position: relative; }
blockquote > :last-child { margin-bottom: 0px; }
blockquote > :first-child, li > :first-child { margin-top: 0px; }
.footnotes-area { color: rgb(136, 136, 136); margin-top: 0.714rem; padding-bottom: 0.143rem; white-space: normal; }
#write .footnote-line { white-space: pre-wrap; }
@media print {
  body, html { border: 1px solid transparent; height: 99%; break-after: avoid; break-before: avoid; }
  #write { margin-top: 0px; padding-top: 0px; border-color: transparent !important; }
  .typora-export * { -webkit-print-color-adjust: exact; }
  html.blink-to-pdf { font-size: 13px; }
  .typora-export #write { padding-left: 32px; padding-right: 32px; padding-bottom: 0px; break-after: avoid; }
  .typora-export #write::after { height: 0px; }
}
.footnote-line { margin-top: 0.714em; font-size: 0.7em; }
a img, img a { cursor: pointer; }
pre.md-meta-block { font-size: 0.8rem; min-height: 0.8rem; white-space: pre-wrap; background: rgb(204, 204, 204); display: block; overflow-x: hidden; }
p > .md-image:only-child:not(.md-img-error) img, p > img:only-child { display: block; margin: auto; }
p > .md-image:only-child { display: inline-block; width: 100%; }
#write .MathJax_Display { margin: 0.8em 0px 0px; }
.md-math-block { width: 100%; }
.md-math-block:not(:empty)::after { display: none; }
[contenteditable="true"]:active, [contenteditable="true"]:focus, [contenteditable="false"]:active, [contenteditable="false"]:focus { outline: 0px; box-shadow: none; }
.md-task-list-item { position: relative; list-style-type: none; }
.task-list-item.md-task-list-item { padding-left: 0px; }
.md-task-list-item > input { position: absolute; top: 0px; left: 0px; margin-left: -1.2em; margin-top: calc(1em - 10px); border: none; }
.math { font-size: 1rem; }
.md-toc { min-height: 3.58rem; position: relative; font-size: 0.9rem; border-radius: 10px; }
.md-toc-content { position: relative; margin-left: 0px; }
.md-toc-content::after, .md-toc::after { display: none; }
.md-toc-item { display: block; color: rgb(65, 131, 196); }
.md-toc-item a { text-decoration: none; }
.md-toc-inner:hover { text-decoration: underline; }
.md-toc-inner { display: inline-block; cursor: pointer; }
.md-toc-h1 .md-toc-inner { margin-left: 0px; font-weight: 700; }
.md-toc-h2 .md-toc-inner { margin-left: 2em; }
.md-toc-h3 .md-toc-inner { margin-left: 4em; }
.md-toc-h4 .md-toc-inner { margin-left: 6em; }
.md-toc-h5 .md-toc-inner { margin-left: 8em; }
.md-toc-h6 .md-toc-inner { margin-left: 10em; }
@media screen and (max-width: 48em) {
  .md-toc-h3 .md-toc-inner { margin-left: 3.5em; }
  .md-toc-h4 .md-toc-inner { margin-left: 5em; }
  .md-toc-h5 .md-toc-inner { margin-left: 6.5em; }
  .md-toc-h6 .md-toc-inner { margin-left: 8em; }
}
a.md-toc-inner { font-size: inherit; font-style: inherit; font-weight: inherit; line-height: inherit; }
.footnote-line a:not(.reversefootnote) { color: inherit; }
.md-attr { display: none; }
.md-fn-count::after { content: "."; }
code, pre, samp, tt { font-family: var(--monospace); }
kbd { margin: 0px 0.1em; padding: 0.1em 0.6em; font-size: 0.8em; color: rgb(36, 39, 41); background: rgb(255, 255, 255); border: 1px solid rgb(173, 179, 185); border-radius: 3px; box-shadow: rgba(12, 13, 14, 0.2) 0px 1px 0px, rgb(255, 255, 255) 0px 0px 0px 2px inset; white-space: nowrap; vertical-align: middle; }
.md-comment { color: rgb(162, 127, 3); opacity: 0.8; font-family: var(--monospace); }
code { text-align: left; vertical-align: initial; }
a.md-print-anchor { white-space: pre !important; border-width: initial !important; border-style: none !important; border-color: initial !important; display: inline-block !important; position: absolute !important; width: 1px !important; right: 0px !important; outline: 0px !important; background: 0px 0px !important; text-decoration: initial !important; text-shadow: initial !important; }
.md-inline-math .MathJax_SVG .noError { display: none !important; }
.html-for-mac .inline-math-svg .MathJax_SVG { vertical-align: 0.2px; }
.md-math-block .MathJax_SVG_Display { text-align: center; margin: 0px; position: relative; text-indent: 0px; max-width: none; max-height: none; min-height: 0px; min-width: 100%; width: auto; overflow-y: hidden; display: block !important; }
.MathJax_SVG_Display, .md-inline-math .MathJax_SVG_Display { width: auto; margin: inherit; display: inline-block !important; }
.MathJax_SVG .MJX-monospace { font-family: var(--monospace); }
.MathJax_SVG .MJX-sans-serif { font-family: sans-serif; }
.MathJax_SVG { display: inline; font-style: normal; font-weight: 400; line-height: normal; zoom: 90%; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; }
.MathJax_SVG * { transition: none 0s ease 0s; }
.MathJax_SVG_Display svg { vertical-align: middle !important; margin-bottom: 0px !important; margin-top: 0px !important; }
.os-windows.monocolor-emoji .md-emoji { font-family: "Segoe UI Symbol", sans-serif; }
.md-diagram-panel > svg { max-width: 100%; }
[lang="flow"] svg, [lang="mermaid"] svg { max-width: 100%; height: auto; }
[lang="mermaid"] .node text { font-size: 1rem; }
table tr th { border-bottom: 0px; }
video { max-width: 100%; display: block; margin: 0px auto; }
iframe { max-width: 100%; width: 100%; border: none; }
.highlight td, .highlight tr { border: 0px; }
svg[id^="mermaidChart"] { line-height: 1em; }
mark { background: rgb(255, 255, 0); color: rgb(0, 0, 0); }
.md-html-inline .md-plain, .md-html-inline strong, mark .md-inline-math, mark strong { color: inherit; }
mark .md-meta { color: rgb(0, 0, 0); opacity: 0.3 !important; }


.CodeMirror { height: auto; }
.CodeMirror.cm-s-inner { background: inherit; }
.CodeMirror-scroll { overflow: auto hidden; z-index: 3; }
.CodeMirror-gutter-filler, .CodeMirror-scrollbar-filler { background-color: rgb(255, 255, 255); }
.CodeMirror-gutters { border-right: 1px solid rgb(221, 221, 221); background: inherit; white-space: nowrap; }
.CodeMirror-linenumber { padding: 0px 3px 0px 5px; text-align: right; color: rgb(153, 153, 153); }
.cm-s-inner .cm-keyword { color: rgb(119, 0, 136); }
.cm-s-inner .cm-atom, .cm-s-inner.cm-atom { color: rgb(34, 17, 153); }
.cm-s-inner .cm-number { color: rgb(17, 102, 68); }
.cm-s-inner .cm-def { color: rgb(0, 0, 255); }
.cm-s-inner .cm-variable { color: rgb(0, 0, 0); }
.cm-s-inner .cm-variable-2 { color: rgb(0, 85, 170); }
.cm-s-inner .cm-variable-3 { color: rgb(0, 136, 85); }
.cm-s-inner .cm-string { color: rgb(170, 17, 17); }
.cm-s-inner .cm-property { color: rgb(0, 0, 0); }
.cm-s-inner .cm-operator { color: rgb(152, 26, 26); }
.cm-s-inner .cm-comment, .cm-s-inner.cm-comment { color: rgb(170, 85, 0); }
.cm-s-inner .cm-string-2 { color: rgb(255, 85, 0); }
.cm-s-inner .cm-meta { color: rgb(85, 85, 85); }
.cm-s-inner .cm-qualifier { color: rgb(85, 85, 85); }
.cm-s-inner .cm-builtin { color: rgb(51, 0, 170); }
.cm-s-inner .cm-bracket { color: rgb(153, 153, 119); }
.cm-s-inner .cm-tag { color: rgb(17, 119, 0); }
.cm-s-inner .cm-attribute { color: rgb(0, 0, 204); }
.cm-s-inner .cm-header, .cm-s-inner.cm-header { color: rgb(0, 0, 255); }
.cm-s-inner .cm-quote, .cm-s-inner.cm-quote { color: rgb(0, 153, 0); }
.cm-s-inner .cm-hr, .cm-s-inner.cm-hr { color: rgb(153, 153, 153); }
.cm-s-inner .cm-link, .cm-s-inner.cm-link { color: rgb(0, 0, 204); }
.cm-negative { color: rgb(221, 68, 68); }
.cm-positive { color: rgb(34, 153, 34); }
.cm-header, .cm-strong { font-weight: 700; }
.cm-del { text-decoration: line-through; }
.cm-em { font-style: italic; }
.cm-link { text-decoration: underline; }
.cm-error { color: red; }
.cm-invalidchar { color: red; }
.cm-constant { color: rgb(38, 139, 210); }
.cm-defined { color: rgb(181, 137, 0); }
div.CodeMirror span.CodeMirror-matchingbracket { color: rgb(0, 255, 0); }
div.CodeMirror span.CodeMirror-nonmatchingbracket { color: rgb(255, 34, 34); }
.cm-s-inner .CodeMirror-activeline-background { background: inherit; }
.CodeMirror { position: relative; overflow: hidden; }
.CodeMirror-scroll { height: 100%; outline: 0px; position: relative; box-sizing: content-box; background: inherit; }
.CodeMirror-sizer { position: relative; }
.CodeMirror-gutter-filler, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-vscrollbar { position: absolute; z-index: 6; display: none; }
.CodeMirror-vscrollbar { right: 0px; top: 0px; overflow: hidden; }
.CodeMirror-hscrollbar { bottom: 0px; left: 0px; overflow: hidden; }
.CodeMirror-scrollbar-filler { right: 0px; bottom: 0px; }
.CodeMirror-gutter-filler { left: 0px; bottom: 0px; }
.CodeMirror-gutters { position: absolute; left: 0px; top: 0px; padding-bottom: 30px; z-index: 3; }
.CodeMirror-gutter { white-space: normal; height: 100%; box-sizing: content-box; padding-bottom: 30px; margin-bottom: -32px; display: inline-block; }
.CodeMirror-gutter-wrapper { position: absolute; z-index: 4; background: 0px 0px !important; border: none !important; }
.CodeMirror-gutter-background { position: absolute; top: 0px; bottom: 0px; z-index: 4; }
.CodeMirror-gutter-elt { position: absolute; cursor: default; z-index: 4; }
.CodeMirror-lines { cursor: text; }
.CodeMirror pre { border-radius: 0px; border-width: 0px; background: 0px 0px; font-family: inherit; font-size: inherit; margin: 0px; white-space: pre; overflow-wrap: normal; color: inherit; z-index: 2; position: relative; overflow: visible; }
.CodeMirror-wrap pre { overflow-wrap: break-word; white-space: pre-wrap; word-break: normal; }
.CodeMirror-code pre { border-right: 30px solid transparent; width: fit-content; }
.CodeMirror-wrap .CodeMirror-code pre { border-right: none; width: auto; }
.CodeMirror-linebackground { position: absolute; left: 0px; right: 0px; top: 0px; bottom: 0px; z-index: 0; }
.CodeMirror-linewidget { position: relative; z-index: 2; overflow: auto; }
.CodeMirror-wrap .CodeMirror-scroll { overflow-x: hidden; }
.CodeMirror-measure { position: absolute; width: 100%; height: 0px; overflow: hidden; visibility: hidden; }
.CodeMirror-measure pre { position: static; }
.CodeMirror div.CodeMirror-cursor { position: absolute; visibility: hidden; border-right: none; width: 0px; }
.CodeMirror div.CodeMirror-cursor { visibility: hidden; }
.CodeMirror-focused div.CodeMirror-cursor { visibility: inherit; }
.cm-searching { background: rgba(255, 255, 0, 0.4); }
@media print {
  .CodeMirror div.CodeMirror-cursor { visibility: hidden; }
}


/* Flowchart variables */
/* Sequence Diagram variables */
/* Gantt chart variables */
/* state colors */
.label {
  
  color: #333; }

.label text {
  fill: #333; }

.node rect,
.node circle,
.node ellipse,
.node polygon {
  fill: #BDD5EA;
  stroke: #9370DB;
  stroke-width: 1px; }

.node .label {
  text-align: center; }

.node.clickable {
  cursor: pointer; }

.arrowheadPath {
  fill: lightgrey; }

.edgePath .path {
  stroke: lightgrey;
  stroke-width: 1.5px; }

.edgeLabel {
  background-color: #e8e8e8;
  text-align: center; }

.cluster rect {
  fill: #6D6D65;
  stroke: rgba(255, 255, 255, 0.25);
  stroke-width: 1px; }

.cluster text {
  fill: #F9FFFE; }

div.mermaidTooltip {
  position: absolute;
  text-align: center;
  max-width: 200px;
  padding: 2px;
  
  font-size: 12px;
  background: #6D6D65;
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 2px;
  pointer-events: none;
  z-index: 100; }

.actor {
  stroke: #81B1DB;
  fill: #BDD5EA; }

text.actor {
  fill: black;
  stroke: none; }

.actor-line {
  stroke: lightgrey; }

.messageLine0 {
  stroke-width: 1.5;
  stroke-dasharray: '2 2';
  stroke: lightgrey; }

.messageLine1 {
  stroke-width: 1.5;
  stroke-dasharray: '2 2';
  stroke: lightgrey; }

#arrowhead {
  fill: lightgrey; }

.sequenceNumber {
  fill: white; }

#sequencenumber {
  fill: lightgrey; }

#crosshead path {
  fill: lightgrey !important;
  stroke: lightgrey !important; }

.messageText {
  fill: lightgrey;
  stroke: none; }

.labelBox {
  stroke: #81B1DB;
  fill: #BDD5EA; }

.labelText {
  fill: #323D47;
  stroke: none; }

.loopText {
  fill: lightgrey;
  stroke: none; }

.loopLine {
  stroke-width: 2;
  stroke-dasharray: '2 2';
  stroke: #81B1DB; }

.note {
  stroke: rgba(255, 255, 255, 0.25);
  fill: #fff5ad; }

.noteText {
  fill: black;
  stroke: none;
  
  font-size: 14px; }

.activation0 {
  fill: #f4f4f4;
  stroke: #666; }

.activation1 {
  fill: #f4f4f4;
  stroke: #666; }

.activation2 {
  fill: #f4f4f4;
  stroke: #666; }

/** Section styling */
.section {
  stroke: none;
  opacity: 0.2; }

.section0 {
  fill: rgba(255, 255, 255, 0.3); }

.section2 {
  fill: #EAE8B9; }

.section1,
.section3 {
  fill: white;
  opacity: 0.2; }

.sectionTitle0 {
  fill: #F9FFFE; }

.sectionTitle1 {
  fill: #F9FFFE; }

.sectionTitle2 {
  fill: #F9FFFE; }

.sectionTitle3 {
  fill: #F9FFFE; }

.sectionTitle {
  text-anchor: start;
  font-size: 11px;
  text-height: 14px;
   }

/* Grid and axis */
.grid .tick {
  stroke: lightgrey;
  opacity: 0.3;
  shape-rendering: crispEdges; }

.grid path {
  stroke-width: 0; }

/* Today line */
.today {
  fill: none;
  stroke: #DB5757;
  stroke-width: 2px; }

/* Task styling */
/* Default task */
.task {
  stroke-width: 2; }

.taskText {
  text-anchor: middle;
   }

.taskText:not([font-size]) {
  font-size: 11px; }

.taskTextOutsideRight {
  fill: #323D47;
  text-anchor: start;
  font-size: 11px;
   }

.taskTextOutsideLeft {
  fill: #323D47;
  text-anchor: end;
  font-size: 11px; }

/* Special case clickable */
.task.clickable {
  cursor: pointer; }

.taskText.clickable {
  cursor: pointer;
  fill: #003163 !important;
  font-weight: bold; }

.taskTextOutsideLeft.clickable {
  cursor: pointer;
  fill: #003163 !important;
  font-weight: bold; }

.taskTextOutsideRight.clickable {
  cursor: pointer;
  fill: #003163 !important;
  font-weight: bold; }

/* Specific task settings for the sections*/
.taskText0,
.taskText1,
.taskText2,
.taskText3 {
  fill: #323D47; }

.task0,
.task1,
.task2,
.task3 {
  fill: #BDD5EA;
  stroke: rgba(255, 255, 255, 0.5); }

.taskTextOutside0,
.taskTextOutside2 {
  fill: lightgrey; }

.taskTextOutside1,
.taskTextOutside3 {
  fill: lightgrey; }

/* Active task */
.active0,
.active1,
.active2,
.active3 {
  fill: #81B1DB;
  stroke: rgba(255, 255, 255, 0.5); }

.activeText0,
.activeText1,
.activeText2,
.activeText3 {
  fill: #323D47 !important; }

/* Completed task */
.done0,
.done1,
.done2,
.done3 {
  stroke: grey;
  fill: lightgrey;
  stroke-width: 2; }

.doneText0,
.doneText1,
.doneText2,
.doneText3 {
  fill: #323D47 !important; }

/* Tasks on the critical line */
.crit0,
.crit1,
.crit2,
.crit3 {
  stroke: #E83737;
  fill: #E83737;
  stroke-width: 2; }

.activeCrit0,
.activeCrit1,
.activeCrit2,
.activeCrit3 {
  stroke: #E83737;
  fill: #81B1DB;
  stroke-width: 2; }

.doneCrit0,
.doneCrit1,
.doneCrit2,
.doneCrit3 {
  stroke: #E83737;
  fill: lightgrey;
  stroke-width: 2;
  cursor: pointer;
  shape-rendering: crispEdges; }

.milestone {
  transform: rotate(45deg) scale(0.8, 0.8); }

.milestoneText {
  font-style: italic; }

.doneCritText0,
.doneCritText1,
.doneCritText2,
.doneCritText3 {
  fill: #323D47 !important; }

.activeCritText0,
.activeCritText1,
.activeCritText2,
.activeCritText3 {
  fill: #323D47 !important; }

.titleText {
  text-anchor: middle;
  font-size: 18px;
  fill: #323D47;
   }

g.classGroup text {
  fill: #9370DB;
  stroke: none;
  
  font-size: 10px; }
  g.classGroup text .title {
    font-weight: bolder; }

g.classGroup rect {
  fill: #BDD5EA;
  stroke: #9370DB; }

g.classGroup line {
  stroke: #9370DB;
  stroke-width: 1; }

.classLabel .box {
  stroke: none;
  stroke-width: 0;
  fill: #BDD5EA;
  opacity: 0.5; }

.classLabel .label {
  fill: #9370DB;
  font-size: 10px; }

.relation {
  stroke: #9370DB;
  stroke-width: 1;
  fill: none; }

#compositionStart {
  fill: #9370DB;
  stroke: #9370DB;
  stroke-width: 1; }

#compositionEnd {
  fill: #9370DB;
  stroke: #9370DB;
  stroke-width: 1; }

#aggregationStart {
  fill: #BDD5EA;
  stroke: #9370DB;
  stroke-width: 1; }

#aggregationEnd {
  fill: #BDD5EA;
  stroke: #9370DB;
  stroke-width: 1; }

#dependencyStart {
  fill: #9370DB;
  stroke: #9370DB;
  stroke-width: 1; }

#dependencyEnd {
  fill: #9370DB;
  stroke: #9370DB;
  stroke-width: 1; }

#extensionStart {
  fill: #9370DB;
  stroke: #9370DB;
  stroke-width: 1; }

#extensionEnd {
  fill: #9370DB;
  stroke: #9370DB;
  stroke-width: 1; }

.commit-id,
.commit-msg,
.branch-label {
  fill: lightgrey;
  color: lightgrey;
   }

.pieTitleText {
  text-anchor: middle;
  font-size: 25px;
  fill: #eee;
}

.slice {
   }

g.stateGroup text {
  fill: #eee;
  stroke: none;
  font-size: 10px;
   }

g.stateGroup circle {
  fill: white !important;
  stroke: white !important;
}

g.stateGroup .state-title {
  font-weight: bolder;
  fill: black; }

g.stateGroup rect {
  fill: #ececff;
  stroke: #9370DB; }

g.stateGroup line {
  stroke: #9370DB;
  stroke-width: 1; }

.transition {
  stroke: #9370DB;
  stroke-width: 1;
  fill: none; }

.stateGroup .composit {
  fill: #555;
  border-bottom: 1px; }

.state-note {
  stroke: rgba(255, 255, 255, 0.25);
  fill: #fff5ad; }
  .state-note text {
    fill: black;
    stroke: none;
    font-size: 10px; }

.stateLabel .box {
  stroke: none;
  stroke-width: 0;
  fill: #BDD5EA;
  opacity: 0.5; }

.stateLabel text {
  fill: black;
  font-size: 10px;
  font-weight: bold;
   }

;
/* CSS Document */

/** code highlight */

.cm-s-inner .cm-variable,
.cm-s-inner .cm-operator,
.cm-s-inner .cm-property {
    color: #b8bfc6;
}

.cm-s-inner .cm-keyword {
    color: #C88FD0;
}

.cm-s-inner .cm-tag {
    color: #7DF46A;
}

.cm-s-inner .cm-attribute {
    color: #7575E4;
}

.CodeMirror div.CodeMirror-cursor {
    border-left: 1px solid #b8bfc6;
    z-index: 3;
}

.cm-s-inner .cm-string {
    color: #D26B6B;
}

.cm-s-inner .cm-comment,
.cm-s-inner.cm-comment {
    color: #DA924A;
}

.cm-s-inner .cm-header,
.cm-s-inner .cm-def,
.cm-s-inner.cm-header,
.cm-s-inner.cm-def {
    color: #8d8df0;
}

.cm-s-inner .cm-quote,
.cm-s-inner.cm-quote {
    color: #57ac57;
}

.cm-s-inner .cm-hr {
    color: #d8d5d5;
}

.cm-s-inner .cm-link {
    color: #d3d3ef;
}

.cm-s-inner .cm-negative {
    color: #d95050;
}

.cm-s-inner .cm-positive {
    color: #50e650;
}

.cm-s-inner .cm-string-2 {
    color: #f50;
}

.cm-s-inner .cm-meta,
.cm-s-inner .cm-qualifier {
    color: #b7b3b3;
}

.cm-s-inner .cm-builtin {
    color: #f3b3f8;
}

.cm-s-inner .cm-bracket {
    color: #997;
}

.cm-s-inner .cm-atom,
.cm-s-inner.cm-atom {
    color: #84B6CB;
}

.cm-s-inner .cm-number {
    color: #64AB8F;
}

.cm-s-inner .cm-variable {
    color: #b8bfc6;
}

.cm-s-inner .cm-variable-2 {
    color: #9FBAD5;
}

.cm-s-inner .cm-variable-3 {
    color: #1cc685;
}

.CodeMirror-selectedtext,
.CodeMirror-selected {
    background: #4a89dc;
    color: #fff !important;
    text-shadow: none;
}

.CodeMirror-gutters {
    border-right: none;
}
;
/* CSS Document */

/** markdown source **/
.cm-s-typora-default .cm-header, 
.cm-s-typora-default .cm-property
{
    color: #cebcca;
}

.CodeMirror.cm-s-typora-default div.CodeMirror-cursor{
    border-left: 3px solid #b8bfc6;
}

.cm-s-typora-default .cm-comment {
    color: #9FB1FF;
}

.cm-s-typora-default .cm-string {
    color: #A7A7D9
}

.cm-s-typora-default .cm-atom, .cm-s-typora-default .cm-number {
    color: #848695;
    font-style: italic;
}

.cm-s-typora-default .cm-link {
    color: #95B94B;
}

.cm-s-typora-default .CodeMirror-activeline-background {
    background: rgba(51, 51, 51, 0.72);
}

.cm-s-typora-default .cm-comment, .cm-s-typora-default .cm-code {
	color: #8aa1e1;
}@import "";
@import "";
@import "";

:root {
    --bg-color:  #363B40;
    --side-bar-bg-color: #2E3033;
    --text-color: #b8bfc6;

    --select-text-bg-color:#4a89dc;

    --item-hover-bg-color: #0a0d16;
    --control-text-color: #b7b7b7;
    --control-text-hover-color: #eee;
    --window-border: 1px solid #555;

    --active-file-bg-color: rgb(34, 34, 34);
    --active-file-border-color: #8d8df0;

    --primary-color: #a3d5fe;

    --active-file-text-color: white;
    --item-hover-bg-color: #70717d;
    --item-hover-text-color: white;
    --primary-color: #6dc1e7;

    --rawblock-edit-panel-bd: #333;

    --search-select-bg-color: #428bca;
}

html {
    font-size: 16px;
}

html,
body {
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
    background: #363B40;
    background: var(--bg-color);
    fill: currentColor;
    line-height: 1.625rem;
}

#write {
    max-width: 914px;
}

html,
body,
button,
input,
select,
textarea,
div.code-tooltip-content {
    color: #b8bfc6;
    border-color: transparent;
}

div.code-tooltip,
.md-hover-tip .md-arrow:after {
    background: #333;
}

.popover.bottom > .arrow:after {
    border-bottom-color: #333;
}

html,
body,
button,
input,
select,
textarea {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}

hr {
    height: 2px;
    border: 0;
    margin: 24px 0 !important;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-family: "Lucida Grande", "Corbel", sans-serif;
    font-weight: normal;
    clear: both;
    -ms-word-wrap: break-word;
    word-wrap: break-word;
    margin: 0;
    padding: 0;
    color: #DEDEDE
}

h1 {
    font-size: 2.5rem;
    /* 36px */
    line-height: 2.75rem;
    /* 40px */
    margin-bottom: 1.5rem;
    /* 24px */
    letter-spacing: -1.5px;
}

h2 {
    font-size: 1.63rem;
    /* 24px */
    line-height: 1.875rem;
    /* 30px */
    margin-bottom: 1.5rem;
    /* 24px */
    letter-spacing: -1px;
    font-weight: bold;
}

h3 {
    font-size: 1.17rem;
    /* 18px */
    line-height: 1.5rem;
    /* 24px */
    margin-bottom: 1.5rem;
    /* 24px */
    letter-spacing: -1px;
    font-weight: bold;
}

h4 {
    font-size: 1.12rem;
    /* 16px */
    line-height: 1.375rem;
    /* 22px */
    margin-bottom: 1.5rem;
    /* 24px */
    color: white;
}

h5 {
    font-size: 0.97rem;
    /* 16px */
    line-height: 1.25rem;
    /* 22px */
    margin-bottom: 1.5rem;
    /* 24px */
    font-weight: bold;
}

h6 {
    font-size: 0.93rem;
    /* 16px */
    line-height: 1rem;
    /* 16px */
    margin-bottom: 0.75rem;
    color: white;
}

@media (min-width: 980px) {
    h3.md-focus:before,
    h4.md-focus:before,
    h5.md-focus:before,
    h6.md-focus:before {
        color: #ddd;
        border: 1px solid #ddd;
        border-radius: 3px;
        position: absolute;
        left: -1.642857143rem;
        top: .357142857rem;
        float: left;
        font-size: 9px;
        padding-left: 2px;
        padding-right: 2px;
        vertical-align: bottom;
        font-weight: normal;
        line-height: normal;
    }

    h3.md-focus:before {
        content: 'h3';
    }

    h4.md-focus:before {
        content: 'h4';
    }

    h5.md-focus:before {
        content: 'h5';
        top: 0px;
    }

    h6.md-focus:before {
        content: 'h6';
        top: 0px;
    }
}

a {
    text-decoration: none;
    outline: 0;
}

a:hover {
    outline: 0;
}

a:focus {
    outline: thin dotted;
}

sup.md-footnote {
    background-color: #555;
    color: #ddd;
}

p {
    -ms-word-wrap: break-word;
    word-wrap: break-word;
}

p,
ul,
dd,
ol,
hr,
address,
pre,
table,
iframe,
.wp-caption,
.wp-audio-shortcode,
.wp-video-shortcode {
    margin-top: 0;
    margin-bottom: 1.5rem;
    /* 24px */
}

li > blockquote {
	margin-bottom: 0;
}

audio:not([controls]) {
    display: none;
}

[hidden] {
    display: none;
}

::-moz-selection {
    background: #4a89dc;
    color: #fff;
    text-shadow: none;
}

*.in-text-selection,
::selection {
    background: #4a89dc;
    color: #fff;
    text-shadow: none;
}

ul,
ol {
    padding: 0 0 0 1.875rem;
    /* 30px */
}

ul {
    list-style: square;
}

ol {
    list-style: decimal;
}

ul ul,
ol ol,
ul ol,
ol ul {
    margin: 0;
}

b,
th,
dt,
strong {
    font-weight: bold;
}

i,
em,
dfn,
cite {
    font-style: italic;
}

blockquote {
    padding-left: 1.875rem;
    margin: 0 0 1.875rem 1.875rem;
    border-left: solid 2px #474d54;
    padding-left: 30px;
    margin-top: 35px;
}

pre,
code,
kbd,
tt,
var {
    font-size: 0.875rem;
    font-family: Monaco, Consolas, "Andale Mono", "DejaVu Sans Mono", monospace;
}

code,
tt,
var {
    background: rgba(0, 0, 0, 0.05);
}

kbd {
    padding: 2px 4px;
    font-size: 90%;
    color: #fff;
    background-color: #333;
    border-radius: 3px;
    box-shadow: inset 0 -1px 0 rgba(0,0,0,.25);
}

pre.md-fences {
    padding: 10px 10px 10px 30px;
    margin-bottom: 20px;
    background: #333;
}

.CodeMirror-gutters {
    background: #333;
    border-right: 1px solid transparent;
}

.enable-diagrams pre.md-fences[lang="sequence"] .code-tooltip,
.enable-diagrams pre.md-fences[lang="flow"] .code-tooltip,
.enable-diagrams pre.md-fences[lang="mermaid"] .code-tooltip {
    bottom: -2.2em;
    right: 4px;
}

code,
kbd,
tt,
var {
    padding: 2px 5px;
}

table {
    max-width: 100%;
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
}

th,
td {
    padding: 5px 10px;
    vertical-align: top;
}

a {
    -webkit-transition: all .2s ease-in-out;
    transition: all .2s ease-in-out;
}

hr {
    background: #474d54;
    /* variable */
}

h1 {
    margin-top: 2em;
}

a {
    color: #e0e0e0;
    text-decoration: underline;
}

a:hover {
    color: #fff;
}

.md-inline-math script {
    color: #81b1db;
}

b,
th,
dt,
strong {
    color: #DEDEDE;
    /* variable */
}

mark {
    background: #D3D40E;
}

blockquote {
    color: #9DA2A6;
}

table a {
    color: #DEDEDE;
    /* variable */
}

th,
td {
    border: solid 1px #474d54;
    /* variable */
}

.task-list {
    padding-left: 0;
}

.md-task-list-item {
    padding-left: 1.25rem;
}

.md-task-list-item > input {
    top: auto;
}

.md-task-list-item > input:before {
    content: "";
    display: inline-block;
    width: 0.875rem;
    height: 0.875rem;
    vertical-align: middle;
    text-align: center;
    border: 1px solid #b8bfc6;
    background-color: #363B40;
    margin-top: -0.4rem;
}

.md-task-list-item > input:checked:before,
.md-task-list-item > input[checked]:before {
    content: '\221A';
    /*◘*/
    font-size: 0.625rem;
    line-height: 0.625rem;
    color: #DEDEDE;
}

/** quick open **/
.auto-suggest-container {
    border: 0px;
    background-color: #525C65;
}

#typora-quick-open {
    background-color: #525C65;
}

#typora-quick-open input{
    background-color: #525C65;
    border: 0;
    border-bottom: 1px solid grey;
}

.typora-quick-open-item {
    background-color: inherit;
    color: inherit;
}

.typora-quick-open-item.active,
.typora-quick-open-item:hover {
    background-color: #4D8BDB;
    color: white;
}

.typora-quick-open-item:hover {
    background-color: rgba(77, 139, 219, 0.8);
}

.typora-search-spinner > div {
  background-color: #fff;
}

#write pre.md-meta-block {
    border-bottom: 1px dashed #ccc;
    background: transparent;
    padding-bottom: 0.6em;
    line-height: 1.6em;
}

.btn,
.btn .btn-default {
    background: transparent;
    color: #b8bfc6;
}

.ty-table-edit {
    border-top: 1px solid gray;
    background-color: #363B40;
}

.popover-title {
    background: transparent;
}

.md-image>.md-meta {
    color: #BBBBBB;
    background: transparent;
}

.md-expand.md-image>.md-meta {
    color: #DDD;
}

#write>h3:before,
#write>h4:before,
#write>h5:before,
#write>h6:before {
    border: none;
    border-radius: 0px;
    color: #888;
    text-decoration: underline;
    left: -1.4rem;
    top: 0.2rem;
}

#write>h3.md-focus:before {
    top: 2px;
}

#write>h4.md-focus:before {
    top: 2px;
}

.md-toc-item {
    color: #A8C2DC;
}

#write div.md-toc-tooltip {
    background-color: #363B40;
}

.dropdown-menu .btn:hover,
.dropdown-menu .btn:focus,
.md-toc .btn:hover,
.md-toc .btn:focus {
    color: white;
    background: black;
}

#toc-dropmenu {
    background: rgba(50, 54, 59, 0.93);
    border: 1px solid rgba(253, 253, 253, 0.15);
}

#toc-dropmenu .divider {
    background-color: #9b9b9b;
}

.outline-expander:before {
    top: 2px;
}

#typora-sidebar {
    box-shadow: none;
    border-right: 1px dashed;
    border-right: none;
}

.sidebar-tabs {
    border-bottom:0;
}

#typora-sidebar:hover .outline-title-wrapper {
    border-left: 1px dashed;
}

.outline-title-wrapper .btn {
    color: inherit;
}

.outline-item:hover {
    border-color: #363B40;
    background-color: #363B40;
    color: white;
}

h1.md-focus .md-attr,
h2.md-focus .md-attr,
h3.md-focus .md-attr,
h4.md-focus .md-attr,
h5.md-focus .md-attr,
h6.md-focus .md-attr,
.md-header-span .md-attr {
    color: #8C8E92;
    display: inline;
}

.md-comment {
    color: #5a95e3;
    opacity: 1;
}

.md-inline-math svg {
    color: #b8bfc6;
}

#math-inline-preview .md-arrow:after {
    background: black;
}

.modal-content {
    background: var(--bg-color);
    border: 0;
}

.modal-title {
    font-size: 1.5em;
}

.modal-content input {
    background-color: rgba(26, 21, 21, 0.51);
    color: white;
}

.modal-content .input-group-addon {
    color: white;
}

.modal-backdrop {
    background-color: rgba(174, 174, 174, 0.7);
}

.modal-content .btn-primary {
    border-color: var(--primary-color);
}

.md-table-resize-popover {
    background-color: #333;
}

.form-inline .input-group .input-group-addon {
    color: white;
}

#md-searchpanel {
    border-bottom: 1px dashed grey;
}

/** UI for electron */

.context-menu,
#spell-check-panel,
#footer-word-count-info {
    background-color: #42464A;
}

.context-menu.dropdown-menu .divider,
.dropdown-menu .divider {
    background-color: #777777;
}

footer {
    color: inherit;
}

@media (max-width: 1000px) {
    footer {
        border-top: none;
    }
    footer:hover {
        color: inherit;
    }
}

#file-info-file-path .file-info-field-value:hover {
    background-color: #555;
    color: #dedede;
}

.megamenu-content,
.megamenu-opened header {
    background: var(--bg-color);
}

.megamenu-menu-panel h2,
.megamenu-menu-panel h1,
.long-btn {
    color: inherit;
}

.megamenu-menu-panel input[type='text'] {
    background: inherit;
    border: 0;
    border-bottom: 1px solid;
}

#recent-file-panel-action-btn {
    background: inherit;
    border: 1px grey solid;
}

.megamenu-menu-panel .dropdown-menu > li > a {
    color: inherit;
    background-color: #2F353A;
    text-decoration: none;
}

.megamenu-menu-panel table td:nth-child(1) {
    color: inherit;
    font-weight: bold;
}

.megamenu-menu-panel tbody tr:hover td:nth-child(1) {
    color: white;
}

.modal-footer .btn-default, 
.modal-footer .btn-primary,
.modal-footer .btn-default:not(:hover) {
    border: 1px solid;
    border-color: transparent;
}

.btn-default:hover, .btn-default:focus, .btn-default.focus, .btn-default:active, .btn-default.active, .open > .dropdown-toggle.btn-default {
    color: white;
    border: 1px solid #ddd;
    background-color: inherit;
}

.modal-header {
    border-bottom: 0;
}

.modal-footer {
    border-top: 0;
}

#recent-file-panel tbody tr:nth-child(2n-1) {
    background-color: transparent !important;
}

.megamenu-menu-panel tbody tr:hover td:nth-child(2) {
    color: inherit;
}

.megamenu-menu-panel .btn {
    border: 1px solid #eee;
    background: transparent;
}

.mouse-hover .toolbar-icon.btn:hover,
#w-full.mouse-hover,
#w-pin.mouse-hover {
    background-color: inherit;
}

.typora-node::-webkit-scrollbar {
    width: 5px;
}

.typora-node::-webkit-scrollbar-thumb:vertical {
    background: rgba(250, 250, 250, 0.3);
}

.typora-node::-webkit-scrollbar-thumb:vertical:active {
    background: rgba(250, 250, 250, 0.5);
}

#w-unpin {
    background-color: #4182c4;
}

#top-titlebar, #top-titlebar * {
    color: var(--item-hover-text-color);
}

.typora-sourceview-on #toggle-sourceview-btn,
#footer-word-count:hover,
.ty-show-word-count #footer-word-count {
    background: #333333;
}

#toggle-sourceview-btn:hover {
    color: #eee;
    background: #333333;
}

/** focus mode */
.on-focus-mode .md-end-block:not(.md-focus):not(.md-focus-container) * {
    color: #686868 !important;
}

.on-focus-mode .md-end-block:not(.md-focus) img,
.on-focus-mode .md-task-list-item:not(.md-focus-container)>input {
    opacity: #686868 !important;
}

.on-focus-mode li[cid]:not(.md-focus-container){
    color: #686868;
}

.on-focus-mode .md-fences.md-focus .CodeMirror-code>*:not(.CodeMirror-activeline) *,
.on-focus-mode .CodeMirror.cm-s-inner:not(.CodeMirror-focused) * {
    color: #686868 !important;
}

.on-focus-mode .md-focus,
.on-focus-mode .md-focus-container {
    color: #fff;
}

.on-focus-mode #typora-source .CodeMirror-code>*:not(.CodeMirror-activeline) * {
    color: #686868 !important;
}


/*diagrams*/
#write .md-focus .md-diagram-panel {
    border: 1px solid #ddd;
    margin-left: -1px;
    width: calc(100% + 2px);
}

/*diagrams*/
#write .md-focus.md-fences-with-lineno .md-diagram-panel {
    margin-left: auto;
}

.md-diagram-panel-error {
    color: #f1908e;
}

.active-tab-files #info-panel-tab-file,
.active-tab-files #info-panel-tab-file:hover,
.active-tab-outline #info-panel-tab-outline,
.active-tab-outline #info-panel-tab-outline:hover {
    color: #eee;
}

.sidebar-footer-item:hover,
.footer-item:hover {
    background: inherit;
    color: white;
}

.ty-side-sort-btn.active,
.ty-side-sort-btn:hover,
.selected-folder-menu-item a:after {
    color: white;
}

#sidebar-files-menu {
    border:solid 1px;
    box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.79);
    background-color: var(--bg-color);
}

.file-list-item {
    border-bottom:none;
}

.file-list-item-summary {
    opacity: 1;
}

.file-list-item.active:first-child {
    border-top: none;
}

.file-node-background {
    height: 32px;
}

.file-library-node.active>.file-node-content,
.file-list-item.active {
    color: white;
    color: var(--active-file-text-color);
}

.file-library-node.active>.file-node-background{
    background-color: rgb(34, 34, 34);
    background-color: var(--active-file-bg-color);
}
.file-list-item.active {
    background-color: rgb(34, 34, 34);
    background-color: var(--active-file-bg-color);
}

#ty-tooltip {
    background-color: black;
    color: #eee;
}

.md-task-list-item>input {
    margin-left: -1.3em;
    margin-top: 0.3rem;
    -webkit-appearance: none;
}

.md-mathjax-midline {
    background-color: #57616b;
    border-bottom: none;
}

footer.ty-footer {
    border-color: #656565;
}

.ty-preferences .btn-default {
    background: transparent;
}
.ty-preferences .btn-default:hover {
    background: #57616b;
}

.ty-preferences select {
    border: 1px solid #989698;
    height: 21px;
}

.ty-preferences .nav-group-item.active {
    background: var(--item-hover-bg-color);
}

.ty-preferences input[type="search"] {
    border-color: #333;
    background: #333;
    line-height: 22px;
    border-radius: 6px;
    color: white;
}

.ty-preferences input[type="search"]:focus {
    box-shadow: none;
}

[data-is-directory="true"] .file-node-content {
    margin-bottom: 0;
}

.file-node-title {
    line-height: 22px;
}

.html-for-mac .file-node-open-state, .html-for-mac .file-node-icon {
    line-height: 26px;
}

::-webkit-scrollbar-thumb {
    background: rgba(230, 230, 230, 0.30);
}

::-webkit-scrollbar-thumb:active {
    background: rgba(230, 230, 230, 0.50);
}

#typora-sidebar:hover div.sidebar-content-content::-webkit-scrollbar-thumb:horizontal {
    background: rgba(230, 230, 230, 0.30);
}

.nav-group-item:active {
    background-color: #474d54;
}

.md-search-hit {
    background: rgba(199, 140, 60, 0.81);
    color: #eee;
}

.md-search-hit * {
    color: #eee;
}

#md-searchpanel input {
    color: white;
}


</style>
</head>
<body class="typora-export os-windows">
<div id="write" class="is-node"><div class="md-toc" mdtype="toc"><p class="md-toc-content" role="list"><span role="listitem" class="md-toc-item md-toc-h1" data-ref="n91"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#coding-challenges">Coding Challenges</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n6"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#challenge-1">Challenge 1</a></span><span role="listitem" class="md-toc-item md-toc-h4" data-ref="n8"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#sample-input">Sample input</a></span><span role="listitem" class="md-toc-item md-toc-h4" data-ref="n19"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#sample-output">Sample output</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n9"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#challenge-2">Challenge 2</a></span><span role="listitem" class="md-toc-item md-toc-h4" data-ref="n43"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#sample-input-n43">Sample input</a></span><span role="listitem" class="md-toc-item md-toc-h4" data-ref="n79"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#sample-output-n79">Sample output</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n165"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#evaluate">Evaluate</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n174"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#approach">Approach</a></span><span role="listitem" class="md-toc-item md-toc-h4" data-ref="n134"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#challenge-1-n134">Challenge 1:</a></span><span role="listitem" class="md-toc-item md-toc-h4" data-ref="n142"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#challenge-2-n142">Challenge 2:</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n99"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#improvements">Improvements</a></span><span role="listitem" class="md-toc-item md-toc-h2" data-ref="n131"><a class="md-toc-inner" href="file:///C:/Users/guras/Downloads/Coding%20Challenges.html#support">Support</a></span></p></div><p>&nbsp;</p><h1><a name="coding-challenges" class="md-header-anchor"></a><span>Coding Challenges</span></h1><p><span>Calculate the yield spread (return) between a corporate bond and its government bond benchmark.</span></p><p><span>Calculate the spread to the government bond curve. </span></p><h2><a name="challenge-1" class="md-header-anchor"></a><span>Challenge 1</span></h2><p><span>Calculate the yield spread (return) between a corporate bond and its government bond benchmark.</span>
<span>A government bond is a good benchmark if it is as close as possible to the corporate bond in terms of years to maturity (term).</span></p><h4><a name="sample-input" class="md-header-anchor"></a><span>Sample input</span></h4><p><img src="./readme_files/Capture.PNG" style="zoom:50%;"></p><h4><a name="sample-output" class="md-header-anchor"></a><span>Sample output</span></h4><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang=""><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang=""><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation"><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">bond,benchmark,spread_to_benchmark</span></pre></div><div class="" style="position: relative;"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">C1,G1,1.60%</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom: 0px solid transparent; top: 52px;"></div><div class="CodeMirror-gutters" style="display: none; height: 52px;"></div></div></div></pre><p><span>To explain, the best candidate for a benchmark for C1 (corporate bond) is the G1 (government bond) since their difference in term is only 0.9 years vs G2 that is 1.7 years away. Hence, the </span><code>spread_to_benchmark</code><span> for C1 is C1.yield - G1.yield = 1.60%.</span></p><p><span>Given a list of corporate and government bonds, find a benchmark bond for each corporate bond and calculate the spread to benchmark.</span></p><h2><a name="challenge-2" class="md-header-anchor"></a><span>Challenge 2</span></h2><p><span>The next challenge is calculate the spread to the government bond curve.</span></p><p><span>Since the corporate bond term is not exactly the same as its benchmark term, we need to use linear interpolation to dermine the spread to the curve.</span></p><h4><a name="sample-input-n43" class="md-header-anchor"></a><span>Sample input</span></h4><p><img src="./readme_files/Capture 2.PNG" alt="Capture 2" style="zoom:50%;"></p><h4><a name="sample-output-n79" class="md-header-anchor"></a><span>Sample output</span></h4><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang=""><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang=""><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation"><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">bond,spread_to_curve</span></pre></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">C1,1.22%</span></pre><div class="" style="position: relative;"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">C2,2.98%</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom: 0px solid transparent; top: 78px;"></div><div class="CodeMirror-gutters" style="display: none; height: 78px;"></div></div></div></pre><p><span>Image below (attached) will help you visualize how to calculate spread to curve.</span></p><p><img src="./readme_files/spread_calculator.png" alt="spread_calculator" style="zoom:70%;"></p><p><span>The formula is: </span></p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang=""><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang=""><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation"><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">C1.spread_to_curve = A - B</span></pre></div><div class="" style="position: relative;"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">C2.spread_to_curve = X - Y</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom: 0px solid transparent; top: 52px;"></div><div class="CodeMirror-gutters" style="display: none; height: 52px;"></div></div></div></pre><p><span>Where </span><code>A = C1.yield = 5.30%</code><span> and </span><code>X = C2.yield = 8.30%</code><span>. Values of B and Y require linear interpolation to determine. We leave this as an exercise to the challenger.</span></p><p><span>You can assume that the list of bonds will always contain at least one government bond with a term less all the corporate bonds. As well, it will contain at least one government bond with a term greater than all the corporate bonds. So that you will always be able to calculate </span><code>spread_to_curve</code><span> for each corporate bond.</span></p><h2><a name="evaluate" class="md-header-anchor"></a><span>Evaluate</span></h2><p><span>To run in Ubuntu, git clone the repository and move all the input csv files to this cloned folder.</span></p><p><span>Note: Have all the files in the same directory. This includes the the csv files as well.</span></p><p><img src="./readme_files/image-20200324025005928.png" referrerpolicy="no-referrer" alt="image-20200324025005928"></p><p><span>Same approach for coding_challenge_2.py</span></p><p><img src="./readme_files/image-20200324025155107.png" referrerpolicy="no-referrer" alt="image-20200324025155107"></p><h2><a name="approach" class="md-header-anchor"></a><span>Approach</span></h2><p><span>My approach for both the challenges was pretty simple. </span></p><h4><a name="challenge-1-n134" class="md-header-anchor"></a><span>Challenge 1:</span></h4><p><span>I decided to import csv module to make reading csv files easier. I first used csv module to covert each row in a dictionary and stored it in a list. I then worked on this list to find the corporate bond dicts and then found the required government bond dicts. Most of this is done in </span><code>calculate_yield_spread()</code><span> method. </span></p><h4><a name="challenge-2-n142" class="md-header-anchor"></a><span>Challenge 2:</span></h4><p><span>Just like challenge 1, I imported csv module to make reading csv files easier again to make processing of data easier. I converted each row in a dictionary and then stored all the rows in a list. </span></p><p><span>For this challenge unlike the first, I implemented a divide and conquer approach. the whole program is divided in small methods that get called in </span><code>process()</code><span> method to make program more readable. </span></p><p><code>get_term()</code><span> and </span><code>get_yield()</code><span> do most of the input processing for term and yield fields in the </span><code>sample_input.csv</code><span> file. </span></p><p><code>upper_bound()</code><span> and </span><code>lower_bound()</code><span> calculate the upper bound (government bond ) and lower bound (government bond) for the required corporate bond. </span></p><p><span>When the bounds are founds the actual calculation is done in </span><code>spread_calculator()</code><span> method.</span></p><p><span>  </span></p><h2><a name="improvements" class="md-header-anchor"></a><span>Improvements</span></h2><p><span>If I had more time to contribute to this project, I will learn complex unit testing with the mock module. With this challenge, I have realized that my unit testing knowledge is really limited (only straightforward functions/methods.)</span></p><h2><a name="support" class="md-header-anchor"></a><span>Support</span></h2><p><span>For any questions contact  me at </span><a href="mailto:gurashish1000@gmail.com" target="_blank" class="url">gurashish1000@gmail.com</a></p></div>

</body></html>