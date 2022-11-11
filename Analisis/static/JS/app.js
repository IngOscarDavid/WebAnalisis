function Euler() {
    document.getElementById('F1').style.display = 'block';
    document.getElementById('F2').style.display = 'none';
    document.getElementById('F3').style.display = 'none';
}
function Heun() {
    document.getElementById('F2').style.display = 'block';
    document.getElementById('F1').style.display = 'none';
    document.getElementById('F3').style.display = 'none';
}
function Runge() {
    document.getElementById('F3').style.display = 'block';
    document.getElementById('F2').style.display = 'none';
    document.getElementById('F1').style.display = 'none';
}
