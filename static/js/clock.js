var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var ctx1 = canvas.getContext("2d");
var radius = canvas.height / 2;
// ctx.translate(radius, radius);
ctx1.translate(radius, radius);

// ctx1.translate(radius+200, radius);
radius = radius * 0.90


// radius1 = radius1 * 0.90
// setInterval(drawClock1, 1000);

setInterval(drawClock, 1000)   

// setInterval(drawClock1, 1000) 
var n1 = 7;
var n2 = 8;



function drawClock() {
  drawFace(ctx, radius); 
  drawNumbers(ctx, radius);
  drawTime(ctx, radius, n1);
  drawTime(ctx1, radius, n2);
}
// function drawClock1() {
//   drawFace(ctx, radius); 
//   drawNumbers(ctx, radius);
//   // drawTime(ctx, radius, n1);
//   drawTime(ctx, radius, n2);
// }


function drawFace(ctx, radius) {
  var grad;
  ctx.beginPath();
  ctx.arc(0, 0, radius, 0, 2*Math.PI);
  ctx.fillStyle = 'white';
  ctx.fill(); //The face
  grad = ctx.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05);
  grad.addColorStop(0, '#333');
  grad.addColorStop(0.5, 'blue');
  grad.addColorStop(1, '#333');
  // ctx.strokeStyle = grad;
  // ctx.lineWidth = radius*0.1;
  // ctx.stroke();
  // ctx.beginPath();
  // ctx.arc(0, 0, radius*0.1, 0, 2*Math.PI);
  // ctx.fillStyle = '#333';

  // ctx.fill();
}

// function drawFace1(ctx1, radius1) {
//   var grad1;
//   ctx1.beginPath();
//   ctx1.arc(0, 0, radius, 0, 2*Math.PI);
//   ctx1.fillStyle = 'white';
//   ctx1.fill(); //The face
//   grad1 = ctx1.createRadialGradient(0,0,radius1*0.95, 0,0,radius1*1.05);
//   grad1.addColorStop(0, '#333');
//   grad1.addColorStop(0.5, 'blue');
//   grad1.addColorStop(1, '#333');

// }


function drawNumbers(ctx, radius) {
  var ang;
  var num;
  ctx.font = radius*0.15 + "px arial";
  ctx.textBaseline="middle";
  ctx.textAlign="center";
  for(num = 1; num < 13; num++){
    ang = num * Math.PI / 6;
    // ctx.rotate(ang);
    // ctx.translate(0, -radius*0.85);
    // ctx.rotate(-ang);
    // ctx.fillText(num.toString(), 0, 0);
    // ctx.rotate(ang);
    // ctx.translate(0, radius*0.85);
    // ctx.rotate(-ang);
  }
}

function drawTime(ctx, radius, n, t1, t2){
    var now = new Date();
    var hour = now.getHours();
    
    var minute = now.getMinutes();
    var second = now.getSeconds();
    //hour
    hour=hour%1 + n;
    ctx.translate(t1, t2)
    hour=(hour*Math.PI/6)+
    (minute*Math.PI/(6*60))+
    (second*Math.PI/(360*60));
    drawHand(ctx, hour, radius*0.58, radius*0.03);
    //minute
    minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
    drawHand(ctx, minute, radius*0.65, radius*0.018);
    // second
    second=(second*Math.PI/30);
    drawHand(ctx, second, radius*0.70, radius*0.007);
}

function drawTime(ctx, radius, n){
    var now = new Date();
    var hour = now.getHours();
    // ctx.translate(600, 0)
    var minute = now.getMinutes();
    var second = now.getSeconds();




    //hour
    hour=hour%1+n;

    hour=(hour*Math.PI/6)+
    (minute*Math.PI/(6*60))+
    (second*Math.PI/(360*60));
    drawHand(ctx, hour, radius*0.58, radius*0.03);
    //minute
    minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
    drawHand(ctx, minute, radius*0.65, radius*0.018);
    // second
    second=(second*Math.PI/30);
    drawHand(ctx, second, radius*0.70, radius*0.007);
}





function drawHand(ctx, pos, length, width) {
    ctx.beginPath();
    ctx.lineWidth = width;
    ctx.lineCap = "round";
    ctx.moveTo(0,0);
    ctx.rotate(pos);
    ctx.lineTo(0, -length);
    ctx.stroke();
    ctx.rotate(-pos);

}