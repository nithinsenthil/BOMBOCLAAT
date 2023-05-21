let count = 0;

document.getElementById('decreaseBtn').onclick = function() {
  count -= 1;
  document.getElementById("countLabel").innerHTML = count;
}

document.getElementById('increaseBtn').onclick = function() {
  count += 1;
  document.getElementById("countLabel").innerHTML = count;
}

document.getElementById('decreaseBtn1').onclick = function() {
  count -= 1;
  document.getElementById("countLabel1").innerHTML = count;
}

document.getElementById('increaseBtn1').onclick = function() {
  count += 1;
  document.getElementById("countLabel1").innerHTML = count;
}


