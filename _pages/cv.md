---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Aeronautical and Astronautical Engineering, 2023
* M.S. in Computer Science with a specialization in Perception, 2016
* M.S. in Electrical and Computer Engineering, 2016
* BEng (Hons.) in Electronics and Communications Engineering with a year in Industry, 2013

Work experience
======
  
Skills
======

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
