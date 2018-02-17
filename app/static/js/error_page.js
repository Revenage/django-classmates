"use strict";

(function() {
  var number = '404';
  var num_arr = number.split('');
  function randomNum() {
    return Math.floor(Math.random() * 9) + 1;
  }
  var time = 30,
    loppArr = []
  var selector = ['third', 'second', 'first']
	var i = 0;
  
  function run(s,j) {
  	 var currentselector = document.querySelector('.'+ s + 'Digit');
    loppArr[j] = setInterval(function() {
    	var num = j;
      if (i > num * 40 + 40) {
        clearInterval(loppArr[num]);
        currentselector.textContent = num_arr[num];
      } else {
        currentselector.textContent = randomNum();
        i++;
      }
    }, time);
  }
  selector.map(run)
})()