var span = document.getElementsByTagName('span')
var portfolio = document.getElementsByClassName('portfolio')

var l = 0;

span[1].onclick = () => {
    l++;
    for(var i of portfolio) {
        if (l==0) {i.style.left = "0%";}
        if (l==1) {i.style.left = "-33.333%";}
        if (l==2) {i.style.left = "-66.666%";}
        if (l==3) {i.style.left = "-99.999%";}
        if (l==4) {i.style.left = "-133.329%";}
        if (l>3) {l=4;}
    }
}


span[0].onclick = () => {
    l--;
    for(var i of portfolio) {
        if (l==0) {i.style.left = "0%";}
        if (l==1) {i.style.left = "-33.333%";}
        if (l==2) {i.style.left = "-66.666%";}
        if (l==3) {i.style.left = "-99.999%";}
        if (l<0) {l=0;}
    }

}