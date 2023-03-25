const d = new Date();

document.getElementById("login").onclick = function () {
    document.getElementById("lol").innerHTML = d;
    document.getElementById("login1").style.background = "blue"
    document.getElementById("a1").remove();
    document.getElementById("a2").remove();
    document.getElementById("wal").innerHTML=String("480C");


}

document.getElementById("lol3").onclick = function () {
    document.getElementById("lol2").innerHTML = d;
    document.getElementById("duration").remove();
    document.getElementById("durationContainer").innerHTML=String("1 hour") ;
    document.getElementById("wal").innerHTML=String("490C");
}

document.getElementById("wallet").onclick = function () {
    location.href =  "file:///F:/Programming/Hackathon/Hashcode/hashcode-meandthebois/site/Smart-Parking/figmatohtml/9/9.html";
}
