let totalIn = 0;
let totalOut=0;

let count = 0;
document.getElementById('increaseBtn').onclick = function() {
  count += 1;
  totalIn += 1;
  document.getElementById("countLabel").innerHTML = count;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn').onclick = function() {
  count -= 1;
  totalOut += 1;
  document.getElementById("countLabel").innerHTML = count;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}

let count2 = 0;
document.getElementById('increaseBtn2').onclick = function() {
  count2 += 1;
  totalIn += 1;
  document.getElementById("countLabel2").innerHTML = count2;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn2').onclick = function() {
  count2 -= 1;
  totalOut += 1;
  document.getElementById("countLabel2").innerHTML = count2;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}

let count3 = 0;
document.getElementById('increaseBtn3').onclick = function() {
  count3 += 1;
  totalIn += 1;
  document.getElementById("countLabel3").innerHTML = count3;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn3').onclick = function() {
  count3 -= 1;
  totalOut += 1;
  document.getElementById("countLabel3").innerHTML = count3;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}


let count4 = 0;
document.getElementById('increaseBtn4').onclick = function() {
  count4 += 1;
  totalIn += 1;
  document.getElementById("countLabel4").innerHTML = count4;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn4').onclick = function() {
  count4 -= 1;
  totalOut += 1;
  document.getElementById("countLabel4").innerHTML = count4;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}




let count5 = 0;
document.getElementById('increaseBtn5').onclick = function() {
  count5 += 1;
  totalIn += 1;
  document.getElementById("countLabel5").innerHTML = count5;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn5').onclick = function() {
  count5 -= 1;
  totalOut += 1;
  document.getElementById("countLabel5").innerHTML = count5;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}

let count6 = 0;
document.getElementById('increaseBtn6').onclick = function() {
  count6 += 1;
  totalIn += 1;
  document.getElementById("countLabel6").innerHTML = count6;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn6').onclick = function() {
  count6 -= 1;
  totalOut += 1;
  document.getElementById("countLabel6").innerHTML = count6;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}

let count7 = 0;
document.getElementById('increaseBtn7').onclick = function() {
  count7 += 1;
  totalIn += 1;
  document.getElementById("countLabel7").innerHTML = count7;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn7').onclick = function() {
  count7 -= 1;
  totalOut += 1;
  document.getElementById("countLabel7").innerHTML = count7;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}

let count8 = 0;
document.getElementById('increaseBtn8').onclick = function() {
  count8 += 1;
  totalIn += 1;
  document.getElementById("countLabel8").innerHTML = count8;
  document.getElementById("totalcount").innerHTML = totalIn;
}

document.getElementById('decreaseBtn8').onclick = function() {
  count8 -= 1;
  totalOut += 1;
  document.getElementById("countLabel8").innerHTML = count8;
  document.getElementById("totalcountOut").innerHTML = totalOut;
}

document.getElementById('submit').onclick = async function() {
  const response = await fetch("http://localhost:8000/api/submit/", {
        method: "POST",
        mode: 'cors',
        crossorigin: 'true',
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "http://127.0.0.1:5000", 'Access-Control-Allow-Credentials': 'true' },
        body: JSON.stringify(
          {
            "shirt": count,
            "tankTop": count2,
            "longSleeve": count3,
            "jacket": count4,
            "pants": count5,
            "jeans": count6,
            "shorts": count7,
            "skirt": count8,
            "totalIn": totalIn,
            "totalOut": totalOut
          })
      });
  const jsonData = await response.json();
  console.log(jsonData);
  count=0;
  count2=0;
  count3=0;
  count4=0;
  count5=0;
  count6=0;
  count7=0;
  count8=0;
  totalIn=0;
  totalOut=0;
  document.getElementById("countLabel").innerHTML = count;
  document.getElementById("countLabel2").innerHTML = count2;
  document.getElementById("countLabel3").innerHTML = count3;
  document.getElementById("countLabel4").innerHTML = count4;
  document.getElementById("countLabel5").innerHTML = count5;
  document.getElementById("countLabel6").innerHTML = count6;
  document.getElementById("countLabel7").innerHTML = count7;
  document.getElementById("countLabel8").innerHTML = count8;
  document.getElementById("totalcount").innerHTML = totalIn;
  document.getElementById("totalcountOut").innerHTML = totalOut;

}


