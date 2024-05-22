document.addEventListener('DOMContentLoaded', function () {
    // element-one: Dupla kattintásra hozzáad egy "animation" class-t kattintáskor
    const elementOne = document.getElementById('element-one');
elementOne.ondblclick=function(){
    elementOne.classList.add("animation")
}
    // element-two: Ha rámegy az egér, hozzáad egy box-shadow-t
    const elementTwo = document.getElementById('element-two');
elementTwo.onmouseover=function(){
    elementTwo.style.boxShadow="5px 10px black"
}
    // element-three: Kattintásra eltűnik
    const elementThree = document.getElementById('element-three');
elementThree.onclick=function(){
    elementThree.style.opacity=0
}
    // element-four: Kattintásra a háttere zöld lesz
    const elementFour = document.getElementById('element-four');
elementFour.onclick=function(){
    elementFour.style.backgroundColor="green"
}
});