var tytvisible = document.getElementById('tytvisible');
var tythidden = document.getElementById('tythidden');
var alltyt = document.getElementById('alltyt');

var aytvisible = document.getElementById('aytvisible');
var aythidden = document.getElementById('aythidden');
var allayt = document.getElementById('allayt');


var formToDo = document.getElementById('formToDo');
var createToDo = document.getElementById('createToDo');

function hideTYT(){
  alltyt.style.display="none";
  tythidden.style.display="none";
  tytvisible.style.display="block";
  tytvisible.style.opacity = "1";
}

function visibleTYT(){
  alltyt.style.display="block";
  tythidden.style.display="block";
  tytvisible.style.display="none";
  tytvisible.style.opacity = "0.5";

}

function hideAYT(){
  allayt.style.display="none";
  aythidden.style.display="none";
  aytvisible.style.display="block";
  aytvisible.style.opacity = "1";
}

function visibleAYT(){
  allayt.style.display="block";
  aythidden.style.display="block";
  aytvisible.style.display="none";
  aytvisible.style.opacity = "0.5";

}

function visibleToDo(){
  formToDo.style.display="block";
}
