<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{{title or 'HILT Institute'}}</title>
<style type="text/css">
@import url(static/css/main.css);
%for stylesheet in addstyles:
@import url(static/css/{{stylesheet}});
%end
</style>
</head>

<body>
<header>
<img src="static/images/logo.png" alt="HILT Institute">
<h2>Arlington Career Center</h2>
<h1>HILT Institute</h1>
<h3>Celebrating Cultures, Languages &amp; Dreams</h3>
<nav>
<a href='/'>Home</a>
<a href='/aboutus'>About Us</a>
<a href='/staff'>Staff</a>
<a href='/'>Students</a>
<a href='/'>Counseling</a>
<a href='/'>Academics</a>
<a href='/'>Activities</a>
<a href='/'>Parents</a>
<a href='/calendar'>Calendar</a>
</nav>
</header>

<section>
  %include
</section>

<footer>
<a href="http://validator.w3.org/check/referer">
<strong> HTML </strong> Valid! </a>
<a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
<strong> CSS </strong> Valid! </a>
</footer>

</body>
</html>
